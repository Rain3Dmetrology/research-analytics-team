# Research Analytics Team - Windows one-click installer (annex form)
# Copies portable/SKILL.md into every detected agent platform's skills/
# directory as `research-orchestrator`, then checks each platform's installed
# dmr copy against the required pin. The WorkBuddy team form is a plugin
# package install (see README) and stays manual.

param([switch]$Check)
$ErrorActionPreference = "Stop"
$Src = Split-Path -Parent $MyInvocation.MyCommand.Path
$AnnexDir = "research-orchestrator"

$Manifest = Get-Content (Join-Path $Src ".codebuddy-plugin\plugin.json") -Raw -Encoding UTF8 | ConvertFrom-Json
$Version = $Manifest.version
$Pin = $Manifest.requires.'deep-market-research'
$PinMin = [version](($Pin -replace '^>=\s*') -replace '\s*<.*$')

# ---------------------------------------------------------------------------
# Startup preflight (-Check, read-only): 启动前核对已落位各平台副本是否 v$Version、
# 契约机制 marker 是否传导、dmr 是否满足 pin，以及 WorkBuddy 团队包是否就绪。
# 关键阻断（团队包缺失/版本漂移/marker 缺失）→ 非零退出；annex 缺 dmr = 警告不阻断。
# ---------------------------------------------------------------------------
if ($Check) {
  $steps = @(); $blocked = $false
  $TeamPkg = "$env:USERPROFILE\.workbuddy\plugins\marketplaces\my-experts\plugins\research-analytics-team"

  Write-Host "== RAT 启动预检 v$Version（dmr pin $Pin）=="

  foreach ($base in ($Targets = @(
    "$env:USERPROFILE\.claude\skills",
    "$env:USERPROFILE\.codex\skills",
    "$env:USERPROFILE\.trae\skills",
    "$env:USERPROFILE\.trae-cn\skills",
    "$env:USERPROFILE\.qoder\skills",
    "$env:USERPROFILE\.workbuddy\skills"
  ))) {
    if (-not (Test-Path $base)) { continue }
    $annex = Join-Path $base (Join-Path $AnnexDir "SKILL.md")
    $dmr = Join-Path $base "deep-market-research\SKILL.md"
    if (-not (Test-Path $annex)) { $steps += ("[{0}] 警告 annex 未落位（路由附件，不影响团队包主路径）" -f $base); continue }
    if (-not (Test-Path $dmr)) {
      $steps += ("[{0}] annex ✓ 但 dmr 未装（annex 休眠，需装 dmr {1}）" -f $base, $Pin)   # 警告
    } else {
      $dv = (Select-String -Path $dmr -Pattern '^version:\s*"?([\d.]+)"?' | Select-Object -First 1).Matches.Groups[1].Value
      if ([version]$dv -lt $PinMin) { $steps += ("[{0}] 警告 dmr v{1} < pin {2}" -f $base, $dv, $PinMin) }
      else { $steps += ("[{0}] annex ✓ dmr v{1} ✓（满足 {2}）" -f $base, $dv, $Pin) }
    }
  }

  # WorkBuddy 团队包：版本 + 4 枚契约机制 marker（关键阻断）
  if (Test-Path $TeamPkg) {
    $tpVer = (Get-Content (Join-Path $TeamPkg ".codebuddy-plugin\plugin.json") -Raw -Encoding UTF8 | ConvertFrom-Json).version
    if ($tpVer -ne $Version) { $steps += "WorkBuddy 团队包版本 $tpVer ≠ 源 $Version —— 需重新同步"; $blocked = $true }
    else { $steps += "WorkBuddy 团队包 v$tpVer ✓（与源一致）" }
    $checks = @{
      "SOP 五态任务板"   = "agents\research-analytics-team-team-lead.md";
      "contract TRAE 列" = "orchestration\contract.md";
      "contract 同模降级" = "orchestration\contract.md";
      "portable 止损"    = "portable\SKILL.md"
    }
    $pat = @{ "SOP 五态任务板" = "五态"; "contract TRAE 列" = "TRAE（TraeWork"; "contract 同模降级" = "降级"; "portable 止损" = "重复动作止损" }
    foreach ($k in $checks.Keys) {
      $ok = Select-String -Path (Join-Path $TeamPkg $checks[$k]) -Pattern $pat[$k] -SimpleMatch -Quiet
      if ($ok) { $steps += "$k ✓" } else { $steps += "$k ✗ 缺失——团队包为旧版快照"; $blocked = $true }
    }
    $steps += "启动动作：请对下次 RAT 会话用 TeamCreate 新建团队（勿复用旧会话）以吃到 v$Version 心智——SOP/契约均自团队包实时解析"
  } else {
    $steps += "WorkBuddy 团队包未就绪：$TeamPkg —— 请按 README 复制仓库根目录到该路径"; $blocked = $true
  }

  $steps | ForEach-Object { Write-Host "  $_" }
  if ($blocked) { Write-Host "RESULT: FAIL —— 修复上列 ✗ 项后再启动。"; exit 1 }
  Write-Host "RESULT: PASS —— 可直接启动（记得 TeamCreate 新建、勿复用旧会话）。"
  exit 0
}
# ---------------------------------------------------------------------------

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
