#!/usr/bin/env python3
"""
Interfaz Gráfica para Auto-Commit GitHub
GUI moderna y fácil de usar para configurar y gestionar commits automáticos
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext, filedialog
import subprocess
import os
import json
from datetime import datetime
import threading
import glob

# Configuración
CONFIG_FILE = "config.json"
REPO_PATH = os.path.dirname(os.path.abspath(__file__))


class AutoCommitGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🤖 Auto-Commit GitHub - Control Panel")
        self.root.geometry("1000x750")
        self.root.resizable(True, True)
        
        # Configuración de estilo
        self.setup_styles()
        
        # Variables
        self.github_url = tk.StringVar()
        self.min_commits = tk.IntVar(value=3)
        self.max_commits = tk.IntVar(value=10)
        self.exec_hour = tk.StringVar(value="10:00")
        self.status_text = tk.StringVar(value="Sistema listo")
        
        # Cargar configuración guardada
        self.load_config()
        
        # Crear interfaz
        self.create_widgets()
        
        # Actualizar estado inicial
        self.update_git_status()
    
    def setup_styles(self):
        """Configurar estilos visuales"""
        style = ttk.Style()
        style.theme_use('clam')
        
        # Colores
        bg_color = "#f0f0f0"
        accent_color = "#0066cc"
        success_color = "#28a745"
        danger_color = "#dc3545"
        
        self.root.configure(bg=bg_color)
        
        # Estilo para frames
        style.configure('Card.TFrame', background='white', relief='raised', borderwidth=1)
        style.configure('TFrame', background=bg_color)
        
        # Estilo para labels
        style.configure('Title.TLabel', font=('Segoe UI', 16, 'bold'), background='white')
        style.configure('Subtitle.TLabel', font=('Segoe UI', 10), background='white', foreground='#666')
        style.configure('TLabel', background='white', font=('Segoe UI', 9))
        
        # Estilo para botones
        style.configure('Accent.TButton', font=('Segoe UI', 10, 'bold'), background=accent_color)
        style.configure('Success.TButton', font=('Segoe UI', 10), background=success_color)
        style.configure('Danger.TButton', font=('Segoe UI', 10), background=danger_color)
    
    def create_widgets(self):
        """Crear todos los widgets de la interfaz"""
        
        # Header
        header = tk.Frame(self.root, bg="#0066cc", height=80)
        header.pack(fill='x', padx=0, pady=0)
        
        title = tk.Label(header, text="🤖 Auto-Commit GitHub", 
                        font=('Segoe UI', 20, 'bold'), bg="#0066cc", fg="white")
        title.pack(pady=20)
        
        # Container principal con scroll
        main_container = tk.Frame(self.root, bg="#f0f0f0")
        main_container.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Notebook (pestañas)
        self.notebook = ttk.Notebook(main_container)
        self.notebook.pack(fill='both', expand=True)
        
        # Pestaña 1: Configuración
        self.create_config_tab()
        
        # Pestaña 2: Control
        self.create_control_tab()
        
        # Pestaña 3: Logs
        self.create_logs_tab()
        
        # Pestaña 4: Ayuda
        self.create_help_tab()
        
        # Barra de estado
        self.create_status_bar()
    
    def create_config_tab(self):
        """Pestaña de configuración"""
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="⚙️ Configuración")
        
        # Canvas con scroll
        canvas = tk.Canvas(tab, bg='white', highlightthickness=0)
        scrollbar = ttk.Scrollbar(tab, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg='white')
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Sección: Repositorio GitHub
        self.create_section(scrollable_frame, "📦 Repositorio de GitHub", 0)
        
        repo_frame = tk.Frame(scrollable_frame, bg='white')
        repo_frame.pack(fill='x', padx=20, pady=10)
        
        tk.Label(repo_frame, text="URL del repositorio:", bg='white', font=('Segoe UI', 9)).pack(anchor='w')
        
        url_frame = tk.Frame(repo_frame, bg='white')
        url_frame.pack(fill='x', pady=5)
        
        url_entry = ttk.Entry(url_frame, textvariable=self.github_url, font=('Segoe UI', 9), width=50)
        url_entry.pack(side='left', fill='x', expand=True)
        
        ttk.Button(url_frame, text="Verificar", command=self.verify_repo).pack(side='left', padx=5)
        
        tk.Label(repo_frame, text="Ejemplo: https://github.com/usuario/faking_okey.git", 
                bg='white', font=('Segoe UI', 8), foreground='#666').pack(anchor='w')
        
        # Sección: Configuración de Commits
        self.create_section(scrollable_frame, "🔢 Configuración de Commits", 1)
        
        commits_frame = tk.Frame(scrollable_frame, bg='white')
        commits_frame.pack(fill='x', padx=20, pady=10)
        
        # Min commits
        min_frame = tk.Frame(commits_frame, bg='white')
        min_frame.pack(fill='x', pady=5)
        tk.Label(min_frame, text="Mínimo de commits diarios:", bg='white', width=25, anchor='w').pack(side='left')
        ttk.Spinbox(min_frame, from_=1, to=20, textvariable=self.min_commits, width=10).pack(side='left')
        
        # Max commits
        max_frame = tk.Frame(commits_frame, bg='white')
        max_frame.pack(fill='x', pady=5)
        tk.Label(max_frame, text="Máximo de commits diarios:", bg='white', width=25, anchor='w').pack(side='left')
        ttk.Spinbox(max_frame, from_=1, to=50, textvariable=self.max_commits, width=10).pack(side='left')
        
        # Sección: Programación
        self.create_section(scrollable_frame, "⏰ Programación de Ejecución", 2)
        
        schedule_frame = tk.Frame(scrollable_frame, bg='white')
        schedule_frame.pack(fill='x', padx=20, pady=10)
        
        time_frame = tk.Frame(schedule_frame, bg='white')
        time_frame.pack(fill='x', pady=5)
        tk.Label(time_frame, text="Hora de ejecución diaria (HH:MM):", bg='white', width=25, anchor='w').pack(side='left')
        ttk.Entry(time_frame, textvariable=self.exec_hour, width=10).pack(side='left')
        tk.Label(time_frame, text="(Formato 24 horas)", bg='white', font=('Segoe UI', 8), 
                foreground='#666').pack(side='left', padx=10)
        
        # Botones de acción
        button_frame = tk.Frame(scrollable_frame, bg='white')
        button_frame.pack(fill='x', padx=20, pady=20)
        
        ttk.Button(button_frame, text="💾 Guardar Configuración", 
                  command=self.save_config, style='Accent.TButton').pack(side='left', padx=5)
        ttk.Button(button_frame, text="🔄 Recargar", 
                  command=self.load_config).pack(side='left', padx=5)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
    
    def create_control_tab(self):
        """Pestaña de control y ejecución"""
        tab = tk.Frame(self.notebook, bg='white')
        self.notebook.add(tab, text="🎮 Control")
        
        # Crear canvas con scrollbar
        canvas = tk.Canvas(tab, bg='white', highlightthickness=0)
        scrollbar = ttk.Scrollbar(tab, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg='white')
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Habilitar scroll con la rueda del mouse
        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        canvas.bind_all("<MouseWheel>", _on_mousewheel)
        
        # Estado del repositorio
        status_card = tk.LabelFrame(scrollable_frame, text="📊 Estado del Repositorio", 
                                   font=('Segoe UI', 11, 'bold'), bg='white', padx=20, pady=20)
        status_card.pack(fill='x', padx=20, pady=10)
        
        self.git_status_text = scrolledtext.ScrolledText(status_card, height=6, 
                                                         font=('Consolas', 9), bg='#f8f8f8')
        self.git_status_text.pack(fill='x')
        
        ttk.Button(status_card, text="🔄 Actualizar Estado", 
                  command=self.update_git_status).pack(pady=5)
        
        # Acciones principales
        actions_card = tk.LabelFrame(scrollable_frame, text="🚀 Acciones", 
                                    font=('Segoe UI', 11, 'bold'), bg='white', padx=20, pady=20)
        actions_card.pack(fill='x', padx=20, pady=10)
        
        # Fila 1
        row1 = tk.Frame(actions_card, bg='white')
        row1.pack(fill='x', pady=5)
        
        ttk.Button(row1, text="✅ Ejecutar Ahora (Prueba)", 
                  command=self.run_manual, style='Success.TButton').pack(side='left', padx=5, fill='x', expand=True)
        ttk.Button(row1, text="📋 Inicializar Git", 
                  command=self.init_git).pack(side='left', padx=5, fill='x', expand=True)
        
        # Fila 2
        row2 = tk.Frame(actions_card, bg='white')
        row2.pack(fill='x', pady=5)
        
        ttk.Button(row2, text="🎯 Hacer Primer Commit", 
                  command=self.first_commit).pack(side='left', padx=5, fill='x', expand=True)
        ttk.Button(row2, text="📤 Push Manual a GitHub", 
                  command=self.manual_push).pack(side='left', padx=5, fill='x', expand=True)
        
        # Fila 3
        row3 = tk.Frame(actions_card, bg='white')
        row3.pack(fill='x', pady=5)
        
        ttk.Button(row3, text="⚙️ Configurar Tarea Automática", 
                  command=self.setup_scheduled_task, style='Accent.TButton').pack(side='left', padx=5, fill='x', expand=True)
        ttk.Button(row3, text="🗑️ Eliminar Tarea", 
                  command=self.remove_scheduled_task, style='Danger.TButton').pack(side='left', padx=5, fill='x', expand=True)
        
        # Fila 4
        row4 = tk.Frame(actions_card, bg='white')
        row4.pack(fill='x', pady=5)
        
        ttk.Button(row4, text="📁 Abrir Carpeta del Proyecto", 
                  command=self.open_project_folder).pack(side='left', padx=5, fill='x', expand=True)
        ttk.Button(row4, text="🔍 Ver en GitHub", 
                  command=self.open_github).pack(side='left', padx=5, fill='x', expand=True)
        
        # Output de comandos
        output_card = tk.LabelFrame(scrollable_frame, text="📄 Salida de Comandos", 
                                   font=('Segoe UI', 11, 'bold'), bg='white', padx=20, pady=20)
        output_card.pack(fill='both', expand=True, padx=20, pady=10)
        
        # Instrucciones
        tk.Label(output_card, text="Aquí verás la salida de los comandos ejecutados:", 
                bg='white', font=('Segoe UI', 9), fg='#666').pack(anchor='w', pady=(0, 5))
        
        self.output_text = scrolledtext.ScrolledText(output_card, height=12, 
                                                     font=('Consolas', 9), bg='#282c34', 
                                                     fg='#abb2bf', insertbackground='white',
                                                     wrap='word')
        self.output_text.pack(fill='both', expand=True)
        
        # Mensaje inicial
        self.output_text.insert('end', "💡 Listo para ejecutar comandos...\n")
        self.output_text.insert('end', "   Click en cualquier botón de acción arriba.\n\n")
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
    
    def create_logs_tab(self):
        """Pestaña de logs"""
        tab = tk.Frame(self.notebook, bg='white')
        self.notebook.add(tab, text="📋 Logs")
        
        # Controles
        controls = tk.Frame(tab, bg='white')
        controls.pack(fill='x', padx=20, pady=10)
        
        ttk.Button(controls, text="🔄 Actualizar Logs", 
                  command=self.load_logs).pack(side='left', padx=5)
        ttk.Button(controls, text="🗑️ Limpiar Logs", 
                  command=self.clear_logs).pack(side='left', padx=5)
        
        # Lista de archivos de log
        log_list_frame = tk.LabelFrame(tab, text="📁 Archivos de Log", 
                                      font=('Segoe UI', 10, 'bold'), bg='white')
        log_list_frame.pack(fill='x', padx=20, pady=10)
        
        self.log_listbox = tk.Listbox(log_list_frame, height=5, font=('Segoe UI', 9))
        self.log_listbox.pack(fill='x', padx=10, pady=10)
        self.log_listbox.bind('<<ListboxSelect>>', self.on_log_select)
        
        # Visor de logs
        log_viewer_frame = tk.LabelFrame(tab, text="📄 Contenido del Log", 
                                        font=('Segoe UI', 10, 'bold'), bg='white')
        log_viewer_frame.pack(fill='both', expand=True, padx=20, pady=10)
        
        self.log_text = scrolledtext.ScrolledText(log_viewer_frame, 
                                                  font=('Consolas', 9), bg='#f8f8f8')
        self.log_text.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Cargar logs inicialmente
        self.load_logs()
    
    def create_help_tab(self):
        """Pestaña de ayuda"""
        tab = tk.Frame(self.notebook, bg='white')
        self.notebook.add(tab, text="❓ Ayuda")
        
        help_text = scrolledtext.ScrolledText(tab, font=('Segoe UI', 10), 
                                             bg='white', wrap='word')
        help_text.pack(fill='both', expand=True, padx=20, pady=20)
        
        help_content = """
