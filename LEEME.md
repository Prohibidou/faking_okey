# 📦 Sistema de Auto-Commit para GitHub

## 🎯 ¿Qué hace este proyecto?

Este sistema automáticamente:
- ✅ Hace **entre 3 y 10 commits** diarios a tu repositorio de GitHub
- ✅ Actualiza el archivo `README.md` con actividad simulada
- ✅ Hace **push** automático a GitHub
- ✅ Se ejecuta **todos los días** sin que tengas que hacer nada
- ✅ Genera **logs** de cada ejecución para que puedas revisar

## 🚀 INICIO RÁPIDO (3 Pasos)

### Paso 1: Crear el Repositorio en GitHub

1. Ve a https://github.com/new
2. Crea un repositorio llamado `faking_okey`
3. **NO marques** "Initialize with README"
4. Click en "Create repository"

### Paso 2: Conectar con GitHub

Abre PowerShell en esta carpeta y ejecuta:

```powershell
# Reemplaza TU_USUARIO con tu usuario de GitHub
git remote add origin https://github.com/TU_USUARIO/faking_okey.git

# Configurar rama principal
git branch -M main

# Primer commit
git add .
git commit -m "🚀 Initial commit - Sistema de auto-commits"
git push -u origin main
```

**IMPORTANTE:** Cuando te pida usuario/contraseña:
- Usuario: tu nombre de usuario de GitHub
- Contraseña: usa un **Personal Access Token** (no tu contraseña)

**¿Cómo obtener un Personal Access Token?**
1. GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. "Generate new token (classic)"
3. Marca el permiso `repo`
4. Genera y copia el token
5. Úsalo como contraseña al hacer push

### Paso 3: Configurar Ejecución Automática

**Opción A - Menú Interactivo (Recomendado):**
```powershell
# Doble click en el archivo:
MENU.bat

# Luego selecciona opción 1 para probar y opción 2 para configurar
```

**Opción B - Línea de comandos:**
```powershell
# 1. Probar que funciona
.\probar_sistema.ps1

# 2. Configurar (requiere Administrador)
# Click derecho en PowerShell → Ejecutar como Administrador
.\configurar_tarea.ps1
```

## 📁 Estructura del Proyecto

```
faking_okey/
├── 📄 LEEME.md                    ← ¡ESTÁS AQUÍ! Guía principal
├── 📄 INICIO_RAPIDO.md            ← Guía rápida de 3 pasos
├── 📄 INSTALACION.md              ← Guía completa y detallada
├── 📄 README.md                   ← Se actualiza automáticamente
│
├── 🐍 auto_commit.py              ← Script principal (Python)
│
├── 💻 MENU.bat                    ← Menú interactivo
├── 💻 probar_sistema.ps1          ← Prueba el sistema
├── 💻 configurar_tarea.ps1        ← Configura la tarea automática
├── 💻 run_auto_commit.ps1         ← Ejecutor para el Programador
│
├── 📋 .gitignore                  ← Configuración de Git
└── 📂 logs/                       ← Logs de ejecución (se crea automáticamente)
```

## 🎮 ¿Cómo Usar?

### Uso Diario (Automático)
**¡No tienes que hacer nada!** El sistema se ejecutará automáticamente todos los días.

### Comandos Útiles

#### Ver los logs:
```powershell
Get-Content .\logs\*.log -Tail 30
```

#### Ver últimos commits:
```powershell
git log --oneline -10
```

#### Ejecutar manualmente:
```powershell
python auto_commit.py
```

#### Ver estado de la tarea programada:
```powershell
Get-ScheduledTask "GitHub Auto Commit - Faking Okey"
```

#### Ejecutar la tarea ahora (sin esperar):
```powershell
Start-ScheduledTask "GitHub Auto Commit - Faking Okey"
```

## ⚙️ Configuración Avanzada

### Cambiar el número de commits diarios

Edita `auto_commit.py` líneas 14-15:
```python
MIN_COMMITS = 3   # Mínimo de commits por día
MAX_COMMITS = 10  # Máximo de commits por día
```

### Cambiar la hora de ejecución

1. Abre el Programador de Tareas:
   ```powershell
   taskschd.msc
   ```

2. Encuentra "GitHub Auto Commit - Faking Okey"

3. Click derecho → Propiedades → Desencadenadores → Editar

4. Cambia la hora

O simplemente ejecuta de nuevo:
```powershell
.\configurar_tarea.ps1
```

### Cambiar los mensajes de commit

