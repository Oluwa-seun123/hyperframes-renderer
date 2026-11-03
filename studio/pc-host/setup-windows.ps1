$ErrorActionPreference = "Stop"
$Repo="https://github.com/Oluwa-seun123/hyperframes-renderer.git"; $Branch="studio-toolchain-integration"
$Install=Join-Path $env:USERPROFILE "ASO-Production"; $Data=Join-Path $env:USERPROFILE "ASO-Studio-Data"
if (-not (Get-Command winget -ErrorAction SilentlyContinue)) { throw "Install/update App Installer (winget), then rerun." }
foreach ($id in @("Git.Git","Python.Python.3.12","OpenJS.NodeJS.LTS","Gyan.FFmpeg","Tailscale.Tailscale")) { winget install --id $id --exact --silent --accept-package-agreements --accept-source-agreements; if ($LASTEXITCODE -ne 0) { throw "Install failed: $id" } }
if (-not (Test-Path (Join-Path $Install ".git"))) { git clone --branch $Branch --single-branch $Repo $Install } else { git -C $Install fetch origin; git -C $Install checkout $Branch; git -C $Install pull --ff-only origin $Branch }
New-Item -ItemType Directory -Force -Path (Join-Path $Data "inbox") | Out-Null
$Cred=Join-Path $Install "studio\pc-host\.env.ps1"
if (-not (Test-Path $Cred)) {
 $bytes=New-Object byte[] 32; [Security.Cryptography.RandomNumberGenerator]::Fill($bytes)
 $pw=[Convert]::ToBase64String($bytes).TrimEnd('=').Replace('+','A').Replace('/','B')
 $lines=@('$env:ASO_USER = "aso"','$env:ASO_PASSWORD = "'+$pw+'"','$env:ASO_DATA_DIR = "'+$Data+'"','$env:ASO_PORT = "8765"')
 $lines | Set-Content -Encoding ASCII $Cred
 Write-Host "Generated password in $Cred. Share it privately with the studio owner."
}
Write-Host "Setup prepared. Restart PowerShell after installers finish."
Write-Host "Sign into Tailscale on this PC and the owner's Android device."
Write-Host "Then run run-host.ps1 and in another terminal: tailscale serve --bg 8765"
Write-Host "Do not enable Funnel or router port forwarding."
