"""
Ventana de Login para Cliente de Conversión de Unidades
"""
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk, ImageDraw
import os

class LoginWindow:
    """Ventana de autenticación del usuario"""
    
    # Credenciales quemadas
    USUARIO_VALIDO = "MONSTER"
    CONTRASENA_VALIDA = "Monster9"
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Login - Sistema de Conversión de Unidades")
        self.root.geometry("480x580")
        self.root.resizable(False, False)
        self.root.configure(bg="#e8f4f8")
        
        # Centrar ventana
        self.center_window()
        
        # Variable para controlar si el login fue exitoso
        self.login_exitoso = False
        
        # Crear interfaz
        self.crear_interfaz()
        
    def center_window(self):
        """Centra la ventana en la pantalla"""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
    
    def crear_imagen_circular(self, ruta_imagen, size=(150, 150)):
        """Crea una imagen circular desde una imagen cuadrada"""
        try:
            # Abrir y redimensionar imagen
            img = Image.open(ruta_imagen)
            img = img.resize(size, Image.Resampling.LANCZOS)
            
            # Crear máscara circular
            mask = Image.new('L', size, 0)
            draw = ImageDraw.Draw(mask)
            draw.ellipse((0, 0) + size, fill=255)
            
            # Aplicar máscara
            output = Image.new('RGBA', size, (0, 0, 0, 0))
            output.paste(img, (0, 0))
            output.putalpha(mask)
            
            return ImageTk.PhotoImage(output)
        except Exception as e:
            print(f"Error al cargar imagen: {e}")
            return None
    
    def crear_interfaz(self):
        """Crea los elementos de la interfaz de login"""
        # Frame principal con fondo celeste claro
        main_frame = tk.Frame(self.root, bg="#e8f4f8")
        main_frame.pack(expand=True, fill="both", padx=30, pady=30)
        
        # Logo circular (si existe)
        logo_path = os.path.join(os.path.dirname(__file__), "logo_login.png")
        if os.path.exists(logo_path):
            logo_img = self.crear_imagen_circular(logo_path, (150, 150))
            if logo_img:
                logo_label = tk.Label(main_frame, image=logo_img, bg="#e8f4f8")
                logo_label.image = logo_img  # Mantener referencia
                logo_label.pack(pady=(0, 20))
        
        # Título
        titulo = tk.Label(
            main_frame,
            text="Sistema de Conversión de Unidades",
            font=("Segoe UI", 16, "bold"),
            bg="#e8f4f8",
            fg="#1a5490",
            wraplength=380
        )
        titulo.pack(pady=(0, 10))
        
        # Separador decorativo
        separador = tk.Frame(main_frame, bg="#4a90d9", height=3, width=200)
        separador.pack(pady=(0, 15))
        
        # Subtítulo
        subtitulo = tk.Label(
            main_frame,
            text="🔐 Iniciar Sesión",
            font=("Segoe UI", 14, "bold"),
            bg="#e8f4f8",
            fg="#1a5490"
        )
        subtitulo.pack(pady=(0, 25))
        
        # Frame para usuario
        usuario_frame = tk.Frame(main_frame, bg="#e8f4f8")
        usuario_frame.pack(pady=12, fill="x")
        
        tk.Label(
            usuario_frame,
            text="👤 Usuario:",
            font=("Segoe UI", 11, "bold"),
            bg="#e8f4f8",
            fg="#1a5490",
            width=13,
            anchor="w"
        ).pack(side="left")
        
        self.entry_usuario = tk.Entry(
            usuario_frame,
            font=("Segoe UI", 11),
            width=24,
            relief="solid",
            borderwidth=2,
            bg="white",
            fg="#333333"
        )
        self.entry_usuario.pack(side="left", padx=5, ipady=6)
        
        # Frame para contraseña
        password_frame = tk.Frame(main_frame, bg="#e8f4f8")
        password_frame.pack(pady=12, fill="x")
        
        tk.Label(
            password_frame,
            text="🔒 Contraseña:",
            font=("Segoe UI", 11, "bold"),
            bg="#e8f4f8",
            fg="#1a5490",
            width=13,
            anchor="w"
        ).pack(side="left")
        
        self.entry_password = tk.Entry(
            password_frame,
            font=("Segoe UI", 11),
            width=24,
            show="●",
            relief="solid",
            borderwidth=2,
            bg="white",
            fg="#333333"
        )
        self.entry_password.pack(side="left", padx=5, ipady=6)
        
        # Bind Enter key
        self.entry_usuario.bind("<Return>", lambda e: self.entry_password.focus())
        self.entry_password.bind("<Return>", lambda e: self.validar_login())
        
        # Frame para botones (más cerca de los campos)
        botones_frame = tk.Frame(main_frame, bg="#e8f4f8")
        botones_frame.pack(pady=20)
        
        # Botón de login - Celeste/Azul con bordes redondeados (MÁS GRANDE)
        self.btn_login = tk.Button(
            botones_frame,
            text="Iniciar Sesión",
            font=("Segoe UI", 14, "bold"),
            bg="#4a90d9",
            fg="white",
            activebackground="#3a7ac0",
            activeforeground="white",
            width=25,
            height=2,
            relief="raised",
            cursor="hand2",
            borderwidth=2,
            command=self.validar_login
        )
        self.btn_login.pack(pady=8, padx=20, fill="x")
        
        # Efecto hover para botón login
        self.btn_login.bind("<Enter>", lambda e: self.btn_login.config(bg="#3a7ac0"))
        self.btn_login.bind("<Leave>", lambda e: self.btn_login.config(bg="#4a90d9"))
        
        # Botón de salir - Celeste claro con bordes redondeados (MÁS GRANDE)
        self.btn_salir = tk.Button(
            botones_frame,
            text="Cancelar",
            font=("Segoe UI", 12),
            bg="#87ceeb",
            fg="white",
            activebackground="#6fb9d9",
            activeforeground="white",
            width=25,
            height=2,
            relief="raised",
            cursor="hand2",
            borderwidth=2,
            command=self.root.quit
        )
        self.btn_salir.pack(pady=8, padx=20, fill="x")
        
        # Efecto hover para botón salir
        self.btn_salir.bind("<Enter>", lambda e: self.btn_salir.config(bg="#6fb9d9"))
        self.btn_salir.bind("<Leave>", lambda e: self.btn_salir.config(bg="#87ceeb"))
        
        # Focus en el campo de usuario
        self.entry_usuario.focus()
        
    def validar_login(self):
        """Valida las credenciales ingresadas"""
        usuario = self.entry_usuario.get().strip()
        password = self.entry_password.get().strip()
        
        if not usuario or not password:
            messagebox.showwarning(
                "Campos vacíos",
                "Por favor, ingrese usuario y contraseña"
            )
            return
        
        if usuario == self.USUARIO_VALIDO and password == self.CONTRASENA_VALIDA:
            self.login_exitoso = True
            messagebox.showinfo(
                "Login Exitoso",
                f"¡Bienvenido {usuario}!"
            )
            self.root.destroy()
        else:
            messagebox.showerror(
                "Error de Autenticación",
                "Usuario o contraseña incorrectos"
            )
            self.entry_password.delete(0, tk.END)
            self.entry_usuario.focus()
    
    def ejecutar(self):
        """Ejecuta el loop principal de la ventana"""
        self.root.mainloop()
        return self.login_exitoso


if __name__ == "__main__":
    login = LoginWindow()
    if login.ejecutar():
        print("Login exitoso")
    else:
        print("Login cancelado")
