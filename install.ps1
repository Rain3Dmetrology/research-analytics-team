# ResearchTeam annex installer and read-only startup preflight.
param([switch]$Check)
$ErrorActionPreference = 'Stop'
$Src = Split-Path -Parent $MyInvocation.MyCommand.Path
$Python = Get-Command python -ErrorAction SilentlyContinue
if (-not $Python) { Write-Host 'FAIL: Python is required for compatibility verification.'; exit 1 }
$Gate = Join-Path $Src 'scripts\compatibility_check.py'
$Targets = @('.claude','.codex','.trae','.trae-cn','.qoder','.workbuddy')
$blocked = $false; $installed = 0
foreach ($name in $Targets) {
    $base = Join-Path $env:USERPROFILE "$name\skills"
    if (-not (Test-Path $base)) { continue }
    $dmr = Join-Path $base 'deep-market-research'
    $dest = Join-Path $base 'research-orchestrator'
    $annex = Join-Path $dest 'SKILL.md'
    if ($Check -and -not (Test-Path $annex)) { Write-Host "WARN: $name annex not installed"; continue }
    if ($Check) {
        & $Python.Source -B $Gate --dmr $dmr --annex $annex
        if ($LASTEXITCODE -ne 0) { $blocked = $true }
    } else {
        & $Python.Source -B $Gate --dmr $dmr
        if ($LASTEXITCODE -ne 0) { $blocked = $true; continue }
        New-Item -ItemType Directory -Force -Path $dest | Out-Null
        Copy-Item -Force (Join-Path $Src 'portable\SKILL.md') $annex
        & $Python.Source -B $Gate --dmr $dmr --annex $annex
        if ($LASTEXITCODE -ne 0) { $blocked = $true; continue }
        $installed++
    }
}
if ($Check) {
    $team = Join-Path $env:USERPROFILE '.workbuddy\plugins\marketplaces\my-experts\plugins\research-analytics-team'
    $dmr = Join-Path $env:USERPROFILE '.workbuddy\skills\deep-market-research'
    & $Python.Source -B $Gate --dmr $dmr --package $team
    if ($LASTEXITCODE -ne 0) { $blocked = $true }
} elseif ($installed -eq 0) { $blocked = $true }
if ($blocked) { Write-Host 'RESULT: FAIL - fix incompatible or drifted artifacts before launch.'; exit 1 }
Write-Host 'RESULT: PASS - verified artifacts; start a fresh session.'
exit 0
