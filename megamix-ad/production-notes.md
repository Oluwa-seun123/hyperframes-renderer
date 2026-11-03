# Megamix — production notes

## Creative direction
“A little goodness in every moment.” A sensory, premium-feeling live-action yoghurt spot: macro yoghurt texture, fruit as an optional serving suggestion, genuine breakfast preparation, then accurate Megamix packaging and logo. 60 seconds, 9:16, 1080×1920, 30fps, silent master.

## Pipeline
1. OpenMontage hybrid/atelier direction: creative brief → script/scene plan → licensed asset sourcing → edit decisions → HyperFrames composition → render QA → ZIP delivery.
2. GitHub Actions acquires candidate Mixkit Free-License clips and records their source and licence.
3. HyperFrames runs check, snapshots, render; FFprobe validates the final master.
4. The workflow packages the render, snapshots, assets and licence manifest into a ZIP artifact.

## Brand accuracy gate
The runner must receive the actual owner-approved Megamix assets at:
- assets/megamix-range.jpg
- assets/megamix-greek.jpg
- assets/megamix-logo.jpg

These are deliberately not fabricated or committed to this public repository. Do not publish packaging images to this public repo. Until a private asset handoff is configured, the workflow stops before render rather than generating counterfeit labels or a misleading product shot.

## Claims and footage
No unverified nutritional/health claims, ingredient claims, price, availability or endorsement. Stock people are not presented as Megamix endorsers. Only use stock items confirmed as Mixkit Free License, not Restricted License.