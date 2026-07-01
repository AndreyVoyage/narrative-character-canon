param(
    [Parameter(Mandatory = $true)]
    [string]$Characters,

    [Parameter(Mandatory = $true)]
    [string]$Scene,

    [Parameter(Mandatory = $true)]
    [string]$Description,

    [string]$RepoRoot = "C:\DEV\Narrative\narrative-character-canon",

    [string]$OutputRoot = "C:\DEV\Narrative\LOCAL_STORAGE\narrative-character-canon\scene_packs"
)

$ErrorActionPreference = "Stop"

$python = Get-Command python -ErrorAction SilentlyContinue
if (-not $python) {
    $python = Get-Command py -ErrorAction SilentlyContinue
}
if (-not $python) {
    throw "Python was not found in PATH. Install Python or make the 'python'/'py' launcher available."
}

$scriptPath = Join-Path $RepoRoot "tools\build_scene_reference_pack.py"
if (-not (Test-Path -LiteralPath $scriptPath)) {
    throw "Scene reference pack script not found: $scriptPath"
}

& $python.Source $scriptPath `
    --characters $Characters `
    --scene $Scene `
    --description $Description `
    --repo-root $RepoRoot `
    --output-root $OutputRoot

exit $LASTEXITCODE
