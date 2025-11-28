# 📋 Guía de Instalación y Configuración

## ⚙️ Requisitos Previos

1. **Python 3.x** instalado en el sistema
2. **Git** instalado y configurado
3. Repositorio de GitHub creado y configurado

## 🚀 Paso 1: Configurar el Repositorio de GitHub

### 1.1 Inicializar Git (si aún no lo has hecho)

```powershell
cd "C:\Users\veram\OneDrive\Documentos\projects\faking_okey"
git init
```

### 1.2 Crear el repositorio en GitHub

1. Ve a https://github.com/new
2. Crea un nuevo repositorio llamado `faking_okey` (o el nombre que prefieras)
3. **NO inicialices con README** (ya tenemos uno)

### 1.3 Conectar el repositorio local con GitHub

```powershell
git remote add origin https://github.com/TU_USUARIO/faking_okey.git
git branch -M main
git add .
git commit -m "Initial commit"
git push -u origin main
```

### 1.4 Configurar credenciales de Git (Importante)

Para que el script funcione sin pedir credenciales:

**Opción A - Personal Access Token (Recomendado):**

1. Ve a GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Genera un nuevo token con permisos de `repo`
3. Copia el token
4. Configura Git Credential Manager:

```powershell
git config --global credential.helper manager-core
```

5. La próxima vez que hagas push, ingresa tu token como contraseña

**Opción B - SSH (Alternativa):**

```powershell
# Generar clave SSH
ssh-keygen -t ed25519 -C "tu_email@ejemplo.com"

# Agregar a GitHub: Settings → SSH and GPG keys → New SSH key
# Cambiar el remote a SSH:
git remote set-url origin git@github.com:TU_USUARIO/faking_okey.git
```

## 🤖 Paso 2: Configurar el Programador de Tareas de Windows

### Opción A: Usar el script de configuración automática

Ejecuta como **Administrador** en PowerShell:

```powershell
# Crear la tarea programada
$action = New-ScheduledTaskAction -Execute "PowerShell.exe" `
    -Argument "-ExecutionPolicy Bypass -WindowStyle Hidden -File `"C:\Users\veram\OneDrive\Documentos\projects\faking_okey\run_auto_commit.ps1`""

# Ejecutar diariamente a las 10:00 AM
$trigger = New-ScheduledTaskTrigger -Daily -At 10:00AM

# Configurar para ejecutar aunque el usuario no esté logueado
$principal = New-ScheduledTaskPrincipal -UserId "$env:USERNAME" -LogonType S4U -RunLevel Highest

# Configuración adicional
$settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -StartWhenAvailable

# Registrar la tarea
Register-ScheduledTask -TaskName "GitHub Auto Commit - Faking Okey" `
    -Action $action `
    -Trigger $trigger `
    -Principal $principal `
    -Settings $settings `
    -Description "Hace commits y push automáticos diarios al proyecto faking_okey"
