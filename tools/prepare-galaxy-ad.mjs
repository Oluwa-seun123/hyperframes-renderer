import { access, copyFile, mkdir, readFile, writeFile } from 'node:fs/promises';
import { execFileSync } from 'node:child_process';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const project = path.join(root, 'image-motion-studio', 'project');
const production = path.join(project, 'production', 'galaxy-s26-ultra');
const sourceHtml = path.join(production, 'index.html');
const sourceModel = path.join(production, 'assets', 'galaxy-s26-ultra.glb');
const sourceArchive = path.join(production, 'assets', 'galaxy-s26-ultra.glb.zip');
const outputModelDir = path.join(project, 'assets');
const outputModel = path.join(outputModelDir, 'galaxy-s26-ultra.glb');

for (const file of [sourceHtml]) {
  try { await access(file); }
  catch {
    console.error('GALAXY BUILD BLOCKED: required production input is missing:');
    console.error('  ' + path.relative(root, file));
    console.error('Place the supplied Samsung GLB at image-motion-studio/project/production/galaxy-s26-ultra/assets/galaxy-s26-ultra.glb, then rerun this workflow.');
    process.exit(2);
  }
}
const composition = await readFile(sourceHtml, 'utf8');
const requiredTokens = [
  'GLTFLoader', 'gsap.timeline({paused:true})', 'window.__timelines.main',
  'product.rotation', 'Math.sin(state.orbit)', 'DirectionalLight', 'id="opening"', 'id="camera-copy"',
  'id="display-copy"', 'id="final-copy"', 'data-duration="30"',
  "./assets/galaxy-s26-ultra.glb"
];
const missingTokens = requiredTokens.filter(token => !composition.includes(token));
if (missingTokens.length) {
  console.error('GALAXY BUILD BLOCKED: composition is missing required 3D/motion-graphics features: ' + missingTokens.join(', '));
  process.exit(2);
}
let modelPath = sourceModel;
try { await access(sourceModel); }
catch {
  try {
    await access(sourceArchive);
    const entries = execFileSync('unzip', ['-Z1', sourceArchive], { encoding: 'utf8' })
      .split(/\r?\n/).filter(name => name.toLowerCase().endsWith('.glb'));
    if (entries.length !== 1) {
      console.error(`GALAXY BUILD BLOCKED: expected exactly one GLB in uploaded ZIP; found ${entries.length}.`);
      process.exit(2);
    }
    const extracted = execFileSync('unzip', ['-p', sourceArchive, entries[0]], { maxBuffer: 128 * 1024 * 1024 });
    await writeFile(sourceModel, extracted);
    console.log(`Extracted GLB from uploaded archive: ${entries[0]}`);
  } catch (error) {
    console.error('GALAXY BUILD BLOCKED: upload galaxy-s26-ultra.glb or galaxy-s26-ultra.glb.zip into the production assets folder.');
    console.error(error.message);
    process.exit(2);
  }
}
const bytes = await readFile(modelPath);
if (bytes.length < 20 || bytes.toString('ascii', 0, 4) !== 'glTF') {
  console.error('GALAXY BUILD BLOCKED: the supplied model is not a valid GLB 2.0 file.');
  process.exit(2);
}
const version = bytes.readUInt32LE(4);
const declaredLength = bytes.readUInt32LE(8);
if (version !== 2 || declaredLength !== bytes.length) {
  console.error(`GALAXY BUILD BLOCKED: invalid GLB header (version=${version}, declared=${declaredLength}, actual=${bytes.length}).`);
  process.exit(2);
}
await mkdir(outputModelDir, { recursive: true });
await copyFile(sourceModel, outputModel);
await copyFile(sourceHtml, path.join(project, 'index.html'));
console.log(`Galaxy composition prepared: ${(bytes.length / 1048576).toFixed(2)} MiB GLB, valid GLB 2.0.`);
console.log('HyperFrames will render the real model and GSAP motion-graphics composition.');
