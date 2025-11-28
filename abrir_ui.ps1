# Launcher de PowerShell con mejor presentación
$Host.UI.RawUI.WindowTitle = "Auto-Commit GitHub - Launcher"

Write-Host ""
Write-Host "╔═══════════════════════════════════════════════════════╗" -ForegroundColor Cyan
Write-Host "║                                                       ║" -ForegroundColor Cyan
Write-Host "║         🤖 AUTO-COMMIT GITHUB - INTERFAZ GUI          ║" -ForegroundColor Cyan -NoNewline
Write-Host "           ║" -ForegroundColor Cyan
Write-Host "║                                                       ║" -ForegroundColor Cyan
Write-Host "╚═══════════════════════════════════════════════════════╝" -ForegroundColor Cyan
Write-Host ""
Write-Host "  Iniciando aplicación..." -ForegroundColor Yellow
Write-Host ""

# Navegar al directorio del script
$scriptPath = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $scriptPath

# Verificar Python
try {
    $pythonVersion = python --version 2>&1
    Write-Host "  ✅ Python detectado: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "  ❌ Python no encontrado" -ForegroundColor Red
    Write-Host ""
    Write-Host "  Por favor instala Python desde: https://www.python.org/downloads/" -ForegroundColor Yellow
    Write-Host ""
    pause
    exit 1
}

Write-Host ""
Write-Host "  🚀 Abriendo interfaz gráfica..." -ForegroundColor Cyan
Write-Host ""

# Ejecutar UI
try {
    python ui_autocommit.py
} catch {
    Write-Host ""
    Write-Host "  ❌ Error al iniciar la aplicación" -ForegroundColor Red
    Write-Host "  $_" -ForegroundColor Red
    Write-Host ""
    pause
}
