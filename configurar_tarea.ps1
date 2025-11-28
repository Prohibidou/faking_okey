# Script de Configuración Automática del Programador de Tareas
# Ejecutar como Administrador

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  Configurador de Auto-Commit GitHub  " -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Verificar si se está ejecutando como administrador
$isAdmin = ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)

if (-not $isAdmin) {
    Write-Host "❌ Este script necesita ejecutarse como Administrador" -ForegroundColor Red
    Write-Host ""
    Write-Host "Por favor:" -ForegroundColor Yellow
    Write-Host "1. Cierra esta ventana" -ForegroundColor Yellow
    Write-Host "2. Click derecho en PowerShell" -ForegroundColor Yellow
    Write-Host "3. Selecciona 'Ejecutar como administrador'" -ForegroundColor Yellow
    Write-Host "4. Ejecuta este script nuevamente" -ForegroundColor Yellow
    Write-Host ""
    pause
    exit 1
}

Write-Host "✅ Ejecutando como Administrador" -ForegroundColor Green
Write-Host ""

# Configuración
$projectPath = "C:\Users\veram\OneDrive\Documentos\projects\faking_okey"
$scriptPath = Join-Path $projectPath "run_auto_commit.ps1"
$taskName = "GitHub Auto Commit - Faking Okey"

# Verificar que el archivo .ps1 existe
if (-not (Test-Path $scriptPath)) {
    Write-Host "❌ No se encuentra el archivo: $scriptPath" -ForegroundColor Red
    pause
    exit 1
}

Write-Host "📁 Proyecto: $projectPath" -ForegroundColor White
Write-Host "📄 Script: $scriptPath" -ForegroundColor White
Write-Host ""

# Preguntar hora de ejecución
Write-Host "⏰ ¿A qué hora quieres que se ejecute diariamente?" -ForegroundColor Yellow
Write-Host "   Formato: HH:MM (ejemplo: 10:00 para las 10 AM)" -ForegroundColor Gray
$hora = Read-Host "   Hora"

# Validar formato
try {
    $horaTime = [DateTime]::ParseExact($hora, "HH:mm", $null)
} catch {
    Write-Host "❌ Formato de hora inválido. Usando 10:00 AM por defecto" -ForegroundColor Red
    $hora = "10:00"
}

Write-Host ""
Write-Host "🔧 Configurando tarea programada..." -ForegroundColor Cyan

# Eliminar tarea si ya existe
$existingTask = Get-ScheduledTask -TaskName $taskName -ErrorAction SilentlyContinue
if ($existingTask) {
    Write-Host "   Eliminando tarea existente..." -ForegroundColor Yellow
    Unregister-ScheduledTask -TaskName $taskName -Confirm:$false
}

try {
    # Crear la acción
    $action = New-ScheduledTaskAction `
        -Execute "PowerShell.exe" `
        -Argument "-ExecutionPolicy Bypass -WindowStyle Hidden -File `"$scriptPath`""

    # Crear el trigger (diariamente)
    $trigger = New-ScheduledTaskTrigger -Daily -At $hora

    # Crear el principal (usuario actual con privilegios altos)
    $principal = New-ScheduledTaskPrincipal `
        -UserId $env:USERNAME `
        -LogonType S4U `
        -RunLevel Highest

    # Configuración adicional
    $settings = New-ScheduledTaskSettingsSet `
        -AllowStartIfOnBatteries `
        -DontStopIfGoingOnBatteries `
        -StartWhenAvailable `
        -ExecutionTimeLimit (New-TimeSpan -Minutes 30)

    # Registrar la tarea
    Register-ScheduledTask `
        -TaskName $taskName `
        -Action $action `
        -Trigger $trigger `
        -Principal $principal `
        -Settings $settings `
        -Description "Hace commits y push automáticos diarios al proyecto faking_okey en GitHub" | Out-Null

    Write-Host ""
    Write-Host "✅ ¡Tarea programada creada exitosamente!" -ForegroundColor Green
    Write-Host ""
    Write-Host "📋 Detalles de la configuración:" -ForegroundColor Cyan
    Write-Host "   • Nombre: $taskName" -ForegroundColor White
    Write-Host "   • Frecuencia: Diaria" -ForegroundColor White
    Write-Host "   • Hora: $hora" -ForegroundColor White
    Write-Host "   • Script: $scriptPath" -ForegroundColor White
    Write-Host ""
    
    # Preguntar si quiere ejecutar ahora
    $ejecutar = Read-Host "¿Deseas ejecutar la tarea ahora para probarla? (S/N)"
    
    if ($ejecutar -eq "S" -or $ejecutar -eq "s") {
        Write-Host ""
        Write-Host "🚀 Ejecutando tarea..." -ForegroundColor Cyan
        Start-ScheduledTask -TaskName $taskName
        Start-Sleep -Seconds 3
        
        # Verificar el estado
        $taskInfo = Get-ScheduledTask -TaskName $taskName | Get-ScheduledTaskInfo
        Write-Host "   Estado: $($taskInfo.LastTaskResult)" -ForegroundColor White
        
        # Mostrar log si existe
        $logPath = Join-Path $projectPath "logs"
        if (Test-Path $logPath) {
            $latestLog = Get-ChildItem $logPath -Filter "*.log" | Sort-Object LastWriteTime -Descending | Select-Object -First 1
            if ($latestLog) {
                Write-Host ""
                Write-Host "📄 Últimas líneas del log:" -ForegroundColor Cyan
                Get-Content $latestLog.FullName -Tail 20 | ForEach-Object {
                    Write-Host "   $_" -ForegroundColor Gray
                }
            }
        }
    }
    
    Write-Host ""
    Write-Host "═══════════════════════════════════════" -ForegroundColor Green
    Write-Host "  ✨ CONFIGURACIÓN COMPLETADA ✨" -ForegroundColor Green
    Write-Host "═══════════════════════════════════════" -ForegroundColor Green
    Write-Host ""
    Write-Host "Próximos pasos:" -ForegroundColor Yellow
    Write-Host "1. Asegúrate de que Git tenga las credenciales guardadas" -ForegroundColor White
    Write-Host "2. Verifica que el repositorio esté configurado en GitHub" -ForegroundColor White
    Write-Host "3. La tarea se ejecutará automáticamente a las $hora todos los días" -ForegroundColor White
    Write-Host ""
    Write-Host "Para ver/gestionar la tarea, abre: Programador de Tareas (taskschd.msc)" -ForegroundColor Gray
    Write-Host ""

} catch {
    Write-Host ""
    Write-Host "❌ Error al crear la tarea programada:" -ForegroundColor Red
    Write-Host $_.Exception.Message -ForegroundColor Red
    Write-Host ""
}

pause
