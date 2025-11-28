@echo off
chcp 65001 >nul
echo.
echo ╔════════════════════════════════════════╗
echo ║   🚀 CONFIGURADOR AUTO-COMMIT GITHUB   ║
echo ╔════════════════════════════════════════╝
echo.
echo Elige una opción:
echo.
echo   1. ✅ Probar el sistema (NO requiere admin)
echo   2. ⚙️  Configurar tarea automática (requiere admin)
echo   3. 📝 Ver README del proyecto
echo   4. 📚 Ver guía de instalación completa
echo   5. 🚪 Salir
echo.
set /p opcion="Ingresa el número de tu opción: "

if "%opcion%"=="1" (
    echo.
    echo Ejecutando prueba del sistema...
    powershell.exe -ExecutionPolicy Bypass -File "probar_sistema.ps1"
    goto :end
)

if "%opcion%"=="2" (
    echo.
    echo ⚠️  Este paso requiere permisos de Administrador
    echo.
    pause
    powershell.exe -ExecutionPolicy Bypass -Command "Start-Process PowerShell -ArgumentList '-ExecutionPolicy Bypass -File configurar_tarea.ps1' -Verb RunAs"
    goto :end
)

if "%opcion%"=="3" (
    echo.
    start notepad.exe "README.md"
    goto :end
)

if "%opcion%"=="4" (
    echo.
    start notepad.exe "INSTALACION.md"
    goto :end
)

if "%opcion%"=="5" (
    echo.
    echo ¡Hasta luego! 👋
    timeout /t 2 >nul
    exit
)

echo.
echo ❌ Opción inválida
pause

:end
echo.
pause
