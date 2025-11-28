# Script de PowerShell para ejecutar auto_commit.py
# Este script se ejecutará desde el Programador de Tareas de Windows

# Navegar al directorio del proyecto
Set-Location "C:\Users\veram\OneDrive\Documentos\projects\faking_okey"

# Crear carpeta de logs si no existe
$logFolder = "logs"
if (-not (Test-Path $logFolder)) {
    New-Item -ItemType Directory -Path $logFolder | Out-Null
}

# Obtener la fecha actual para el nombre del log
$fecha = Get-Date -Format "yyyy-MM-dd"
$hora = Get-Date -Format "HH-mm-ss"
$logFile = Join-Path $logFolder "auto_commit_$fecha.log"

# Escribir header en el log
Write-Output "`n========================================" | Out-File -Append -FilePath $logFile
Write-Output "Ejecución: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')" | Out-File -Append -FilePath $logFile
Write-Output "========================================`n" | Out-File -Append -FilePath $logFile

try {
    # Ejecutar el script de Python
    python auto_commit.py 2>&1 | Out-File -Append -FilePath $logFile
    
    Write-Output "`n✅ Script ejecutado exitosamente" | Out-File -Append -FilePath $logFile
    
} catch {
    Write-Output "`n❌ Error al ejecutar el script:" | Out-File -Append -FilePath $logFile
    Write-Output $_.Exception.Message | Out-File -Append -FilePath $logFile
}

Write-Output "`n========================================`n" | Out-File -Append -FilePath $logFile
