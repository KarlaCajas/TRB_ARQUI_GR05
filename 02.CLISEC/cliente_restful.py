"""
Cliente de Escritorio RESTful con Tkinter
Autor: Monster University Team
Fecha: 2025-11-04
"""

import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk, ImageDraw
import requests
import os

BASE_URL = "http://localhost:8080/WS_ConersionUnidades_RESTFULL/webresources"
USUARIO_VALIDO = "MONSTER"
CONTRASENA_VALIDA = "Monster9"


class ClienteRESTfulApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Login - Sistema de Conversión de Unidades")
        self.root.geometry("500x650")
        self.root.resizable(False, False)
        self.root.configure(bg='#E8F4F8')
        
        self.color_bg = "#E8F4F8"
        self.color_blue = "#4A90E2"
        self.color_title = "#2E5C8A"
        self.color_white = "#FFFFFF"
        
        self.usuario_actual = None
        self.mostrar_login()
    
    def limpiar_ventana(self):
        for widget in self.root.winfo_children():
            widget.destroy()
    
    def mostrar_login(self):
        self.limpiar_ventana()
        self.root.title("🎓 Monster University - Login")
        self.root.geometry("480x650")
        self.root.configure(bg=self.color_bg)
        
        # Frame principal centrado
        main_frame = tk.Frame(self.root, bg='white', relief=tk.RAISED, borderwidth=3)
        main_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER, width=420, height=580)
        
        # Contenedor interno
        inner_frame = tk.Frame(main_frame, bg='white')
        inner_frame.pack(fill=tk.BOTH, expand=True, padx=30, pady=25)
        
        # Imagen circular de Sullivan
        img_path = os.path.join(os.path.dirname(__file__), "login-solivan.jpeg")
        try:
            if os.path.exists(img_path):
                # Crear imagen circular
                img = Image.open(img_path)
                img = img.resize((140, 140), Image.Resampling.LANCZOS)
                
                # Crear máscara circular
                mask = Image.new('L', (140, 140), 0)
                from PIL import ImageDraw
                draw = ImageDraw.Draw(mask)
                draw.ellipse((0, 0, 140, 140), fill=255)
                
                # Aplicar máscara
                img.putalpha(mask)
                
                # Crear borde circular
                border_size = 150
                bordered_img = Image.new('RGBA', (border_size, border_size), (74, 144, 226, 255))
                mask_border = Image.new('L', (border_size, border_size), 0)
                draw_border = ImageDraw.Draw(mask_border)
                draw_border.ellipse((0, 0, border_size, border_size), fill=255)
                bordered_img.putalpha(mask_border)
                
                # Pegar imagen original en el centro
                bordered_img.paste(img, (5, 5), img)
                
                self.photo = ImageTk.PhotoImage(bordered_img)
                img_label = tk.Label(inner_frame, image=self.photo, bg='white')
                img_label.pack(pady=(0, 15))
        except Exception as e:
            print(f"Error cargando imagen: {e}")
        
        # Título con estilo
        titulo_frame = tk.Frame(inner_frame, bg='white')
        titulo_frame.pack(pady=(0, 8))
        
        tk.Label(titulo_frame, text="🎓 MONSTER UNIVERSITY 🎓", font=('Arial', 14, 'bold'), bg='white', fg=self.color_title).pack()
        tk.Label(titulo_frame, text="Sistema de Conversión de Unidades", font=('Arial', 9), bg='white', fg='#666666').pack(pady=(3, 0))
        
        # Línea decorativa
        linea = tk.Frame(inner_frame, height=3, bg=self.color_blue)
        linea.pack(fill=tk.X, pady=15)
        
        # Header de login
        login_header = tk.Frame(inner_frame, bg='white')
        login_header.pack(pady=(8, 15))
        
        tk.Label(login_header, text="🔐 Iniciar Sesión", font=('Arial', 12, 'bold'), bg='white', fg=self.color_title).pack()
        
        # Campo Usuario
        usuario_container = tk.Frame(inner_frame, bg='white')
        usuario_container.pack(fill=tk.X, pady=(8, 0))
        
        usuario_label_frame = tk.Frame(usuario_container, bg='white')
        usuario_label_frame.pack(anchor=tk.W, pady=(0, 4))
        
        tk.Label(usuario_label_frame, text="👤", font=('Arial', 11), bg='white').pack(side=tk.LEFT, padx=(0, 4))
        tk.Label(usuario_label_frame, text="Usuario:", font=('Arial', 10, 'bold'), bg='white', fg='#333333').pack(side=tk.LEFT)
        
        self.entry_usuario = tk.Entry(usuario_container, font=('Arial', 11), relief=tk.SOLID, borderwidth=2, bg='#F8F9FA')
        self.entry_usuario.pack(fill=tk.X, ipady=8)
        
        # Campo Contraseña
        password_container = tk.Frame(inner_frame, bg='white')
        password_container.pack(fill=tk.X, pady=(12, 0))
        
        password_label_frame = tk.Frame(password_container, bg='white')
        password_label_frame.pack(anchor=tk.W, pady=(0, 4))
        
        tk.Label(password_label_frame, text="🔒", font=('Arial', 11), bg='white').pack(side=tk.LEFT, padx=(0, 4))
        tk.Label(password_label_frame, text="Contraseña:", font=('Arial', 10, 'bold'), bg='white', fg='#333333').pack(side=tk.LEFT)
        
        self.entry_password = tk.Entry(password_container, font=('Arial', 11), show='●', relief=tk.SOLID, borderwidth=2, bg='#F8F9FA')
        self.entry_password.pack(fill=tk.X, ipady=8)
        self.entry_password.bind('<Return>', lambda e: self.validar_login())
        
        # Botones
        botones_frame = tk.Frame(inner_frame, bg='white')
        botones_frame.pack(pady=(20, 8), fill=tk.X)
        
        btn_login = tk.Button(botones_frame, text="🔓 INGRESAR", font=('Arial', 11, 'bold'), bg=self.color_blue, fg='white', relief=tk.FLAT, cursor='hand2', command=self.validar_login, height=2)
        btn_login.pack(fill=tk.X, pady=(0, 8))
        
        btn_salir = tk.Button(botones_frame, text="❌ SALIR", font=('Arial', 10, 'bold'), bg='#E74C3C', fg='white', relief=tk.FLAT, cursor='hand2', command=self.salir_aplicacion, height=2)
        btn_salir.pack(fill=tk.X)
        
        # Footer
        footer = tk.Label(inner_frame, text="💡 Credenciales: MONSTER / Monster9", font=('Arial', 8, 'italic'), bg='white', fg='#7F8C8D')
        footer.pack(pady=(15, 0))
        
        btn_login = tk.Button(main_frame, text="Iniciar Sesión", font=('Arial', 12, 'bold'), bg=self.color_blue, fg='white', relief=tk.FLAT, cursor='hand2', command=self.validar_login, width=30, height=2)
        btn_login.pack(pady=30)
    
    def salir_aplicacion(self):
        if messagebox.askyesno("Salir", "¿Está seguro que desea salir de la aplicación?"):
            self.root.quit()
            self.root.destroy()
    
    def validar_login(self):
        usuario = self.entry_usuario.get().strip()
        password = self.entry_password.get()
        
        if usuario == USUARIO_VALIDO and password == CONTRASENA_VALIDA:
            self.usuario_actual = usuario
            messagebox.showinfo("Exito", f"Bienvenido, {usuario}!")
            self.mostrar_dashboard()
        else:
            messagebox.showerror("Error", "Credenciales incorrectas")
            self.entry_password.delete(0, tk.END)
    
    def mostrar_dashboard(self):
        self.limpiar_ventana()
        self.root.title("🎓 Monster University - Sistema de Conversión")
        self.root.geometry("650x750")
        
        canvas = tk.Canvas(self.root, width=650, height=750, highlightthickness=0)
        canvas.pack(fill=tk.BOTH, expand=True)
        
        # Imagen de fondo
        img_fondo_path = os.path.join(os.path.dirname(__file__), "Monsters_university_6.jpg")
        try:
            if os.path.exists(img_fondo_path):
                img_fondo = Image.open(img_fondo_path)
                img_fondo = img_fondo.resize((650, 750), Image.Resampling.LANCZOS)
                self.photo_fondo = ImageTk.PhotoImage(img_fondo)
                canvas.create_image(0, 0, image=self.photo_fondo, anchor=tk.NW)
        except:
            canvas.configure(bg='white')
        
        # Header mejorado
        header = tk.Frame(canvas, bg=self.color_blue)
        canvas.create_window(325, 35, window=header, width=650, height=70)
        
        header_content = tk.Frame(header, bg=self.color_blue)
        header_content.pack(expand=True)
        
        tk.Label(header_content, text="🎓 MONSTER UNIVERSITY 🎓", font=('Arial', 14, 'bold'), bg=self.color_blue, fg='white').pack()
        tk.Label(header_content, text="Sistema de Conversión de Unidades RESTful", font=('Arial', 10), bg=self.color_blue, fg='white').pack(pady=(3, 0))
        
        # Contenedor principal centrado y más llamativo
        main_container = tk.Frame(canvas, bg='white', relief=tk.RAISED, borderwidth=3)
        canvas.create_window(325, 430, window=main_container, width=600, height=630)
        
        # Frame interno con mejor padding
        form_frame = tk.Frame(main_container, bg='white')
        form_frame.pack(fill=tk.BOTH, expand=True, padx=30, pady=25)
        
        # Título de sección
        tk.Label(form_frame, text="📊 Configuración de Conversión", font=('Arial', 12, 'bold'), bg='white', fg=self.color_title).grid(row=0, column=0, pady=(0, 15), sticky='w')
        
        # Categoría con mejor diseño
        cat_label_frame = tk.Frame(form_frame, bg='white')
        cat_label_frame.grid(row=1, column=0, sticky='w', pady=(5, 4))
        
        tk.Label(cat_label_frame, text="📂", font=('Arial', 11), bg='white').pack(side=tk.LEFT, padx=(0, 4))
        tk.Label(cat_label_frame, text="Categoría:", font=('Arial', 10, 'bold'), bg='white', fg='#333333').pack(side=tk.LEFT)
        
        self.combo_categoria = ttk.Combobox(form_frame, values=["Longitud", "Temperatura", "Masa"], state='readonly', font=('Arial', 10), width=62)
        self.combo_categoria.grid(row=2, column=0, pady=(0, 15), ipady=7)
        self.combo_categoria.bind('<<ComboboxSelected>>', self.actualizar_conversiones)
        
        # Conversión con mejor diseño
        conv_label_frame = tk.Frame(form_frame, bg='white')
        conv_label_frame.grid(row=3, column=0, sticky='w', pady=(5, 4))
        
        tk.Label(conv_label_frame, text="🔄", font=('Arial', 11), bg='white').pack(side=tk.LEFT, padx=(0, 4))
        tk.Label(conv_label_frame, text="Tipo de Conversión:", font=('Arial', 10, 'bold'), bg='white', fg='#333333').pack(side=tk.LEFT)
        
        self.combo_conversion = ttk.Combobox(form_frame, state='readonly', font=('Arial', 10), width=62)
        self.combo_conversion.grid(row=4, column=0, pady=(0, 15), ipady=7)
        
        # Valor con mejor diseño
        val_label_frame = tk.Frame(form_frame, bg='white')
        val_label_frame.grid(row=5, column=0, sticky='w', pady=(5, 4))
        
        tk.Label(val_label_frame, text="🔢", font=('Arial', 11), bg='white').pack(side=tk.LEFT, padx=(0, 4))
        tk.Label(val_label_frame, text="Valor a Convertir:", font=('Arial', 10, 'bold'), bg='white', fg='#333333').pack(side=tk.LEFT)
        
        self.entry_valor = tk.Entry(form_frame, font=('Arial', 11), relief=tk.SOLID, borderwidth=2, bg='#F8F9FA')
        self.entry_valor.grid(row=6, column=0, pady=(0, 18), ipady=8, sticky='ew')
        self.entry_valor.bind('<Return>', lambda e: self.realizar_conversion())
        
        # Botones mejorados
        botones = tk.Frame(form_frame, bg='white')
        botones.grid(row=7, column=0, pady=12)
        
        tk.Button(botones, text="✅ CONVERTIR", font=('Arial', 10, 'bold'), bg='#27AE60', fg='white', width=18, height=2, relief=tk.FLAT, cursor='hand2', command=self.realizar_conversion).pack(side=tk.LEFT, padx=6)
        tk.Button(botones, text="🗑️ LIMPIAR", font=('Arial', 10, 'bold'), bg='#FF9800', fg='white', width=18, height=2, relief=tk.FLAT, cursor='hand2', command=self.limpiar_campos).pack(side=tk.LEFT, padx=6)
        
        # Frame de resultado más atractivo
        result_frame = tk.Frame(form_frame, bg='#E8F8F5', relief=tk.SOLID, borderwidth=3)
        result_frame.grid(row=8, column=0, pady=18, ipady=18, sticky='ew')
        
        tk.Label(result_frame, text="✨ Resultado de la Conversión ✨", font=('Arial', 11, 'bold'), bg='#E8F8F5', fg='#1B5E20').pack(pady=(8, 4))
        
        self.label_resultado = tk.Label(result_frame, text="Ingrese los datos y presione CONVERTIR", font=('Arial', 10, 'bold'), bg='#E8F8F5', fg='#27AE60', wraplength=500)
        self.label_resultado.pack(pady=8)
        
        # Botón de salir en el dashboard
        footer_frame = tk.Frame(form_frame, bg='white')
        footer_frame.grid(row=9, column=0, pady=(15, 0))
        
        tk.Button(footer_frame, text="🚪 CERRAR SESIÓN", font=('Arial', 9, 'bold'), bg='#E74C3C', fg='white', width=22, height=2, relief=tk.FLAT, cursor='hand2', command=self.logout).pack(side=tk.LEFT, padx=4)
        tk.Button(footer_frame, text="❌ SALIR DEL PROGRAMA", font=('Arial', 9, 'bold'), bg='#95A5A6', fg='white', width=22, height=2, relief=tk.FLAT, cursor='hand2', command=self.salir_aplicacion).pack(side=tk.LEFT, padx=4)
        
        self.conversiones_map = {
            "Longitud": {
                "Kilometros -> Metros": ("conversion/km-a-m", "km", "m"),
                "Metros -> Centimetros": ("conversion/m-a-cm", "m", "cm"),
                "Centimetros -> Milimetros": ("conversion/cm-a-mm", "cm", "mm")
            },
            "Temperatura": {
                "Celsius -> Fahrenheit": ("conversion/celsius-a-fahrenheit", "°C", "°F"),
                "Fahrenheit -> Celsius": ("conversion/fahrenheit-a-celsius", "°F", "°C"),
                "Celsius -> Kelvin": ("conversion/celsius-a-kelvin", "°C", "K")
            },
            "Masa": {
                "Kilogramos -> Gramos": ("conversion/kg-a-gramos", "kg", "g"),
                "Gramos -> Miligramos": ("conversion/gramos-a-miligramos", "g", "mg"),
                "Toneladas -> Kilogramos": ("conversion/toneladas-a-kg", "t", "kg")
            }
        }
    
    def actualizar_conversiones(self, event=None):
        categoria = self.combo_categoria.get()
        if categoria in self.conversiones_map:
            self.combo_conversion['values'] = list(self.conversiones_map[categoria].keys())
            self.combo_conversion.current(0)
    
    def limpiar_campos(self):
        self.combo_categoria.set('')
        self.combo_conversion.set('')
        self.combo_conversion['values'] = []
        self.entry_valor.delete(0, tk.END)
        self.label_resultado.config(
            text="Ingrese los datos y presione CONVERTIR",
            fg='#27AE60',
            font=('Arial', 10, 'bold')
        )
    
    def realizar_conversion(self):
        try:
            categoria = self.combo_categoria.get()
            conversion = self.combo_conversion.get()
            valor_str = self.entry_valor.get().strip()
            
            if not categoria:
                messagebox.showwarning("Advertencia", "Por favor, selecciona una categoría")
                return
            
            if not conversion:
                messagebox.showwarning("Advertencia", "Por favor, selecciona un tipo de conversión")
                return
            
            if not valor_str:
                messagebox.showwarning("Advertencia", "Por favor, ingresa un valor")
                return
            
            valor = float(valor_str)
            
            endpoint, u1, u2 = self.conversiones_map[categoria][conversion]
            response = requests.get(f"{BASE_URL}/{endpoint}/{valor}", timeout=5)
            
            if response.status_code == 200:
                resultado = float(response.text)
                self.label_resultado.config(
                    text=f"✅ {valor} {u1} = {resultado:.4f} {u2}",
                    fg='#1B5E20',
                    font=('Arial', 11, 'bold')
                )
            else:
                raise Exception("Error en el servidor")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa un número válido")
            self.label_resultado.config(text="❌ Valor inválido", fg='#C0392B')
        except Exception as e:
            messagebox.showerror("Error", f"Error en la conversión\n\nVerifica que el servidor esté activo")
            self.label_resultado.config(text="❌ Error en la conversión", fg='#C0392B')
    
    def logout(self):
        self.usuario_actual = None
        self.mostrar_login()


def main():
    root = tk.Tk()
    app = ClienteRESTfulApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
