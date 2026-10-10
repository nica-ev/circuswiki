param(
    # Configured language code to stage and preview.
    [string]$Language = "de",

    # Address to bind the Zensical development server to.
    [string]$HostAddress = "127.0.0.1",

    # Local port for the preview server.
    [int]$Port = 8000
)

$ErrorActionPreference = "Stop"

$Root = Resolve-Path (Join-Path $PSScriptRoot "..")
$LanguageRegistry = Join-Path $Root "tools\config\languages.json"
$VenvPython = Join-Path $Root ".venv\Scripts\python.exe"
$VenvZensical = Join-Path $Root ".venv\Scripts\zensical.exe"

if (-not (Test-Path -LiteralPath $VenvPython) -or -not (Test-Path -LiteralPath $VenvZensical)) {
    throw "The repository .venv is missing or incomplete. Create it and run '.\.venv\Scripts\python.exe -m pip install -r requirements.txt'."
}

$Registry = Get-Content -LiteralPath $LanguageRegistry -Raw | ConvertFrom-Json
$LanguageEntry = @($Registry.languages) | Where-Object { $_.code -eq $Language } | Select-Object -First 1
if (-not $LanguageEntry) {
    $Available = (@($Registry.languages) | ForEach-Object { $_.code }) -join ", "
    throw "Unknown language '$Language'. Configured languages: $Available"
}

$Listener = Get-NetTCPConnection -State Listen -LocalPort $Port -ErrorAction SilentlyContinue | Select-Object -First 1
if ($Listener) {
    $Owner = Get-Process -Id $Listener.OwningProcess -ErrorAction SilentlyContinue
    $OwnerLabel = if ($Owner) { "$($Owner.ProcessName) (PID $($Owner.Id))" } else { "PID $($Listener.OwningProcess)" }
    throw "Port $Port is already used by $OwnerLabel. Stop that server or run this command with -Port <another-port>."
}

$ConfigPath = Join-Path $Root $LanguageEntry.zensical
$BasePath = if ($env:CIRCUSWIKI_SITE_BASE_PATH) { $env:CIRCUSWIKI_SITE_BASE_PATH.Trim() } else { "/circuswiki/" }
if (-not $BasePath.StartsWith("/")) { $BasePath = "/$BasePath" }
if (-not $BasePath.EndsWith("/")) { $BasePath += "/" }
$LanguagePath = if ($LanguageEntry.root) { $BasePath } else { "$BasePath$Language/" }

Push-Location $Root
try {
    $ZensicalVersion = & $VenvZensical --version
    if ($LASTEXITCODE -ne 0) {
        throw "Unable to run Zensical from the repository .venv."
    }
    Write-Host "Using Zensical $ZensicalVersion from .venv"

    Write-Host "Staging only language '$Language'..."
    & $VenvPython tools/stage_multilang.py --language $Language
    if ($LASTEXITCODE -ne 0) {
        throw "Single-language staging failed with exit code $LASTEXITCODE."
    }

    Write-Host "Starting the '$Language' preview at http://${HostAddress}:$Port$LanguagePath"
    Write-Host "This preview does not verify language switching or multilingual post-build behavior."
    Write-Host "Press Ctrl+C to stop."
    & $VenvZensical serve -f $ConfigPath --dev-addr "${HostAddress}:$Port"
    if ($LASTEXITCODE -ne 0) {
        throw "Zensical exited with code $LASTEXITCODE."
    }
}
finally {
    Pop-Location
}
