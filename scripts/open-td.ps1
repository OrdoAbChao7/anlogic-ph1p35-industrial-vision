param([switch]$ClockFix)

$repoRoot = Split-Path -Parent $PSScriptRoot
$tdExe = Join-Path $repoRoot '.tools\td\app\bin\td.exe'
$workName = if ($ClockFix) { 'lab_ex1_mipi_hdmi_sc520_clockfix' } else { 'lab_ex1_mipi_hdmi_sc520' }
$project = Join-Path $repoRoot ".tools\td\work\$workName\td_project\camera_to_dsi_display.al"

if (-not (Test-Path -LiteralPath $tdExe)) {
    throw "TangDynasty 6.2.1 is missing: $tdExe"
}

if (-not (Test-Path -LiteralPath $project)) {
    throw "Baseline project is missing: $project"
}

Start-Process -FilePath $tdExe -ArgumentList ('"' + $project + '"') -WorkingDirectory (Split-Path -Parent $tdExe)
