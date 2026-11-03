# ASO Studio private PC host (Windows)

This prepares a friend's Windows PC to host a private mobile dashboard. The server binds to 127.0.0.1; Tailscale Serve provides private HTTPS. Never use router port forwarding or Tailscale Funnel.

## Included
- Authenticated dashboard and PC/inbox status.
- Uploads into a separate ASO-Studio-Data/inbox folder.
- Random password generated locally; 2 GB default upload cap.
- Python standard library only; no paid API.

## Not connected yet
This does not execute OpenMontage, control VoiceStudio, automatically import files, queue jobs or run HyperFrames renders. It is a secure remote transfer/dashboard foundation, not yet a render farm. The PC must remain powered on and online. Rendering and local AI inference can slow other work; schedule heavy jobs for idle periods.

## Friend's setup
1. Ensure Windows 10/11 has App Installer/winget.
2. Clone this branch:
   git clone --branch studio-toolchain-integration --single-branch https://github.com/Oluwa-seun123/hyperframes-renderer.git "$HOME\ASO-Production"
3. Open PowerShell in ASO-Production\studio\pc-host and run:
   powershell -ExecutionPolicy Bypass -File .\setup-windows.ps1
4. Restart PowerShell after installs finish.
5. Sign into Tailscale on the PC. Install Tailscale on the owner's Android phone and join the same private tailnet; each person uses their own account.
6. Run .\run-host.ps1 and keep the terminal open.
7. In a second PowerShell window run: tailscale serve --bg 8765
8. Tailscale displays a private HTTPS URL. Send it and the generated password to the owner privately. Username: aso.
9. On Android, connect Tailscale, open the URL in Chrome and sign in.

If Serve is not enabled, follow the Tailscale admin prompt. Do not enable Funnel.

## Updates and privacy
Update from the repo folder with git pull --ff-only origin studio-toolchain-integration, then restart the host. The local .env.ps1 password file must never be committed. Uploaded files live under %USERPROFILE%\ASO-Studio-Data\inbox; agree retention with the PC owner. Consider a separate Windows user account for stronger isolation. Do not upload secrets or media without permission.