🚀 GUÍA DE USO RÁPIDO

1️⃣ CONFIGURACIÓN INICIAL:
   • Ve a la pestaña "Configuración"
   • Ingresa la URL de tu repositorio de GitHub
   • Ajusta el número de commits (3-10 recomendado)
   • Elige la hora de ejecución diaria
   • Click en "Guardar Configuración"

2️⃣ CONECTAR CON GITHUB:
   • Asegúrate de tener un repositorio creado en GitHub
   • Click en "Inicializar Git" si aún no lo has hecho
   • Necesitarás un Personal Access Token de GitHub:
     → GitHub → Settings → Developer settings → Personal access tokens
     → Genera uno con permiso "repo"
   
3️⃣ PROBAR EL SISTEMA:
   • Ve a la pestaña "Control"
   • Click en "Ejecutar Ahora (Prueba)"
   • Verifica que los commits aparecen en GitHub
   
4️⃣ CONFIGURAR EJECUCIÓN AUTOMÁTICA:
   • Click en "Configurar Tarea Automática"
   • Esto requiere permisos de administrador
   • El sistema se ejecutará diariamente a la hora configurada

📋 CARACTERÍSTICAS:

✅ Commits Aleatorios: Entre el mínimo y máximo que configures
✅ Push Automático: Sube los commits a GitHub automáticamente
✅ Logs Detallados: Revisa todos los logs en la pestaña "Logs"
✅ Fácil de Usar: Interfaz gráfica intuitiva

