# Research Analytics Team - Windows one-click installer (annex form)
# Copies portable/SKILL.md into every detected agent platform's skills/
# directory as `research-orchestrator`, then checks each platform's installed
# dmr copy against the required pin. The WorkBuddy team form is a plugin
# package install (see README) and stays manual.

$ErrorActionPreference = "Stop"
$Src = Split-Path -Parent $MyInvocation.MyCommand.Path
$AnnexDir = "research-orchestrator"

$Manifest = Get-Content (Join-Path $Src ".codebuddy-plugin\plugin.json") -Raw -Encoding UTF8 | ConvertFrom-Json
$Version = $Manifest.version
$Pin = $Manifest.requires.'deep-market-research'
$PinMin = [version](($Pin -replace '^>=\s*') -replace '\s*<.*$')
Write-Host "Installing research-analytics-team annex v$Version (dmr pin $Pin)"

$Targets = @(
  "$env:USERPROFILE\.claude\skills",
  "$env:USERPROFILE\.codex\skills",
  "$env:USERPROFILE\.trae\skills",
  "$env:USERPROFILE\.trae-cn\skills",
  "$env:USERPROFILE\.qoder\skills",
  "$env:USERPROFILE\.workbuddy\skills"
)

$installed = 0
foreach ($base in $Targets) {
  if (Test-Path $base) {
    $dest = Join-Path $base $AnnexDir
    New-Item -ItemType Directory -Force -Path $dest | Out-Null
    Copy-Item -Force (Join-Path $Src "portable\SKILL.md") $dest
    $dmrSkill = Join-Path $base "deep-market-research\SKILL.md"
    if (Test-Path $dmrSkill) {
      $dmrV = (Select-String -Path $dmrSkill -Pattern '^version:\s*"?([\d.]+)"?' | Select-Object -First 1).Matches.Groups[1].Value
      if ([version]$dmrV -lt $PinMin) {
        Write-Warning "[$base] dmr v$dmrV < pin minimum $PinMin — run deep-market-research install.ps1 first"
      } else {
        Write-Host "[$base] annex v$Version installed (dmr v$dmrV satisfies $Pin)"
      }
    } else {
      Write-Warning "[$base] dmr not installed — annex stays dormant until dmr (pin $Pin) is present"
    }
    $installed++
  }
}

if ($installed -eq 0) {
  Write-Host "No supported agent skills directory found. Copy portable/SKILL.md into your platform's skills/research-orchestrator/ manually."
  exit 1
}
Write-Host "Done. WorkBuddy team form: copy the repo root into ~/.workbuddy/plugins/marketplaces/my-experts/plugins/research-analytics-team/ (see README)."
