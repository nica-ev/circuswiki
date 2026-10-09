$ErrorActionPreference = "Stop"

$Root = Resolve-Path (Join-Path $PSScriptRoot "..")
$Site = Join-Path $Root "site"
$LanguageRegistry = Join-Path $Root "tools\config\languages.json"
$VenvPython = Join-Path $Root ".venv\Scripts\python.exe"
$VenvZensical = Join-Path $Root ".venv\Scripts\zensical.exe"
$PythonCommand = if (Test-Path -LiteralPath $VenvPython) { $VenvPython } else { "python" }
$ZensicalCommand = if (Test-Path -LiteralPath $VenvZensical) { $VenvZensical } else { "zensical" }

Push-Location $Root
try {
    $Languages = (Get-Content -LiteralPath $LanguageRegistry -Raw | ConvertFrom-Json).languages
    $ZensicalVersion = & $ZensicalCommand --version
    if ($LASTEXITCODE -ne 0) {
        throw "Unable to run Zensical from '$ZensicalCommand'."
    }
    Write-Host "Using Zensical $ZensicalVersion"

    Write-Host "== Staging multilingual content =="
    & $PythonCommand tools/stage_multilang.py
    if ($LASTEXITCODE -ne 0) {
        throw "Multilingual staging failed with exit code $LASTEXITCODE."
    }

    Write-Host "== Configuring site URLs =="
    & $PythonCommand tools/configure_site_base.py
    if ($LASTEXITCODE -ne 0) {
        throw "Site URL configuration failed with exit code $LASTEXITCODE."
    }

    if (Test-Path $Site) {
        Write-Host "== Removing previous site output =="
        Remove-Item -LiteralPath $Site -Recurse -Force
    }

    for ($Index = 0; $Index -lt $Languages.Count; $Index++) {
        $Language = $Languages[$Index]
        $ConfigPath = Join-Path $Root ".zensical-build.$($Language.zensical)"
        Write-Host "== Building language $($Language.code) ($($Index + 1)/$($Languages.Count)) =="
        & $ZensicalCommand build -f $ConfigPath
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

    Write-Host "== Augmenting multilingual sitemaps =="
    & $PythonCommand tools/augment_sitemaps.py
    if ($LASTEXITCODE -ne 0) {
        throw "Sitemap augmentation failed with exit code $LASTEXITCODE."
    }
    Write-Host "== Multilingual build complete =="
}
finally {
    Pop-Location
}