⚠️ IMPORTANTE:

• Asegúrate de tener Python y Git instalados
• Usa un Personal Access Token, no tu contraseña de GitHub
• La primera vez ejecuta una prueba manual
• Revisa los logs si algo no funciona

🔧 SOLUCIÓN DE PROBLEMAS:

❌ "Error al conectar con GitHub"
   → Verifica que la URL del repositorio sea correcta
   → Asegúrate de tener el remote configurado

❌ "Error de autenticación"
   → Usa un Personal Access Token de GitHub
   → Configura Git Credential Manager

❌ "La tarea no se ejecuta"
   → Verifica que la tarea está habilitada en el Programador de Tareas
   → Revisa los logs para ver errores

📚 MÁS AYUDA:

Ver archivos de documentación:
• LEEME.md - Guía principal completa
• INICIO_RAPIDO.md - Guía rápida
• INSTALACION.md - Instalación detallada
        """
        
        help_text.insert('1.0', help_content)
        help_text.config(state='disabled')
    
    def create_status_bar(self):
        """Crear barra de estado"""
        status_bar = tk.Frame(self.root, bg="#0066cc", height=30)
        status_bar.pack(fill='x', side='bottom')
        
        status_label = tk.Label(status_bar, textvariable=self.status_text, 
                               bg="#0066cc", fg="white", font=('Segoe UI', 9))
        status_label.pack(side='left', padx=10)
        
        time_label = tk.Label(status_bar, text=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                             bg="#0066cc", fg="white", font=('Segoe UI', 9))
        time_label.pack(side='right', padx=10)
        
        # Actualizar hora cada segundo
        def update_time():
            time_label.config(text=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            self.root.after(1000, update_time)
        
        update_time()
    
    def create_section(self, parent, title, row):
        """Crear una sección con título"""
        section = tk.Frame(parent, bg='#f0f0f0', height=40)
        section.pack(fill='x', padx=10, pady=(20, 0))
        
        tk.Label(section, text=title, font=('Segoe UI', 12, 'bold'), 
                bg='#f0f0f0', fg='#0066cc').pack(anchor='w', padx=10, pady=10)
    
    def load_config(self):
        """Cargar configuración desde archivo"""
        try:
            if os.path.exists(CONFIG_FILE):
                with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
                    config = json.load(f)
                    self.github_url.set(config.get('github_url', ''))
                    self.min_commits.set(config.get('min_commits', 3))
                    self.max_commits.set(config.get('max_commits', 10))
                    self.exec_hour.set(config.get('exec_hour', '10:00'))
                self.status_text.set("✅ Configuración cargada")
        except Exception as e:
            messagebox.showerror("Error", f"Error al cargar configuración: {str(e)}")
    
    def save_config(self):
        """Guardar configuración"""
        try:
            config = {
                'github_url': self.github_url.get(),
                'min_commits': self.min_commits.get(),
                'max_commits': self.max_commits.get(),
                'exec_hour': self.exec_hour.get()
            }
            
            with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
                json.dump(config, f, indent=4)
            
            # También actualizar auto_commit.py
            self.update_auto_commit_script()
            
            self.status_text.set("✅ Configuración guardada")
            messagebox.showinfo("Éxito", "Configuración guardada correctamente")
        except Exception as e:
            messagebox.showerror("Error", f"Error al guardar configuración: {str(e)}")
    
    def update_auto_commit_script(self):
        """Actualizar el script auto_commit.py con la configuración actual"""
        try:
            script_path = os.path.join(REPO_PATH, 'auto_commit.py')
            with open(script_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Actualizar MIN_COMMITS y MAX_COMMITS
            import re
            content = re.sub(r'MIN_COMMITS = \d+', f'MIN_COMMITS = {self.min_commits.get()}', content)
            content = re.sub(r'MAX_COMMITS = \d+', f'MAX_COMMITS = {self.max_commits.get()}', content)
            
            with open(script_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
        except Exception as e:
            print(f"Error al actualizar script: {e}")
    
    def verify_repo(self):
        """Verificar repositorio"""
        url = self.github_url.get()
        if not url:
            messagebox.showwarning("Advertencia", "Por favor ingresa una URL de repositorio")
            return
        
        self.run_command_async(f'git ls-remote {url}', 
                              success_msg="✅ Repositorio verificado correctamente",
                              error_msg="❌ Error al verificar repositorio")
    
    def update_git_status(self):
        """Actualizar estado de Git"""
        def update():
            status = self.run_command('git status')
            log = self.run_command('git log --oneline -5')
            remote = self.run_command('git remote -v')
            
            text = f"=== ESTADO DEL REPOSITORIO ===\n{status}\n\n"
            text += f"=== ÚLTIMOS 5 COMMITS ===\n{log}\n\n"
            text += f"=== REMOTES ===\n{remote}"
            
            self.git_status_text.delete('1.0', 'end')
            self.git_status_text.insert('1.0', text)
        
        threading.Thread(target=update, daemon=True).start()
    
    def run_manual(self):
        """Ejecutar script manualmente"""
        def run():
            self.output_text.delete('1.0', 'end')
            self.output_text.insert('end', "🚀 Ejecutando auto_commit.py...\n\n")
            
            result = self.run_command('python auto_commit.py')
            self.output_text.insert('end', result)
            self.output_text.insert('end', "\n\n✅ Ejecución completada")
            
            self.update_git_status()
        
        threading.Thread(target=run, daemon=True).start()
    
    def init_git(self):
        """Inicializar Git y conectar con GitHub"""
        url = self.github_url.get()
        if not url:
            messagebox.showwarning("Advertencia", "Por favor configura la URL del repositorio primero")
            return
        
        def init():
            self.output_text.delete('1.0', 'end')
            self.output_text.insert('end', "🔧 Inicializando Git...\n\n")
            
            # Init
            result = self.run_command('git init')
            self.output_text.insert('end', f"{result}\n")
            
            # Add remote
            self.output_text.insert('end', "➕ Agregando remote...\n")
            result = self.run_command(f'git remote add origin {url}')
            if 'already exists' in result:
                self.output_text.insert('end',  "ℹ️ Remote ya existe, actualizando URL...\n")
                result = self.run_command(f'git remote set-url origin {url}')
            self.output_text.insert('end', f"{result}\n")
            
            # Set branch
            self.output_text.insert('end', "🌿 Configurando rama main...\n")
            result = self.run_command('git branch -M main')
            self.output_text.insert('end', f"{result}\n")
            
            self.output_text.insert('end', "\n✅ Git inicializado correctamente")
            self.update_git_status()
        
        threading.Thread(target=init, daemon=True).start()
    
    def first_commit(self):
        """Hacer el primer commit con todos los archivos"""
        if messagebox.askyesno("Confirmar", "Esto agregará TODOS los archivos y hará el primer commit.\n¿Continuar?"):
            def commit():
                self.output_text.delete('1.0', 'end')
                self.output_text.insert('end', "🎯 Haciendo primer commit...\n\n")
                
                # Agregar todos los archivos
                self.output_text.insert('end', "➕ Agregando archivos...\n")
                result = self.run_command('git add .')
                self.output_text.insert('end', f"{result}\n")
                
                # Commit
                self.output_text.insert('end', "\n📝 Creando commit inicial...\n")
                result = self.run_command('git commit -m "🚀 Initial commit - Sistema de auto-commits"')
                self.output_text.insert('end', f"{result}\n")
                
                # Push
                self.output_text.insert('end', "\n📤 Haciendo push a GitHub...\n")
                result = self.run_command('git push -u origin main')
                self.output_text.insert('end', f"{result}\n")
                
                if 'error' in result.lower() or 'fatal' in result.lower():
                    self.output_text.insert('end', "\n\n⚠️ Si aparece error de autenticación:\n")
                    self.output_text.insert('end', "1. Usuario: tu nombre de usuario de GitHub\n")
                    self.output_text.insert('end', "2. Contraseña: usa un Personal Access Token (no tu contraseña)\n")
                    self.output_text.insert('end', "\n💡 Para obtener el token:\n")
                    self.output_text.insert('end', "   GitHub → Settings → Developer settings → Personal access tokens\n")
                else:
                    self.output_text.insert('end', "\n\n✅ Primer commit completado!")
                    messagebox.showinfo("Éxito", "Primer commit realizado y subido a GitHub!")
                
                self.update_git_status()
            
            threading.Thread(target=commit, daemon=True).start()
    
    def open_github(self):
        """Abrir el repositorio en GitHub"""
        url = self.github_url.get()
        if url:
            # Convertir URL de git a URL web
            web_url = url.replace('.git', '').replace('git@github.com:', 'https://github.com/')
            import webbrowser
            webbrowser.open(web_url)
        else:
            messagebox.showwarning("Advertencia", "Configura la URL del repositorio primero")
    
    def manual_push(self):
        """Push manual a GitHub"""
        def push():
            self.output_text.delete('1.0', 'end')
            self.output_text.insert('end', "📤 Haciendo push a GitHub...\n\n")
            
            result = self.run_command('git push origin main')
            self.output_text.insert('end', result)
            
            if 'error' in result.lower() or 'fatal' in result.lower():
                self.output_text.insert('end', "\n\n❌ Error al hacer push")
            else:
                self.output_text.insert('end', "\n\n✅ Push completado")
        
        threading.Thread(target=push, daemon=True).start()
    
    def setup_scheduled_task(self):
        """Configurar tarea programada"""
        hour = self.exec_hour.get()
        
        if not self.validate_time(hour):
            messagebox.showerror("Error", "Formato de hora inválido. Usa HH:MM (ej: 10:00)")
            return
        
        # Crear script de PowerShell temporal
        ps_script = f"""
