# 🎨 Guía de Uso - Interfaz Gráfica

## 🚀 Inicio Rápido

### Abrir la Aplicación

**Opción más fácil:**
```bash
# Doble click en:
Abrir_UI.bat
```

**Otras opciones:**
```bash
# PowerShell:
.\abrir_ui.ps1

# Python directo:
python ui_autocommit.py
```

---

## 📋 Guía Visual de la Interfaz

### 🎯 Pestaña 1: CONFIGURACIÓN

Aquí configuras todo el sistema:

#### 📦 Repositorio de GitHub
1. **URL del repositorio**: Ingresa la URL de tu repositorio
   - Ejemplo: `https://github.com/usuario/faking_okey.git`
   - Click en **"Verificar"** para comprobar que existe

#### 🔢 Configuración de Commits
2. **Mínimo de commits diarios**: Número mínimo de commits (ej: 3)
3. **Máximo de commits diarios**: Número máximo de commits (ej: 10)
   - El sistema elegirá un número aleatorio entre estos valores cada día

#### ⏰ Programación de Ejecución
4. **Hora de ejecución**: Ingresa la hora en formato 24h (ej: `10:00`)
   - El sistema se ejecutará automáticamente a esta hora cada día

#### 💾 Guardar
5. Click en **"Guardar Configuración"** para aplicar los cambios
   - Esto actualiza tanto la UI como el script `auto_commit.py`

---

### 🎮 Pestaña 2: CONTROL

Aquí controlas y ejecutas el sistema:

#### 📊 Estado del Repositorio
Muestra información en tiempo real:
- Estado actual del repositorio Git
- Últimos 5 commits
- Remotes configurados

Click en **"Actualizar Estado"** para refrescar la información

#### 🚀 Acciones

**Fila 1:**
- **✅ Ejecutar Ahora (Prueba)**
  - Ejecuta el script inmediatamente para probar que funciona
  - Los commits se crean y suben a GitHub
  - Úsalo ANTES de configurar la tarea automática

- **📋 Inicializar Git**
  - Inicializa el repositorio Git
  - Configura el remote con GitHub
  - Configura la rama principal (main)
  - Úsalo la primera vez, antes de usar el sistema

**Fila 2:**
- **⚙️ Configurar Tarea Automática**
  - Crea una tarea en el Programador de Tareas de Windows
  - Requiere permisos de administrador
  - La tarea se ejecutará diariamente a la hora configurada
  - ⚠️ Solo hazlo DESPUÉS de probar con "Ejecutar Ahora"

- **🗑️ Eliminar Tarea**
  - Elimina la tarea del Programador de Tareas
  - Detiene las ejecuciones automáticas
  - Requiere confirmación

**Fila 3:**
- **📤 Push Manual a GitHub**
  - Hace push de commits pendientes a GitHub
  - Útil si algo falló y quieres reintentar

- **📁 Abrir Carpeta del Proyecto**
  - Abre el explorador de Windows en la carpeta del proyecto
  - Para acceder rápidamente a los archivos

#### 📄 Salida de Comandos
- Muestra la salida de todos los comandos ejecutados
- Ayuda a ver qué está pasando y detectar errores

---

### 📋 Pestaña 3: LOGS

Aquí ves el historial de ejecuciones:

#### Ver Logs
1. La lista muestra todos los archivos de log disponibles
2. Click en un archivo para ver su contenido
3. Los logs más recientes aparecen primero

#### Controles
- **🔄 Actualizar Logs**: Refresca la lista de archivos
- **🗑️ Limpiar Logs**: Limpia el visor (no elimina archivos)

---

### ❓ Pestaña 4: AYUDA

Guía de uso integrada con:
- Instrucciones paso a paso
- Solución de problemas comunes
- Enlaces a documentación adicional

---

## 🎯 Flujo de Trabajo Recomendado

### Primera Vez (Configuración Inicial)

**Paso 1: Crear Repositorio en GitHub**
1. Ve a https://github.com/new
2. Crea un repositorio llamado `faking_okey`
3. NO marques "Initialize with README"

**Paso 2: Configurar en la UI**
1. Abre la UI: doble click en `Abrir_UI.bat`
2. Ve a la pestaña **"⚙️ Configuración"**
3. Ingresa la URL de tu repositorio
4. Ajusta mínimo y máximo de commits (ej: 3-10)
5. Elige la hora de ejecución (ej: 10:00)
6. Click en **"💾 Guardar Configuración"**

**Paso 3: Inicializar Git**
1. Ve a la pestaña **"🎮 Control"**
2. Click en **"📋 Inicializar Git"**
3. Verifica la salida en el panel inferior

**Paso 4: Hacer Primer Commit**
```bash
# En PowerShell o CMD:
git add .
git commit -m "🚀 Initial commit - Sistema de auto-commits"
git push -u origin main
```

