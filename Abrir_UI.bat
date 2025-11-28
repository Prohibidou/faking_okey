@echo off
chcp 65001 >nul
cd /d "%~dp0"
echo.
echo ╔════════════════════════════════════════╗
echo ║    🚀 Iniciando Auto-Commit GUI...     ║
echo ╚════════════════════════════════════════╝
echo.
python ui_autocommit.py
if errorlevel 1 (
    echo.
    echo ❌ Error al iniciar la aplicación
    echo.
    echo Verifica que Python esté instalado correctamente
    pause
)
