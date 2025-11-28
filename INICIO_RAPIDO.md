# 🚀 Inicio Rápido - Auto-Commit para GitHub

Este proyecto hace commits y push automáticos a GitHub todos los días, sin que tengas que hacer nada manualmente.

## ⚡ Configuración Rápida (3 pasos)

### 1️⃣ Configurar GitHub

```powershell
# Navegar al proyecto
cd "C:\Users\veram\OneDrive\Documentos\projects\faking_okey"

# Inicializar Git
git init

# Conectar con GitHub (reemplaza TU_USUARIO con tu usuario de GitHub)
git remote add origin https://github.com/TU_USUARIO/faking_okey.git

# Primer commit
git add .
git commit -m "Initial commit"
git push -u origin main
```

### 2️⃣ Probar que Funciona

```powershell
# Ejecutar el script de prueba
.\probar_sistema.ps1
```

### 3️⃣ Programar Ejecución Automática

```powershell
# Abrir PowerShell como Administrador y ejecutar:
.\configurar_tarea.ps1
```

## ✅ ¡Listo!

El sistema ahora:
- ✨ Hará entre 3-10 commits diarios automáticamente
- 🔄 Hará push a GitHub sin tu intervención
- 📝 Actualizará el README con la actividad
- ⏰ Se ejecutará todos los días a la hora que configuraste

## 📋 Archivos del Proyecto

| Archivo | Descripción |
|---------|-------------|
| `auto_commit.py` | Script principal que hace commits y push |
| `run_auto_commit.ps1` | Ejecutor para el Programador de Tareas |
| `configurar_tarea.ps1` | Configurador automático de la tarea |
| `probar_sistema.ps1` | Script de prueba |
| `README.md` | Documentación del proyecto (se actualiza automáticamente) |
| `INSTALACION.md` | Guía completa de instalación |
| `INICIO_RAPIDO.md` | Esta guía rápida |

## 🆘 Ayuda Rápida

### Ver los logs:
```powershell
Get-Content .\logs\*.log -Tail 50
```

### Ver últimos commits:
```powershell
git log --oneline -10
```

### Probar el script manualmente:
```powershell
python auto_commit.py
```

### Gestionar la tarea programada:
```powershell
# Abrir el Programador de Tareas
taskschd.msc

# O usar PowerShell (como Administrador):

# Ver estado
Get-ScheduledTask "GitHub Auto Commit - Faking Okey"

# Ejecutar ahora
Start-ScheduledTask "GitHub Auto Commit - Faking Okey"

# Deshabilitar
Disable-ScheduledTask "GitHub Auto Commit - Faking Okey"

# Habilitar
Enable-ScheduledTask "GitHub Auto Commit - Faking Okey"
```

## ⚙️ Personalización

### Cambiar cantidad de commits:

Edita `auto_commit.py`:
```python
MIN_COMMITS = 3   # Cambiar aquí
MAX_COMMITS = 10  # Cambiar aquí
```

### Cambiar hora de ejecución:

1. Ejecuta nuevamente `.\configurar_tarea.ps1` como Administrador
2. O edita la tarea en el Programador de Tareas

## ❓ ¿Problemas?

Consulta la guía completa en: **`INSTALACION.md`**

---

**🎯 Objetivo:** Mantener tu GitHub activo con commits diarios automáticos