$action = New-ScheduledTaskAction -Execute "PowerShell.exe" `
    -Argument "-ExecutionPolicy Bypass -WindowStyle Hidden -File `"{REPO_PATH}\\run_auto_commit.ps1`""

$trigger = New-ScheduledTaskTrigger -Daily -At {hour}

$principal = New-ScheduledTaskPrincipal -UserId "$env:USERNAME" -LogonType S4U -RunLevel Highest

$settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -StartWhenAvailable

Register-ScheduledTask -TaskName "GitHub Auto Commit - Faking Okey" `
    -Action $action `
    -Trigger $trigger `
    -Principal $principal `
    -Settings $settings `
    -Description "Commits automáticos diarios" -Force
"""
        
        temp_ps = os.path.join(REPO_PATH, 'temp_setup.ps1')
        with open(temp_ps, 'w', encoding='utf-8') as f:
            f.write(ps_script)
        
        # Ejecutar como administrador
        try:
            subprocess.run(['powershell', '-Command', 
                          f"Start-Process PowerShell -ArgumentList '-ExecutionPolicy Bypass -File {temp_ps}' -Verb RunAs"],
                         check=True)
            messagebox.showinfo("Éxito", f"Tarea programada configurada para ejecutarse a las {hour} diariamente")
            self.status_text.set(f"✅ Tarea configurada para las {hour}")
        except Exception as e:
            messagebox.showerror("Error", f"Error al configurar tarea: {str(e)}")
        finally:
            if os.path.exists(temp_ps):
                try:
                    os.remove(temp_ps)
                except:
                    pass
    
    def remove_scheduled_task(self):
        """Eliminar tarea programada"""
        if messagebox.askyesno("Confirmar", "¿Estás seguro de eliminar la tarea programada?"):
            result = self.run_command('Unregister-ScheduledTask -TaskName "GitHub Auto Commit - Faking Okey" -Confirm:$false')
            if 'error' not in result.lower():
                messagebox.showinfo("Éxito", "Tarea programada eliminada")
                self.status_text.set("✅ Tarea eliminada")
            else:
                messagebox.showerror("Error", "Error al eliminar tarea")
    
    def open_project_folder(self):
        """Abrir carpeta del proyecto"""
        os.startfile(REPO_PATH)
    
    def load_logs(self):
        """Cargar lista de archivos de log"""
        self.log_listbox.delete(0, 'end')
        
        log_folder = os.path.join(REPO_PATH, 'logs')
        if not os.path.exists(log_folder):
            return
        
        log_files = glob.glob(os.path.join(log_folder, '*.log'))
        log_files.sort(reverse=True)  # Más recientes primero
        
        for log_file in log_files:
            self.log_listbox.insert('end', os.path.basename(log_file))
    
    def on_log_select(self, event):
        """Cuando se selecciona un archivo de log"""
        selection = self.log_listbox.curselection()
        if not selection:
            return
        
        filename = self.log_listbox.get(selection[0])
        log_path = os.path.join(REPO_PATH, 'logs', filename)
        
        try:
            with open(log_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            self.log_text.delete('1.0', 'end')
            self.log_text.insert('1.0', content)
        except Exception as e:
            self.log_text.delete('1.0', 'end')
            self.log_text.insert('1.0', f"Error al leer log: {str(e)}")
    
    def clear_logs(self):
        """Limpiar visualizador de logs"""
        self.log_text.delete('1.0', 'end')
    
    def run_command(self, command):
        """Ejecutar comando y retornar salida"""
        try:
            result = subprocess.run(
                command,
                shell=True,
                cwd=REPO_PATH,
                capture_output=True,
                text=True,
                encoding='utf-8'
            )
            return result.stdout + result.stderr
        except Exception as e:
            return f"Error: {str(e)}"
    
    def run_command_async(self, command, success_msg=None, error_msg=None):
        """Ejecutar comando de forma asíncrona"""
        def run():
            result = self.run_command(command)
            if 'error' in result.lower() or 'fatal' in result.lower():
                if error_msg:
                    self.status_text.set(error_msg)
            else:
                if success_msg:
                    self.status_text.set(success_msg)
        
        threading.Thread(target=run, daemon=True).start()
    
    def validate_time(self, time_str):
        """Validar formato de hora"""
        try:
            from datetime import datetime
            datetime.strptime(time_str, '%H:%M')
            return True
        except:
            return False


def main():
    root = tk.Tk()
    app = AutoCommitGUI(root)
    
    # Centrar ventana
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f'{width}x{height}+{x}+{y}')
    
    root.mainloop()


if __name__ == "__main__":
    main()
