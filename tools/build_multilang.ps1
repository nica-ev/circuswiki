$ErrorActionPreference = "Stop"

$Root = Resolve-Path (Join-Path $PSScriptRoot "..")
$Site = Join-Path $Root "site"
$LanguageRegistry = Join-Path $Root "tools\config\languages.json"

Push-Location $Root
try {
    $Languages = (Get-Content -LiteralPath $LanguageRegistry -Raw | ConvertFrom-Json).languages

    python tools/stage_multilang.py
    python tools/configure_site_base.py

    if (Test-Path $Site) {
        Remove-Item -LiteralPath $Site -Recurse -Force
    }

    foreach ($Language in $Languages) {
        $ConfigPath = Join-Path $Root ".zensical-build.$($Language.zensical)"
        zensical build -f $ConfigPath
        if ($LASTEXITCODE -ne 0) {
            throw "Zensical build failed for language '$($Language.code)' with exit code $LASTEXITCODE."
        }
        if ($Language.root) {
            $ExpectedIndex = Join-Path $Site "index.html"
        }
        else {
            $ExpectedIndex = Join-Path (Join-Path $Site $Language.code) "index.html"
        }
        if (-not (Test-Path -LiteralPath $ExpectedIndex)) {
            throw "Zensical build did not create expected index for language '$($Language.code)': $ExpectedIndex"
        }
    }

    python tools/augment_sitemaps.py
}
finally {
    Pop-Location
}
