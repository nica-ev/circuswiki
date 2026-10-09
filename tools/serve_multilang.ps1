param(
    # Address to bind the preview server to. Use 0.0.0.0 for local-network testing.
    [string]$HostAddress = "127.0.0.1",

    # Local port for the preview server.
    [int]$Port = 8000,

    # Skip rebuilding and serve the existing site/ output.
    [switch]$NoBuild
)

$ErrorActionPreference = "Stop"

$Root = Resolve-Path (Join-Path $PSScriptRoot "..")
$SiteIndex = Join-Path $Root "site\index.html"
$VenvPython = Join-Path $Root ".venv\Scripts\python.exe"
$PythonCommand = if (Test-Path -LiteralPath $VenvPython) { $VenvPython } else { "python" }
Push-Location $Root
try {
    if (-not $NoBuild) {
        Write-Host "Building the multilingual site before starting the server."
        Write-Host "This processes all configured languages and can take several minutes."
        Write-Host "Use -NoBuild to serve an existing site/ directory immediately."
        & (Join-Path $PSScriptRoot "build_multilang.ps1")
    }
    elseif (-not (Test-Path -LiteralPath $SiteIndex)) {
        throw "Cannot use -NoBuild because site/index.html does not exist. Run without -NoBuild once to create it."
    }

    Write-Host "Starting preview server at http://${HostAddress}:$Port/circuswiki/"
    Write-Host "Press Ctrl+C to stop."
    & $PythonCommand tools/serve_multilang_site.py --host $HostAddress --port $Port
}
finally {
    Pop-Location
}