Edita `auto_commit.py` líneas 18-29 (lista `COMMIT_MESSAGES`)

### Ejecutar varias veces al día

Crea múltiples tareas con `configurar_tarea.ps1` usando diferentes horas

## 🔍 Verificar que Funciona

### Después de la primera ejecución, verifica:

1. **README.md actualizado:**
   ```powershell
   type README.md
   ```

2. **Commits creados:**
   ```powershell
   git log --oneline -5
   ```

3. **Commits en GitHub:**
   - Ve a tu repositorio en GitHub
   - Deberías ver los commits

4. **Logs generados:**
   ```powershell
   dir logs
   ```

## ❓ Solución de Problemas

### "Error: git remote already exists"
```powershell
git remote remove origin
git remote add origin https://github.com/TU_USUARIO/faking_okey.git
```

### "Error: authorization failed"
Necesitas un **Personal Access Token**:
1. GitHub → Settings → Developer settings → Personal access tokens
2. Genera un nuevo token con permiso `repo`
3. Úsalo como contraseña al hacer push

```powershell
# Configurar para que guarde las credenciales
git config --global credential.helper manager-core
```

### "La tarea no se ejecuta"

1. Verifica que está habilitada:
   ```powershell
   Get-ScheduledTask "GitHub Auto Commit - Faking Okey"
   ```

2. Verifica la última ejecución:
   ```powershell
   Get-ScheduledTask "GitHub Auto Commit - Faking Okey" | Get-ScheduledTaskInfo
   ```

3. Ejecuta manualmente para ver errores:
   ```powershell
   python auto_commit.py
   ```

### "Python no se encuentra"

Instala Python desde: https://www.python.org/downloads/

Al instalar, marca la opción "Add Python to PATH"

## 📊 Monitoreo

### Ver última ejecución:
```powershell
Get-ScheduledTask "GitHub Auto Commit - Faking Okey" | Get-ScheduledTaskInfo
```

### Ver log más reciente:
```powershell
Get-ChildItem logs | Sort-Object LastWriteTime -Descending | Select-Object -First 1 | Get-Content -Tail 30
```

### Ver commits de hoy:
```powershell
git log --since="today" --oneline
```

## 🛑 Desactivar/Eliminar

### Pausar temporalmente:
```powershell
Disable-ScheduledTask "GitHub Auto Commit - Faking Okey"
```

### Reactivar:
```powershell
Enable-ScheduledTask "GitHub Auto Commit - Faking Okey"
```

### Eliminar completamente:
```powershell
Unregister-ScheduledTask "GitHub Auto Commit - Faking Okey" -Confirm:$false
```

## 📚 Documentación Adicional

- **`INICIO_RAPIDO.md`**: Guía concisa de configuración
- **`INSTALACION.md`**: Guía completa con todos los detalles
- **`README.md`**: Documentación del proyecto (se actualiza automáticamente)

## 🎯 Resumen

| Característica | Detalle |
|----------------|---------|
| 🔢 Commits diarios | 3-10 aleatorios |
| ⏰ Frecuencia | Diaria (configurable) |
| 🤖 Manual | No, completamente automático |
| 📝 Actualiza | README.md |
| 🔄 Push | Automático |
| 📊 Logs | Sí, en carpeta `logs/` |
| 💰 Costo | Gratis |

## 💡 Consejos

1. **Revisa los logs** regularmente para asegurarte de que todo funciona
2. **Mantén las credenciales de Git guardadas** para evitar errores
3. **No modifiques manualmente** el README si el script está activo (o coordina bien)
4. **Ten paciencia** - la primera ejecución puede tardar un poco

## 🆘 ¿Necesitas Ayuda?

1. Revisa `INSTALACION.md` para información detallada
2. Revisa los logs en `logs/` para ver qué ocurrió
3. Ejecuta `python auto_commit.py` manualmente para ver errores
4. Verifica que Git y Python funcionan: `git --version` y `python --version`

---

## ✅ Checklist de Configuración

- [ ] Crear repositorio en GitHub
- [ ] Generar Personal Access Token
- [ ] Conectar repositorio local con GitHub
- [ ] Hacer el primer push manual
- [ ] Probar el script: `.\probar_sistema.ps1`
- [ ] Configurar tarea automática: `.\configurar_tarea.ps1`
- [ ] Verificar que la tarea está programada
- [ ] Esperar al día siguiente o ejecutar manualmente
- [ ] Verificar que los commits aparecen en GitHub

---

**¡Disfruta de tu GitHub siempre activo! 🎉**