```

### Opción B: Configuración manual

1. **Abrir el Programador de Tareas:**
   - Presiona `Win + R`
   - Escribe `taskschd.msc` y presiona Enter

2. **Crear nueva tarea:**
   - Click en "Crear tarea..." (no "Crear tarea básica")

3. **Pestaña General:**
   - Nombre: `GitHub Auto Commit - Faking Okey`
   - Descripción: `Hace commits y push automáticos diarios`
   - Marcar: "Ejecutar tanto si el usuario inició sesión como si no"
   - Marcar: "Ejecutar con los privilegios más altos"
   - Configurar para: Windows 10

4. **Pestaña Desencadenadores:**
   - Click en "Nuevo..."
   - Iniciar la tarea: "Según una programación"
   - Configuración: "Diariamente"
   - Hora: `10:00:00` (o la hora que prefieras)
   - Marcar: "Habilitado"
   - Click en "Aceptar"

5. **Pestaña Acciones:**
   - Click en "Nueva..."
   - Acción: "Iniciar un programa"
   - Programa: `PowerShell.exe`
   - Argumentos: 
     ```
     -ExecutionPolicy Bypass -WindowStyle Hidden -File "C:\Users\veram\OneDrive\Documentos\projects\faking_okey\run_auto_commit.ps1"
     ```
   - Click en "Aceptar"

6. **Pestaña Condiciones:**
   - DESMARCAR: "Iniciar la tarea solo si el equipo está conectado a la corriente alterna"
   - Marcar: "Iniciar la tarea aunque esté funcionando con baterías"

7. **Pestaña Configuración:**
   - Marcar: "Permitir que la tarea se ejecute a petición"
   - Marcar: "Ejecutar la tarea lo antes posible después de un inicio programado perdido"
   - Marcar: "Si la tarea falla, reiniciar cada: 1 minuto"
   - Click en "Aceptar"

## ✅ Paso 3: Probar el Sistema

### Prueba manual inmediata:

```powershell
cd "C:\Users\veram\OneDrive\Documentos\projects\faking_okey"
python auto_commit.py
```

### Prueba del script de PowerShell:

```powershell
cd "C:\Users\veram\OneDrive\Documentos\projects\faking_okey"
.\run_auto_commit.ps1
```

### Prueba de la tarea programada:

1. Abre el Programador de Tareas
2. Busca "GitHub Auto Commit - Faking Okey"
3. Click derecho → "Ejecutar"
4. Verifica los logs en la carpeta `logs/`

## 📊 Verificar que Funciona

Después de ejecutar, verifica:

1. ✅ El archivo `README.md` ha sido actualizado
2. ✅ Se han creado commits en Git: `git log`
3. ✅ Los commits están en GitHub
4. ✅ Existe un archivo de log en la carpeta `logs/`

## 🔧 Personalización

### Cambiar el número de commits diarios:

Edita `auto_commit.py` y modifica:
```python
MIN_COMMITS = 3  # Mínimo de commits
MAX_COMMITS = 10  # Máximo de commits
```

### Cambiar la hora de ejecución:

- Opción A: Modifica la tarea en el Programador de Tareas
- Opción B: Crea múltiples tareas para ejecutar varias veces al día

### Cambiar los mensajes de commit:

Edita la lista `COMMIT_MESSAGES` en `auto_commit.py`

## 🐛 Solución de Problemas

### El script no hace push

**Problema:** Credenciales de Git no configuradas

**Solución:**
```powershell
git config --global credential.helper manager-core
# Luego hacer un push manual para guardar credenciales
git push
```

### La tarea programada no se ejecuta

**Verificar:**
1. La tarea está habilitada en el Programador de Tareas
2. La ruta del archivo `.ps1` es correcta (usa rutas absolutas)
3. El usuario tiene permisos para ejecutar scripts de PowerShell

**Habilitar ejecución de scripts (como Administrador):**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Python no se encuentra

**Solución:**
```powershell
# Verificar que Python está en PATH
python --version

# Si no funciona, usa la ruta completa en run_auto_commit.ps1:
C:\Users\veram\AppData\Local\Programs\Python\Python311\python.exe auto_commit.py
```

### Los commits no tienen timestamps diferentes

El script ya incluye pausas aleatorias de 1-3 segundos entre commits

## 📝 Ver los Logs

Los logs se guardan en la carpeta `logs/` con el formato:
```
logs/auto_commit_2025-11-27.log
```

Para ver el último log:
```powershell
Get-Content .\logs\auto_commit_*.log -Tail 50
```

## 🎯 Comandos Útiles

```powershell
# Ver estado del repositorio
git status

# Ver últimos commits
git log --oneline -10

# Ver tareas programadas de este proyecto
Get-ScheduledTask | Where-Object {$_.TaskName -like "*Faking*"}

# Ver última ejecución de la tarea
Get-ScheduledTask "GitHub Auto Commit - Faking Okey" | Get-ScheduledTaskInfo

# Deshabilitar temporalmente
Disable-ScheduledTask -TaskName "GitHub Auto Commit - Faking Okey"

# Habilitar nuevamente
Enable-ScheduledTask -TaskName "GitHub Auto Commit - Faking Okey"

# Eliminar la tarea
Unregister-ScheduledTask -TaskName "GitHub Auto Commit - Faking Okey" -Confirm:$false
```

## ⚠️ Advertencias

1. **Credenciales**: Asegúrate de que Git tiene las credenciales guardadas correctamente
2. **Conexión**: El sistema necesita conexión a internet para hacer push
3. **Límites de GitHub**: No excedas los límites de rate de GitHub
4. **Batería**: Si es una laptop, la tarea se ejecutará aunque esté con batería

## 📚 Recursos Adicionales

- [Documentación de Git](https://git-scm.com/doc)
- [GitHub Personal Access Tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)
- [Programador de Tareas de Windows](https://docs.microsoft.com/es-es/windows/win32/taskschd/task-scheduler-start-page)

---

¿Necesitas ayuda? Revisa la sección de Solución de Problemas o los logs en `logs/`
