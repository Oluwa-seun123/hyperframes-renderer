import { readdir, mkdir, copyFile, writeFile, stat, readFile } from 'node:fs/promises';
import { resolve, join, extname, basename } from 'node:path';
import { spawnSync } from 'node:child_process';
const project=resolve(process.cwd()),outDir=join(project,'output','delivery');
const audioPath=resolve(process.env.HFX_AUDIO_FILE||join(project,'audio','audio-master.wav'));
function run(cmd,args){const r=spawnSync(cmd,args,{encoding:'utf8',maxBuffer:16*1024*1024});if(r.error)throw r.error;if(r.status!==0)throw new Error(cmd+' exited '+r.status+': '+(r.stderr||r.stdout||'').slice(-4000));return r.stdout||''}
async function walk(dir,found=[]){for(const item of await readdir(dir,{withFileTypes:true})){if(['node_modules','.git','output'].includes(item.name))continue;const p=join(dir,item.name);if(item.isDirectory())await walk(p,found);else if(extname(item.name).toLowerCase()==='.mp4')found.push(p)}return found}
function probe(file){return JSON.parse(run('ffprobe',['-v','error','-show_entries','format=duration,size:stream=index,codec_type,codec_name,width,height,sample_rate,channels','-of','json',file]))}
const candidates=await walk(project);if(!candidates.length)throw new Error('No rendered MP4 found in the project folder.');
const videos=await Promise.all(candidates.map(async path=>({path,mtime:(await stat(path)).mtimeMs})));videos.sort((a,b)=>b.mtime-a.mtime);
const source=videos[0].path,srcInfo=probe(source),videoStream=srcInfo.streams?.find(s=>s.codec_type==='video');
if(!videoStream||!(Number(srcInfo.format?.duration)>0))throw new Error('Rendered file is not a valid MP4 with a video stream and positive duration.');
const videoDuration=Number(srcInfo.format.duration),html=await readFile(join(project,'index.html'),'utf8');
const declared=Number(html.match(/data-duration=["']([0-9.]+)/)?.[1]||0),checks=[];
checks.push({name:'MP4 container and video stream',status:'PASS',detail:(videoStream.codec_name||'video')+' '+(videoStream.width||'?')+'x'+(videoStream.height||'?')+' · '+videoDuration.toFixed(2)+' s'});
checks.push({name:'Declared composition duration',status:declared?(Math.abs(declared-videoDuration)<=Math.max(1,declared*.03)?'PASS':'WARN'):'SKIP',detail:declared?'Composition '+declared+'s; rendered '+videoDuration.toFixed(2)+'s':'No data-duration metadata found.'});
await mkdir(outDir,{recursive:true});
const base='hfx-final-delivery',videoOnly=join(outDir,base+'-video-only.mp4'),finalVideo=join(outDir,base+'.mp4');let audioUsed=false;
let audioExists=true;try{await stat(audioPath)}catch(e){if(e.code==='ENOENT')audioExists=false;else throw e}if(audioExists){const aProbe=probe(audioPath);if(!aProbe.streams?.some(s=>s.codec_type==='audio'))throw new Error('WAV has no audio stream');run('ffmpeg',['-y','-i',source,'-i',audioPath,'-map','0:v:0','-map','1:a:0','-c:v','copy','-c:a','aac','-b:a','320k','-af','apad','-t',String(videoDuration),'-movflags','+faststart',finalVideo]);audioUsed=true}
if(!audioUsed)await copyFile(source,videoOnly);
const delivered=audioUsed?finalVideo:videoOnly,finalInfo=probe(delivered),finalAudio=finalInfo.streams?.some(s=>s.codec_type==='audio')||false;
if(audioUsed&&!finalAudio)throw new Error('Mux result has no audio stream.');
checks.push({name:'Audio master supplied',status:audioUsed?'PASS':'WARN',detail:audioUsed?'WAV muxed into MP4 as AAC at 320 kb/s.':'No audio master at '+audioPath+'; video-only output packaged.'});
checks.push({name:'Final MP4 audio stream',status:finalAudio?'PASS':'WARN',detail:finalAudio?'Audio stream detected.':'No audio stream detected.'});
checks.push({name:'Final file duration',status:Math.abs(Number(finalInfo.format.duration)-videoDuration)<=.15?'PASS':'FAIL',detail:Number(finalInfo.format.duration).toFixed(2)+' s'});
const report={format:'hfx-render-qc',version:1,createdAt:new Date().toISOString(),sourceVideo:basename(source),deliveredFile:basename(delivered),audioMaster:audioUsed?basename(audioPath):null,videoDurationSeconds:videoDuration,output:{width:videoStream.width||null,height:videoStream.height||null,videoCodec:videoStream.codec_name||null,audioPresent:finalAudio},checks,notes:['Black-frame and visual quality require human review.','This checks media streams and metadata; it cannot judge realism, composition quality or factual accuracy.']};
await writeFile(join(outDir,'quality-report.json'),JSON.stringify(report,null,2));
await writeFile(join(outDir,'quality-report.md'),'# HFX Render Quality Report\n\n- Delivered: '+basename(delivered)+'\n- Duration: '+videoDuration.toFixed(2)+' seconds\n- Resolution: '+(videoStream.width||'?')+' × '+(videoStream.height||'?')+'\n- Audio included: '+(finalAudio?'Yes':'No')+'\n\n| Check | Result | Detail |\n|---|---|---|\n'+checks.map(c=>'| '+c.name+' | '+c.status+' | '+c.detail+' |').join('\n')+'\n\n## Human review required\n'+report.notes.map(n=>'- '+n).join('\n')+'\n');
run('zip',['-j','-q',join(outDir,base+'.zip'),delivered,join(outDir,'quality-report.json'),join(outDir,'quality-report.md')]);
console.log(JSON.stringify({source,delivered,zip:join(outDir,base+'.zip'),audioUsed,checks},null,2));
if(checks.some(c=>c.status==='FAIL'))process.exitCode=1;
