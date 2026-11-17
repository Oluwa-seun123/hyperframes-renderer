import { readFile, mkdtemp, writeFile, rm } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import { join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import { spawnSync } from 'node:child_process';

const files = [
  { path: 'image-motion-studio/3d-engine.html', mode: 'module' },
  { path: 'image-motion-studio/render-pipeline.html', mode: 'module' },
  { path: 'image-motion-studio/hfx-hyperframes-exporter.html', mode: 'classic' },
  { path: 'image-motion-studio/production-intelligence.html', mode: 'classic' },
];
const root = fileURLToPath(new URL('..', import.meta.url));
const dir = await mkdtemp(join(tmpdir(),'hfx-browser-check-'));
let failed = false;
try {
  for (const file of files) {
    const html = await readFile(resolve(root,file.path),'utf8');
    const pattern = file.mode === 'module'
      ? /<script\s+type=["']module["'][^>]*>([\s\S]*?)<\/script>/gi
      : /<script>([\s\S]*?)<\/script>/i;
    const scripts = [...html.matchAll(pattern)];
    if (!scripts.length) { console.error('FAIL '+file.path+': no target script found'); failed = true; continue; }
    for (let i=0;i<scripts.length;i++) {
      const ext = file.mode === 'module' ? '.mjs' : '.js';
      const path = join(dir, file.path.replaceAll('/','_')+'-'+i+ext);
      await writeFile(path,scripts[i][1]);
      const result = spawnSync(process.execPath,['--check',path],{encoding:'utf8'});
      if(result.status!==0){console.error('FAIL '+file.path+' script '+i+'\n'+result.stderr);failed=true}
      else console.log('PASS '+file.path+' script '+i);
    }
    if(file.path.endsWith('render-pipeline.html')){
      for(const token of ['hfx-shot-plan','orbit360','captureStream','Export shot plan JSON']) if(!html.includes(token)){console.error('FAIL '+file.path+': missing '+token);failed=true}
    }
    if(file.path.endsWith('production-intelligence.html')){
      for(const token of [\"format:'hfx-shot-plan'\",'function evaluate','hfx-production-brief.md']) if(!html.includes(token)){console.error('FAIL '+file.path+': missing '+token);failed=true}
    }
    if(file.path.endsWith('hfx-hyperframes-exporter.html')){
      for(const token of ['data-composition-id="main"','window.__timelines.main','GLTFLoader','hfx-shot-plan']) if(!html.includes(token)){console.error('FAIL '+file.path+': missing '+token);failed=true}
    }
  }
} finally { await rm(dir,{recursive:true,force:true}); }
if(failed) process.exit(1);
console.log('HFX browser studio checks passed.');
