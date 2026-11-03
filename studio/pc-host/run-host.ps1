$ErrorActionPreference="Stop"
$Here=Split-Path -Parent $MyInvocation.MyCommand.Path; $Repo=(Resolve-Path (Join-Path $Here "..\..")).Path
$EnvFile=Join-Path $Here ".env.ps1"; if (-not (Test-Path $EnvFile)) { throw "Run setup-windows.ps1 first." }
. $EnvFile
if (-not (Get-Command python -ErrorAction SilentlyContinue)) { throw "Python missing; restart PowerShell after setup." }
Set-Location $Repo; python (Join-Path $Here "host.py")
