# Script de Prueba Rápida
# No requiere permisos de administrador

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "     Prueba del Sistema Auto-Commit    " -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

$projectPath = "C:\Users\veram\OneDrive\Documentos\projects\faking_okey"
Set-Location $projectPath

Write-Host "📁 Directorio: $projectPath" -ForegroundColor White
Write-Host ""

# Verificar Python
Write-Host "🔍 Verificando Python..." -ForegroundColor Yellow
try {
    $pythonVersion = python --version 2>&1
    Write-Host "   ✅ $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "   ❌ Python no encontrado" -ForegroundColor Red
    Write-Host "   Instala Python desde: https://www.python.org/downloads/" -ForegroundColor Yellow
    pause
    exit 1
}

# Verificar Git
Write-Host "🔍 Verificando Git..." -ForegroundColor Yellow
try {
    $gitVersion = git --version 2>&1
    Write-Host "   ✅ $gitVersion" -ForegroundColor Green
} catch {
    Write-Host "   ❌ Git no encontrado" -ForegroundColor Red
    Write-Host "   Instala Git desde: https://git-scm.com/download/win" -ForegroundColor Yellow
    pause
    exit 1
}

# Verificar repositorio Git
Write-Host "🔍 Verificando repositorio Git..." -ForegroundColor Yellow
if (Test-Path ".git") {
    Write-Host "   ✅ Repositorio Git inicializado" -ForegroundColor Green
    
    # Verificar remote
    $remote = git remote -v 2>&1
    if ($remote -match "origin") {
        Write-Host "   ✅ Remote 'origin' configurado" -ForegroundColor Green
        Write-Host "      $($remote -split "`n" | Select-Object -First 1)" -ForegroundColor Gray
    } else {
        Write-Host "   ⚠️  No hay remote 'origin' configurado" -ForegroundColor Yellow
        Write-Host "   Ejecuta: git remote add origin <URL_DE_TU_REPO>" -ForegroundColor Gray
    }
} else {
    Write-Host "   ⚠️  No es un repositorio Git" -ForegroundColor Yellow
    Write-Host "   Ejecuta: git init" -ForegroundColor Gray
}

Write-Host ""
Write-Host "🚀 Ejecutando prueba del script..." -ForegroundColor Cyan
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Gray

# Ejecutar el script
python auto_commit.py

Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Gray
Write-Host ""

# Verificar resultados
Write-Host "📊 Verificando resultados..." -ForegroundColor Cyan
Write-Host ""

# Ver commits recientes
Write-Host "📝 Últimos commits:" -ForegroundColor Yellow
git log --oneline -5 2>$null
Write-Host ""

# Ver estado
Write-Host "📋 Estado del repositorio:" -ForegroundColor Yellow
git status
Write-Host ""

# Verificar logs
$logFolder = "logs"
if (Test-Path $logFolder) {
    $latestLog = Get-ChildItem $logFolder -Filter "*.log" | Sort-Object LastWriteTime -Descending | Select-Object -First 1
    if ($latestLog) {
        Write-Host "📄 Archivo de log creado: $($latestLog.Name)" -ForegroundColor Green
        Write-Host "   Ruta: $($latestLog.FullName)" -ForegroundColor Gray
    }
}

Write-Host ""
Write-Host "═══════════════════════════════════════" -ForegroundColor Green
Write-Host "        ✅ PRUEBA COMPLETADA" -ForegroundColor Green
Write-Host "═══════════════════════════════════════" -ForegroundColor Green
Write-Host ""
Write-Host "Si todo funcionó correctamente:" -ForegroundColor Yellow
Write-Host "1. El README.md debe estar actualizado" -ForegroundColor White
Write-Host "2. Deben haberse creado varios commits" -ForegroundColor White
Write-Host "3. Los commits deben estar en GitHub (si hiciste push)" -ForegroundColor White
Write-Host ""
Write-Host "Siguiente paso: Configura la tarea programada con:" -ForegroundColor Cyan
Write-Host ".\configurar_tarea.ps1" -ForegroundColor White
Write-Host "(Requiere ejecutarse como Administrador)" -ForegroundColor Gray
Write-Host ""

pause
