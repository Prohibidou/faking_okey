#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de Auto-Commit para GitHub
Hace commits y push automáticos al README.md de forma diaria
"""

import os
import sys
import random
import time
from datetime import datetime
import subprocess

# Configurar encoding UTF-8 para Windows
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')


# Configuración
REPO_PATH = os.path.dirname(os.path.abspath(__file__))
README_FILE = os.path.join(REPO_PATH, "README.md")
MIN_COMMITS = 3
MAX_COMMITS = 10

# Mensajes de commit variados
COMMIT_MESSAGES = [
    "📝 Actualización diaria del README",
    "✨ Mejoras en la documentación",
    "🔄 Actualización automática",
    "📊 Actualización de estadísticas",
    "🚀 Mejoras continuas",
    "💡 Actualización de información",
    "🎯 Actualización programada",
    "⚡ Optimización de contenido",
    "🔧 Mantenimiento del repositorio",
    "📈 Actualización de progreso",
    "🌟 Mejoras generales",
    "🎨 Actualización de formato",
]

# Frases para agregar al README
ACTIVITY_PHRASES = [
    "Desarrollo activo en progreso",
    "Trabajando en nuevas características",
    "Mejorando la base de código",
    "Optimizando el rendimiento",
    "Actualizando dependencias",
    "Revisando la documentación",
    "Implementando mejoras",
    "Refinando funcionalidades",
    "Depurando el código",
    "Añadiendo tests",
    "Mejorando la arquitectura",
    "Optimizando recursos",
]


def run_command(command, cwd=None):
    """Ejecuta un comando y retorna el resultado"""
    try:
        result = subprocess.run(
            command,
            cwd=cwd or REPO_PATH,
            shell=True,
            check=True,
            capture_output=True,
            text=True,
            encoding='utf-8'
        )
        return True, result.stdout
    except subprocess.CalledProcessError as e:
        return False, e.stderr


def initialize_repo():
    """Inicializa el repositorio si no existe"""
    git_dir = os.path.join(REPO_PATH, ".git")
    
    if not os.path.exists(git_dir):
        print("🔧 Inicializando repositorio Git...")
        run_command("git init")
        
    # Verificar si existe origin
    success, output = run_command("git remote -v")
    if success and "origin" not in output:
        print("⚠️  No hay remote 'origin' configurado.")
        print("   Por favor ejecuta manualmente:")
        print("   git remote add origin <URL_DE_TU_REPO>")
        return False
    
    return True


def create_or_update_readme():
    """Crea o actualiza el README.md"""
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
    date_str = now.strftime("%Y-%m-%d")
    activity = random.choice(ACTIVITY_PHRASES)
    
    # Si el README no existe, crear uno básico
    if not os.path.exists(README_FILE):
        content = f"""# Faking Okey

Este es un proyecto en desarrollo activo.

## 📊 Actividad Reciente

- **{timestamp}**: {activity}

## 🚀 Actualizaciones Diarias

### {date_str}
- {activity}

---
*Última actualización automática: {timestamp}*
"""
    else:
        # Leer el contenido actual
        with open(README_FILE, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Agregar nueva entrada
        new_entry = f"\n- **{timestamp}**: {activity}"
        
        # Si existe la sección de actividad reciente, agregar ahí
        if "## 📊 Actividad Reciente" in content:
            content = content.replace(
                "## 📊 Actividad Reciente\n",
                f"## 📊 Actividad Reciente\n{new_entry}\n"
            )
        else:
            # Agregar al final
            content += new_entry
        
        # Actualizar timestamp al final
        if "*Última actualización automática:" in content:
            import re
            content = re.sub(
                r'\*Última actualización automática:.*?\*',
                f'*Última actualización automática: {timestamp}*',
                content
            )
        else:
            content += f"\n\n---\n*Última actualización automática: {timestamp}*\n"
    
    # Escribir el archivo
    with open(README_FILE, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ README actualizado: {activity}")


def make_commit():
    """Hace un commit del README"""
    # Agregar el archivo
    success, _ = run_command("git add README.md")
    if not success:
        print("❌ Error al agregar README.md")
        return False
    
    # Hacer commit
    message = random.choice(COMMIT_MESSAGES)
    success, _ = run_command(f'git commit -m "{message}"')
    if not success:
        print("⚠️  No hay cambios para commitear")
        return False
    
    print(f"✅ Commit realizado: {message}")
    return True


def push_changes():
    """Hace push de los cambios"""
    print("🔄 Haciendo push...")
    success, output = run_command("git push origin main")
    
    if not success:
        # Intentar con 'master' si 'main' falla
        print("   Intentando con rama 'master'...")
        success, output = run_command("git push origin master")
    
    if success:
        print("✅ Push completado exitosamente")
        return True
    else:
        print(f"❌ Error al hacer push: {output}")
        return False


def main():
    """Función principal"""
    print("=" * 60)
    print("🤖 Auto-Commit Script para GitHub")
    print("=" * 60)
    print(f"📁 Directorio: {REPO_PATH}")
    print(f"📅 Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    # Inicializar repo si es necesario
    if not initialize_repo():
        print("\n❌ El repositorio no está configurado correctamente.")
        sys.exit(1)
    
    # Determinar número de commits
    num_commits = random.randint(MIN_COMMITS, MAX_COMMITS)
    print(f"🎲 Se realizarán {num_commits} commits\n")
    
    commits_realizados = 0
    
    # Realizar los commits
    for i in range(num_commits):
        print(f"\n--- Commit {i + 1}/{num_commits} ---")
        
        # Actualizar README
        create_or_update_readme()
        
        # Hacer commit
        if make_commit():
            commits_realizados += 1
        
        # Pequeña pausa entre commits para que tengan timestamps diferentes
        if i < num_commits - 1:
            time.sleep(random.randint(1, 3))
    
    # Hacer push de todos los commits
    if commits_realizados > 0:
        print("\n" + "=" * 60)
        push_changes()
        print("\n✨ Proceso completado exitosamente!")
        print(f"📊 Total de commits realizados: {commits_realizados}")
    else:
        print("\n⚠️  No se realizaron commits")
    
    print("=" * 60)


if __name__ == "__main__":
    main()
