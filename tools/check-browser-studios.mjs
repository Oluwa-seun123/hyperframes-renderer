import { readFile, mkdtemp, writeFile, rm } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { spawnSync } from 'node:child_process';

const files = ['image-motion-studio/3d-engine.html','image-motion-studio/render-pipeline.html'];
const dir = await mkdtemp(join(tmpdir(),'hfx-browser-check-'));
let failed = false;
try {
  for (const file of files) {
    const html = await readFile(file,'utf8');
    const scripts = [...html.matchAll(/<script\\s+type=["']module["'][^>]*>([\\s\\S]*?)<\\/script>/gi)];
    if (!scripts.length) { console.error('FAIL '+file+': no module script found'); failed = true; continue; }
    for (let i=0;i<scripts.length;i++) {
      const path=join(dir, file.replaceAll('/','_')+'-'+i+'.mjs');
      await writeFile(path,scripts[i][1]);
      const result=spawnSync(process.execPath,['--check',path],{encoding:'utf8'});
      if(result.status!==0){console.error('FAIL '+file+' module '+i+'\\n'+result.stderr);failed=true}
      else console.log('PASS '+file+' module '+i);
    }
    if(file.endsWith('render-pipeline.html')){
      for(const token of ['hfx-shot-plan','orbit360','captureStream','Export shot plan JSON']) if(!html.includes(token)){console.error('FAIL '+file+': missing '+token);failed=true}
    }
  }
} finally { await rm(dir,{recursive:true,force:true}); }
if(failed) process.exit(1);
console.log('HFX browser studio checks passed.');
