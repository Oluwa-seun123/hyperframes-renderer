# Phase 12 — HFX Production Desk

The phone-first `studio-dashboard.html` is a lightweight project and delivery dashboard for the existing browser studios.

## What it provides

- Local project register: product/project name, output format, campaign objective and production stage.
- Project register JSON export for backup or transfer.
- Production route links to Production Intelligence, 3D Engine, Sequencer, HyperFrames Exporter and Audio Studio.
- Render workflow, pull request and repository shortcuts.
- Render/delivery instructions for GitHub Actions artifacts.
- A local pre-render checklist.

## Open on Android

Open `studio-dashboard.html` from the repository in a browser, or publish the `image-motion-studio` folder as a static site. It uses no build step and no paid API. Project notes are stored in that browser's local storage; use Export project list to back them up.

## Security and operational boundaries

- The dashboard does not contain a GitHub token and does not attempt to dispatch a workflow from unauthenticated browser JavaScript.
- The Run workflow button opens GitHub Actions. Sign in to GitHub, select the branch, and use GitHub's own Run workflow control.
- Download the ZIP from the completed run's Artifacts section. Current workflow retention is 7 days.
- Project register and checklist are local browser data, not synced to GitHub and not shared across devices.
- This is project tracking and navigation, not an authenticated remote-control backend. It does not claim to list live runs or fetch artifact files automatically.

## Phase 12 limits

This dashboard does not replace the actual render pipeline, verify the artistic quality of a video, upload user assets, or provide permanent cloud storage. GitHub Actions remains the cloud render host; the workflow's completed run and artifact are the source of truth for delivery.