> **Nota:** La primera vez que hagas push, GitHub te pedirá credenciales.
> - Usuario: tu nombre de usuario
> - Contraseña: usa un **Personal Access Token** (no tu contraseña)
> 
> Para obtener el token:
> - GitHub → Settings → Developer settings → Personal access tokens
> - Genera uno con permiso `repo`

**Paso 5: Probar el Sistema**
1. En la UI, click en **"✅ Ejecutar Ahora (Prueba)"**
2. Observa la salida en el panel inferior
3. Verifica que aparecen mensajes de éxito
4. Ve a GitHub y confirma que los commits están ahí

**Paso 6: Configurar Ejecución Automática**
1. Click en **"⚙️ Configurar Tarea Automática"**
2. Se abrirá una ventana de PowerShell pidiendo permisos de admin
3. Acepta los permisos
4. ¡Listo! El sistema se ejecutará diariamente

---

### Uso Diario (Después de Configurar)

**¡No tienes que hacer nada!** El sistema funciona automáticamente.

**Opcional - Monitorear:**
1. Abre la UI cuando quieras
2. Ve a **"📋 Logs"** para ver las ejecuciones
3. Ve a **"🎮 Control"** para ver el estado del repositorio

---

## 🔧 Personalización

### Cambiar el Número de Commits
1. Ve a **"⚙️ Configuración"**
2. Ajusta "Mínimo" y "Máximo"
3. Click en **"💾 Guardar Configuración"**

### Cambiar la Hora de Ejecución
1. Ve a **"⚙️ Configuración"**
2. Cambia la "Hora de ejecución"
3. Click en **"💾 Guardar Configuración"**
4. Ve a **"🎮 Control"**
5. Click en **"⚙️ Configurar Tarea Automática"** nuevamente
   - Esto actualizará la hora en el Programador de Tareas

---

## 🐛 Solución de Problemas

### ❌ "Error al conectar con GitHub"

**Causa:** URL del repositorio incorrecta o remote no configurado

**Solución:**
1. Verifica que la URL sea correcta
2. Ve a **"🎮 Control"**
3. Click en **"📋 Inicializar Git"**

---

### ❌ "Error de autenticación" al hacer push

**Causa:** Credenciales no guardadas o incorrectas

**Solución:**
1. Usa un **Personal Access Token** en lugar de tu contraseña
2. Desde PowerShell:
   ```bash
   git config --global credential.helper manager-core
   git push  # Te pedirá credenciales
   ```
3. Usuario: tu nombre de usuario de GitHub
4. Contraseña: tu Personal Access Token

---

### ❌ La aplicación no abre

**Causa:** Python no instalado o no en PATH

**Solución:**
1. Verifica que Python está instalado:
   ```bash
   python --version
   ```
2. Si no está instalado, descarga de: https://www.python.org/downloads/
3. Al instalar, marca "Add Python to PATH"

---

### ❌ "La tarea no se ejecuta automáticamente"

**Causa:** Tarea no configurada correctamente

**Solución:**
1. Verifica que la tarea existe:
   - Presiona `Win + R`
   - Escribe `taskschd.msc`
   - Busca "GitHub Auto Commit - Faking Okey"
2. En la UI, elimina y recrea la tarea:
   - **"🗑️ Eliminar Tarea"**
   - **"⚙️ Configurar Tarea Automática"**

---

## 💡 Consejos y Trucos

### ✅ Mejores Prácticas

1. **Prueba primero manualmente:**
   - Usa "Ejecutar Ahora" antes de configurar la tarea automática
   - Asegúrate de que los commits aparecen en GitHub

2. **Revisa los logs regularmente:**
   - Ve a la pestaña "Logs" cada tanto
   - Verifica que no hay errores

3. **Cantidad de commits realista:**
   - 3-10 commits es un rango razonable
   - No exageres (50+ commits diarios se ve sospechoso)

4. **Mantén las credenciales guardadas:**
   - Usa Git Credential Manager
   - Evita tener que ingresar credenciales cada vez

---

## 📊 Indicadores Visuales

### 🟢 Verde = Éxito
- Configuración guardada
- Comando ejecutado correctamente
- Tarea configurada

### 🔵 Azul = Información
- Estado neutral
- Información general

### 🟡 Amarillo = Advertencia
- Algo requiere atención
- Verifica la configuración

### 🔴 Rojo = Error
- Algo falló
- Revisa la salida de comandos o logs

---

## 🎓 Recursos Adicionales

- **[LEEME.md](LEEME.md)** - Guía completa del sistema
- **[INSTALACION.md](INSTALACION.md)** - Guía de instalación detallada
- **[INICIO_RAPIDO.md](INICIO_RAPIDO.md)** - Guía rápida de 3 pasos

---

## 📞 ¿Necesitas Más Ayuda?

1. **Revisa los logs** en la pestaña "Logs"
2. **Lee la pestaña "Ayuda"** dentro de la aplicación
3. **Ejecuta comandos manualmente** para ver errores detallados
4. **Verifica la documentación** en los archivos .md

---

**¡Disfruta de tu GitHub siempre activo! 🎉**
