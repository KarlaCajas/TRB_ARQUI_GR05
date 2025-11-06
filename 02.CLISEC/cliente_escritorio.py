"""
Cliente de Escritorio SOAP con Tkinter para consumir el servicio .NET
Autor: Sistema
Fecha: 2025-11-03
"""

import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from zeep import Client
from zeep.transports import Transport
from requests import Session as RequestsSession
import os

# Configuración
WSDL_URL = "http://localhost:63393/Service.svc?wsdl"
USUARIO_VALIDO = "MONSTER"
CONTRASENA_VALIDA = "Monster9"

# Cliente SOAP global
soap_client = None


class ClienteSOAPApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Login - Sistema de Conversión de Unidades")
        self.root.geometry("500x650")
        self.root.resizable(False, False)
        self.root.configure(bg='#E8F4F8')
        
        # Colores del diseño
        self.color_bg = "#E8F4F8"
        self.color_blue = "#4A90E2"
        self.color_title = "#2E5C8A"
        self.color_white = "#FFFFFF"
        
        # Inicializar cliente SOAP
        self.init_soap_client()
        
        # Variable de usuario logueado
        self.usuario_actual = None
        
        # Mostrar pantalla de login
        self.mostrar_login()
    
    def init_soap_client(self):
        """Inicializa el cliente SOAP"""
        global soap_client
        try:
            session = RequestsSession()
            session.verify = False
            transport = Transport(session=session)
            soap_client = Client(WSDL_URL, transport=transport)
            print("✓ Conexión establecida con el servicio SOAP")
        except Exception as e:
            messagebox.showerror("Error de Conexión", 
                               f"No se pudo conectar con el servicio SOAP:\n{str(e)}")
    
    def limpiar_ventana(self):
        """Limpia todos los widgets de la ventana"""
        for widget in self.root.winfo_children():
            widget.destroy()
    
    def mostrar_login(self):
        """Muestra la pantalla de login exacta a la imagen"""
        self.limpiar_ventana()
        self.root.title("Login - Sistema de Conversión de Unidades")
        self.root.geometry("500x650")
        self.root.configure(bg=self.color_bg)
        
        # Frame principal
        main_frame = tk.Frame(self.root, bg=self.color_bg)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=30, pady=30)
        
        # Intentar cargar imagen de Sullivan
        img_path = os.path.join(os.path.dirname(__file__), "login-solivan.jpeg")
        try:
            if os.path.exists(img_path):
                img = Image.open(img_path)
                img = img.resize((200, 200), Image.Resampling.LANCZOS)
                self.photo = ImageTk.PhotoImage(img)
                img_label = tk.Label(main_frame, image=self.photo, bg=self.color_bg)
                img_label.pack(pady=20)
            else:
                # Placeholder si no existe la imagen
                placeholder = tk.Label(main_frame, 
                                      text="🎓\nSULLIVAN",
                                      font=('Arial', 24, 'bold'),
                                      bg=self.color_bg,
                                      fg=self.color_blue)
                placeholder.pack(pady=20)
        except Exception as e:
            print(f"Error cargando imagen: {e}")
            placeholder = tk.Label(main_frame, 
                                  text="🎓\nSULLIVAN",
                                  font=('Arial', 24, 'bold'),
                                  bg=self.color_bg,
                                  fg=self.color_blue)
            placeholder.pack(pady=20)
        
        # Título
        titulo = tk.Label(main_frame, 
                         text="Sistema de Conversión de Unidades",
                         font=('Arial', 16, 'bold'),
                         bg=self.color_bg,
                         fg=self.color_title)
        titulo.pack(pady=(0, 5))
        
        # Línea azul debajo del título
        linea = tk.Frame(main_frame, height=3, bg=self.color_blue, width=350)
        linea.pack(pady=(0, 30))
        
        # Sección "Iniciar Sesión"
        login_header = tk.Frame(main_frame, bg=self.color_bg)
        login_header.pack(pady=(10, 20))
        
        icono_lock = tk.Label(login_header, text="🔐", font=('Arial', 18), bg=self.color_bg)
        icono_lock.pack(side=tk.LEFT, padx=5)
        
        login_text = tk.Label(login_header, text="Iniciar Sesión",
                             font=('Arial', 14, 'bold'),
                             bg=self.color_bg,
                             fg=self.color_title)
        login_text.pack(side=tk.LEFT)
        
        # Frame para campos de entrada
        campos_frame = tk.Frame(main_frame, bg=self.color_bg)
        campos_frame.pack(pady=10, fill=tk.X)
        
        # Usuario
        usuario_frame = tk.Frame(campos_frame, bg=self.color_bg)
        usuario_frame.pack(fill=tk.X, pady=10)
        
        usuario_icon = tk.Label(usuario_frame, text="👤", font=('Arial', 14), 
                               bg=self.color_bg, width=3)
        usuario_icon.pack(side=tk.LEFT)
        
        usuario_label = tk.Label(usuario_frame, text="Usuario:",
                                font=('Arial', 11),
                                bg=self.color_bg,
                                fg='#333333')
        usuario_label.pack(side=tk.LEFT, padx=(0, 10))
        
        self.entry_usuario = tk.Entry(campos_frame,
                                      font=('Arial', 11),
                                      relief=tk.SOLID,
                                      borderwidth=2,
                                      width=35)
        self.entry_usuario.pack(fill=tk.X, ipady=8, pady=(0, 20))
        self.entry_usuario.focus()
        
        # Contraseña
        password_frame = tk.Frame(campos_frame, bg=self.color_bg)
        password_frame.pack(fill=tk.X, pady=10)
        
        password_icon = tk.Label(password_frame, text="🔒", font=('Arial', 14),
                                bg=self.color_bg, width=3)
        password_icon.pack(side=tk.LEFT)
        
        password_label = tk.Label(password_frame, text="Contraseña:",
                                 font=('Arial', 11),
                                 bg=self.color_bg,
                                 fg='#333333')
        password_label.pack(side=tk.LEFT, padx=(0, 10))
        
        self.entry_password = tk.Entry(campos_frame,
                                       font=('Arial', 11),
                                       show='●',
                                       relief=tk.SOLID,
                                       borderwidth=2,
                                       width=35)
        self.entry_password.pack(fill=tk.X, ipady=8)
        self.entry_password.bind('<Return>', lambda e: self.validar_login())
        
        # Botón Iniciar Sesión
        btn_login = tk.Button(main_frame,
                             text="Iniciar Sesión",
                             font=('Arial', 12, 'bold'),
                             bg=self.color_blue,
                             fg='white',
                             relief=tk.FLAT,
                             cursor='hand2',
                             command=self.validar_login,
                             width=30,
                             height=2)
        btn_login.pack(pady=30)
        
        # Hover effects
        btn_login.bind('<Enter>', lambda e: btn_login.config(bg='#3A7BC8'))
        btn_login.bind('<Leave>', lambda e: btn_login.config(bg=self.color_blue))
    
    def validar_login(self):
        """Valida las credenciales de login"""
        usuario = self.entry_usuario.get().strip()
        password = self.entry_password.get()
        
        if usuario == USUARIO_VALIDO and password == CONTRASENA_VALIDA:
            self.usuario_actual = usuario
            messagebox.showinfo("Éxito", f"¡Bienvenido, {usuario}!")
            self.mostrar_dashboard()
        else:
            messagebox.showerror("Error", "Credenciales incorrectas.\nIntenta de nuevo.")
            self.entry_password.delete(0, tk.END)
            self.entry_password.focus()
    
    def mostrar_dashboard(self):
        """Muestra el dashboard exacto a la imagen proporcionada"""
        self.limpiar_ventana()
        self.root.title(f"Calculadora de Conversión de Unidades - Usuario: {self.usuario_actual}")
        self.root.geometry("680x750")
        
        # Crear canvas para imagen de fondo
        canvas = tk.Canvas(self.root, width=680, height=750, highlightthickness=0)
        canvas.pack(fill=tk.BOTH, expand=True)
        
        # Intentar cargar imagen de fondo
        img_fondo_path = os.path.join(os.path.dirname(__file__), "Monsters_university_6.jpg")
        try:
            if os.path.exists(img_fondo_path):
                img_fondo = Image.open(img_fondo_path)
                img_fondo = img_fondo.resize((680, 750), Image.Resampling.LANCZOS)
                self.photo_fondo = ImageTk.PhotoImage(img_fondo)
                canvas.create_image(0, 0, image=self.photo_fondo, anchor=tk.NW)
            else:
                # Fondo blanco si no existe la imagen
                canvas.configure(bg='white')
        except Exception as e:
            print(f"Error cargando fondo: {e}")
            canvas.configure(bg='white')
        
        # Header azul sobre el canvas
        header = tk.Frame(canvas, bg=self.color_blue, height=60)
        canvas.create_window(0, 0, window=header, anchor=tk.NW, width=680)
        
        # Icono y título en header
        header_content = tk.Frame(header, bg=self.color_blue)
        header_content.pack(side=tk.LEFT, padx=15, pady=12)
        
        icono_header = tk.Label(header_content, text="🔷", font=('Arial', 20), 
                               bg=self.color_blue, fg='white')
        icono_header.pack(side=tk.LEFT, padx=5)
        
        titulo_header = tk.Label(header_content, 
                                text="Calculadora de Conversión de Unidades",
                                font=('Arial', 12, 'bold'),
                                bg=self.color_blue,
                                fg='white')
        titulo_header.pack(side=tk.LEFT)
        
        # Usuario y logout en header
        user_frame = tk.Frame(header, bg=self.color_blue)
        user_frame.pack(side=tk.RIGHT, padx=15)
        
        user_label = tk.Label(user_frame, text=f"👤 {self.usuario_actual}",
                             font=('Arial', 10, 'bold'),
                             bg=self.color_blue,
                             fg='white')
        user_label.pack(side=tk.LEFT, padx=10)
        
        btn_logout = tk.Button(user_frame, text="🔄",
                              font=('Arial', 12),
                              bg='#3A7BC8',
                              fg='white',
                              relief=tk.FLAT,
                              cursor='hand2',
                              width=3,
                              command=self.logout)
        btn_logout.pack(side=tk.LEFT)
        
        # Frame principal blanco sobre el canvas
        main_container = tk.Frame(canvas, bg='white')
        canvas.create_window(340, 405, window=main_container, anchor=tk.CENTER, width=620, height=640)
        
        # Panel de conversión (fondo blanco, borde azul)
        panel = tk.Frame(main_container, bg='white', relief=tk.SOLID, 
                        borderwidth=3, highlightbackground='#000000',
                        highlightthickness=1)
        panel.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)
        
        # Título del panel
        titulo_panel = tk.Label(panel, 
                               text="Selecciona el tipo de conversión",
                               font=('Arial', 13, 'bold'),
                               bg=self.color_blue,
                               fg='white',
                               pady=10)
        titulo_panel.pack(fill=tk.X)
        
        # Frame interior para los campos
        form_frame = tk.Frame(panel, bg='white')
        form_frame.pack(fill=tk.BOTH, expand=True, padx=30, pady=20)
        
        # Categoría
        cat_label = tk.Label(form_frame, text="Categoría:",
                            font=('Arial', 10, 'bold'),
                            bg='white',
                            fg=self.color_title)
        cat_label.grid(row=0, column=0, sticky='w', pady=(5, 3))
        
        self.combo_categoria = ttk.Combobox(form_frame,
                                           values=["Temperatura", "Masa", "Longitud"],
                                           state='readonly',
                                           font=('Arial', 10),
                                           width=50)
        self.combo_categoria.grid(row=1, column=0, sticky='ew', pady=(0, 12), ipady=8)
        self.combo_categoria.bind('<<ComboboxSelected>>', self.actualizar_conversiones)
        
        # Conversión
        conv_label = tk.Label(form_frame, text="Conversión:",
                             font=('Arial', 10, 'bold'),
                             bg='white',
                             fg=self.color_title)
        conv_label.grid(row=2, column=0, sticky='w', pady=(5, 3))
        
        self.combo_conversion = ttk.Combobox(form_frame,
                                            state='readonly',
                                            font=('Arial', 10),
                                            width=50)
        self.combo_conversion.grid(row=3, column=0, sticky='ew', pady=(0, 12), ipady=8)
        
        # Línea divisoria
        separator = tk.Frame(form_frame, height=2, bg=self.color_blue)
        separator.grid(row=4, column=0, sticky='ew', pady=12)
        
        # Valor a convertir
        valor_label = tk.Label(form_frame, text="Valor a convertir:",
                              font=('Arial', 10, 'bold'),
                              bg='white',
                              fg=self.color_title)
        valor_label.grid(row=5, column=0, sticky='w', pady=(5, 3))
        
        self.entry_valor = tk.Entry(form_frame,
                                    font=('Arial', 11),
                                    relief=tk.SOLID,
                                    borderwidth=2)
        self.entry_valor.grid(row=6, column=0, sticky='ew', ipady=10, pady=(0, 12))
        self.entry_valor.bind('<Return>', lambda e: self.realizar_conversion_dashboard())
        
        # Botones
        botones_frame = tk.Frame(form_frame, bg='white')
        botones_frame.grid(row=7, column=0, pady=8)
        
        btn_convertir = tk.Button(botones_frame,
                                 text="🔄  CONVERTIR",
                                 font=('Arial', 10, 'bold'),
                                 bg=self.color_blue,
                                 fg='white',
                                 relief=tk.FLAT,
                                 cursor='hand2',
                                 width=16,
                                 height=1,
                                 command=self.realizar_conversion_dashboard)
        btn_convertir.grid(row=0, column=0, padx=8, ipady=8)
        
        btn_limpiar = tk.Button(botones_frame,
                               text="🗑️  LIMPIAR",
                               font=('Arial', 10, 'bold'),
                               bg='#FF9800',
                               fg='white',
                               relief=tk.FLAT,
                               cursor='hand2',
                               width=16,
                               height=1,
                               command=self.limpiar_campos)
        btn_limpiar.grid(row=0, column=1, padx=8, ipady=8)
        
        # Hover effects
        btn_convertir.bind('<Enter>', lambda e: btn_convertir.config(bg='#3A7BC8'))
        btn_convertir.bind('<Leave>', lambda e: btn_convertir.config(bg=self.color_blue))
        btn_limpiar.bind('<Enter>', lambda e: btn_limpiar.config(bg='#F57C00'))
        btn_limpiar.bind('<Leave>', lambda e: btn_limpiar.config(bg='#FF9800'))
        
        # Panel de resultado (verde)
        resultado_frame = tk.Frame(form_frame, bg='#C8E6C9', 
                                  relief=tk.SOLID, borderwidth=2,
                                  highlightbackground='#4CAF50',
                                  highlightthickness=2)
        resultado_frame.grid(row=8, column=0, sticky='ew', pady=10, ipady=18)
        
        resultado_titulo = tk.Label(resultado_frame,
                                    text="✅ Resultado:",
                                    font=('Arial', 11, 'bold'),
                                    bg='#C8E6C9',
                                    fg='#2E7D32')
        resultado_titulo.pack(pady=3)
        
        self.label_resultado = tk.Label(resultado_frame,
                                       text="---",
                                       font=('Arial', 14, 'bold'),
                                       bg='#C8E6C9',
                                       fg='#1B5E20',
                                       wraplength=500)
        self.label_resultado.pack(pady=8)
        
        # Estado del servidor (verde) - Posicionado en canvas
        estado_label = tk.Label(canvas,
                               text="✅ Servidor disponible",
                               font=('Arial', 10, 'bold'),
                               bg='white',
                               fg='#4CAF50')
        canvas.create_window(340, 720, window=estado_label, anchor=tk.CENTER)
        
        # Configurar grid
        form_frame.grid_columnconfigure(0, weight=1)
        
        # Mapeo de conversiones
        self.conversiones_map = {
            "Temperatura": {
                "Celsius → Fahrenheit": ("celsius_fahrenheit", "°C", "°F"),
                "Fahrenheit → Celsius": ("fahrenheit_celsius", "°F", "°C"),
                "Celsius → Kelvin": ("celsius_kelvin", "°C", "K")
            },
            "Masa": {
                "Kilogramos → Libras": ("kg_lb", "kg", "lb"),
                "Libras → Kilogramos": ("lb_kg", "lb", "kg"),
                "Kilogramos → Onzas": ("kg_oz", "kg", "oz")
            },
            "Longitud": {
                "Metros → Pies": ("m_ft", "m", "ft"),
                "Pies → Metros": ("ft_m", "ft", "m"),
                "Kilómetros → Millas": ("km_mi", "km", "mi")
            }
        }
    
    def actualizar_conversiones(self, event=None):
        """Actualiza el combobox de conversiones según la categoría"""
        categoria = self.combo_categoria.get()
        if categoria in self.conversiones_map:
            conversiones = list(self.conversiones_map[categoria].keys())
            self.combo_conversion['values'] = conversiones
            if conversiones:
                self.combo_conversion.current(0)
    
    def limpiar_campos(self):
        """Limpia todos los campos del formulario"""
        self.combo_categoria.set('')
        self.combo_conversion.set('')
        self.combo_conversion['values'] = []
        self.entry_valor.delete(0, tk.END)
        self.label_resultado.config(text="---")
    
    def realizar_conversion_dashboard(self):
        """Realiza la conversión desde el dashboard"""
        try:
            categoria = self.combo_categoria.get()
            conversion = self.combo_conversion.get()
            valor_str = self.entry_valor.get().strip()
            
            if not categoria or not conversion or not valor_str:
                messagebox.showwarning("Advertencia", "Por favor completa todos los campos")
                return
            
            valor = float(valor_str)
            
            # Obtener datos de la conversión
            tipo_conv, unidad_origen, unidad_destino = self.conversiones_map[categoria][conversion]
            
            # Realizar conversión SOAP
            conversiones_soap = {
                'celsius_fahrenheit': soap_client.service.CelsiusToFahrenheit,
                'fahrenheit_celsius': soap_client.service.FahrenheitToCelsius,
                'celsius_kelvin': soap_client.service.CelsiusToKelvin,
                'kg_lb': soap_client.service.KilogramsToPounds,
                'lb_kg': soap_client.service.PoundsToKilograms,
                'kg_oz': soap_client.service.KilogramsToOunces,
                'm_ft': soap_client.service.MetersToFeet,
                'ft_m': soap_client.service.FeetToMeters,
                'km_mi': soap_client.service.KilometersToMiles
            }
            
            if tipo_conv in conversiones_soap:
                resultado = conversiones_soap[tipo_conv](valor)
                self.label_resultado.config(
                    text=f"{valor} {unidad_origen} = {resultado:.4f} {unidad_destino}"
                )
            
        except ValueError:
            messagebox.showerror("Error", "Por favor ingresa un valor numérico válido")
        except Exception as e:
            messagebox.showerror("Error", f"Error al realizar la conversión:\n{str(e)}")
    
    def logout(self):
        """Cierra sesión y vuelve al login"""
        respuesta = messagebox.askyesno("Cerrar Sesión", 
                                       "¿Estás seguro de que deseas cerrar sesión?")
        if respuesta:
            self.usuario_actual = None
            self.mostrar_login()


def main():
    """Función principal"""
    root = tk.Tk()
    app = ClienteSOAPApp(root)
    
    # Centrar ventana
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f'{width}x{height}+{x}+{y}')
    
    root.mainloop()


if __name__ == "__main__":
    print("\n" + "="*60)
    print(" INICIANDO CLIENTE DE ESCRITORIO SOAP ".center(60))
    print("="*60 + "\n")
    main()
