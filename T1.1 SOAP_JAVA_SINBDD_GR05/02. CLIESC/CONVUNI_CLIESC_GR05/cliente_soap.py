"""
Cliente de Escritorio para Web Service SOAP de Conversión de Unidades
Grupo: GR05
"""
import tkinter as tk
from tkinter import messagebox, ttk
from zeep import Client
from zeep.exceptions import Fault
from PIL import Image, ImageTk, ImageDraw
import os


class SOAPClient:
    """Clase para manejar la comunicación con el servicio SOAP"""
    
    def __init__(self, wsdl_url):
        self.wsdl_url = wsdl_url
        self.client = None
        
    def conectar(self):
        """Establece conexión con el servicio SOAP"""
        try:
            self.client = Client(self.wsdl_url)
            return True
        except Exception as e:
            messagebox.showerror("Error de Conexión", f"No se pudo conectar al servicio SOAP:\n{str(e)}")
            return False
    
    def login(self, usuario, password):
        """Realiza el login en el servicio"""
        try:
            if not self.client:
                if not self.conectar():
                    return False
            
            resultado = self.client.service.login(usuario, password)
            return resultado
        except Fault as e:
            messagebox.showerror("Error SOAP", f"Error en el servicio:\n{str(e)}")
            return False
        except Exception as e:
            messagebox.showerror("Error", f"Error al realizar login:\n{str(e)}")
            return False
    
    def celsius_a_fahrenheit(self, celsius):
        """Convierte Celsius a Fahrenheit"""
        try:
            return self.client.service.celsiusAFahrenheit(celsius)
        except Exception as e:
            messagebox.showerror("Error", f"Error en conversión:\n{str(e)}")
            return None
    
    def fahrenheit_a_celsius(self, fahrenheit):
        """Convierte Fahrenheit a Celsius"""
        try:
            return self.client.service.fahrenheitACelsius(fahrenheit)
        except Exception as e:
            messagebox.showerror("Error", f"Error en conversión:\n{str(e)}")
            return None
    
    def celsius_a_kelvin(self, celsius):
        """Convierte Celsius a Kelvin"""
        try:
            return self.client.service.celsiusAKelvin(celsius)
        except Exception as e:
            messagebox.showerror("Error", f"Error en conversión:\n{str(e)}")
            return None
    
    def kilogramos_a_gramos(self, kg):
        """Convierte Kilogramos a Gramos"""
        try:
            return self.client.service.kilogramosAGramos(kg)
        except Exception as e:
            messagebox.showerror("Error", f"Error en conversión:\n{str(e)}")
            return None
    
    def gramos_a_miligramos(self, gramos):
        """Convierte Gramos a Miligramos"""
        try:
            return self.client.service.gramosAMiligramos(gramos)
        except Exception as e:
            messagebox.showerror("Error", f"Error en conversión:\n{str(e)}")
            return None
    
    def toneladas_a_kilogramos(self, toneladas):
        """Convierte Toneladas a Kilogramos"""
        try:
            return self.client.service.toneladasAKilogramos(toneladas)
        except Exception as e:
            messagebox.showerror("Error", f"Error en conversión:\n{str(e)}")
            return None
    
    def kilometros_a_metros(self, km):
        """Convierte Kilómetros a Metros"""
        try:
            return self.client.service.kilometrosAMetros(km)
        except Exception as e:
            messagebox.showerror("Error", f"Error en conversión:\n{str(e)}")
            return None
    
    def metros_a_centimetros(self, metros):
        """Convierte Metros a Centímetros"""
        try:
            return self.client.service.metrosACentimetros(metros)
        except Exception as e:
            messagebox.showerror("Error", f"Error en conversión:\n{str(e)}")
            return None
    
    def centimetros_a_milimetros(self, cm):
        """Convierte Centímetros a Milímetros"""
        try:
            return self.client.service.centimetrosAMilimetros(cm)
        except Exception as e:
            messagebox.showerror("Error", f"Error en conversión:\n{str(e)}")
            return None


class LoginWindow:
    """Ventana de Login"""
    
    # Credenciales quemadas
    USUARIO_CORRECTO = "MONSTER"
    PASSWORD_CORRECTO = "Monster9"
    
    def __init__(self, root, soap_client):
        self.root = root
        self.soap_client = soap_client
        self.root.title("Login - Cliente SOAP GR05")
        self.root.geometry("400x500")
        self.root.resizable(False, False)
        
        # Centrar ventana
        self.centrar_ventana()
        
        # Configurar estilo
        self.configurar_estilo()
        
        # Crear widgets
        self.crear_widgets()
    
    def centrar_ventana(self):
        """Centra la ventana en la pantalla"""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
    
    def configurar_estilo(self):
        """Configura los estilos de la aplicación"""
        self.root.configure(bg='#f0f0f0')
    
    def crear_imagen_circular(self, ruta_imagen, tamano=150):
        """Crea una imagen circular desde un archivo"""
        try:
            # Verificar si existe el archivo
            if not os.path.exists(ruta_imagen):
                return None
            
            # Abrir y redimensionar imagen
            img = Image.open(ruta_imagen)
            img = img.resize((tamano, tamano), Image.Resampling.LANCZOS)
            
            # Crear máscara circular
            mascara = Image.new('L', (tamano, tamano), 0)
            draw = ImageDraw.Draw(mascara)
            draw.ellipse((0, 0, tamano, tamano), fill=255)
            
            # Aplicar máscara
            img_circular = Image.new('RGBA', (tamano, tamano))
            img_circular.paste(img, (0, 0))
            img_circular.putalpha(mascara)
            
            # Convertir a PhotoImage
            return ImageTk.PhotoImage(img_circular)
        except Exception as e:
            print(f"Error al cargar imagen: {e}")
            return None
    
    def crear_widgets(self):
        """Crea los widgets de la ventana de login"""
        # Frame principal
        main_frame = tk.Frame(self.root, bg='#f0f0f0')
        main_frame.pack(expand=True, fill='both', padx=20, pady=20)
        
        # Cargar y mostrar imagen circular
        ruta_imagen = os.path.join(os.path.dirname(__file__), "logo_login.png")
        imagen_circular = self.crear_imagen_circular(ruta_imagen, 150)
        
        if imagen_circular:
            # Guardar referencia para evitar que se borre
            self.imagen_ref = imagen_circular
            
            label_imagen = tk.Label(
                main_frame,
                image=imagen_circular,
                bg='#f0f0f0',
                borderwidth=0
            )
            label_imagen.pack(pady=(0, 20))
        
        # Título
        titulo = tk.Label(
            main_frame, 
            text="🔐 SISTEMA DE LOGIN", 
            font=("Arial", 16, "bold"),
            bg='#f0f0f0',
            fg='#333333'
        )
        titulo.pack(pady=(0, 10))
        
        # Subtítulo
        subtitulo = tk.Label(
            main_frame,
            text="Cliente SOAP - Conversor de Unidades",
            font=("Arial", 10),
            bg='#f0f0f0',
            fg='#666666'
        )
        subtitulo.pack(pady=(0, 30))
        
        # Frame para los campos
        campos_frame = tk.Frame(main_frame, bg='#f0f0f0')
        campos_frame.pack(pady=10)
        
        # Usuario
        tk.Label(
            campos_frame,
            text="Usuario:",
            font=("Arial", 10, "bold"),
            bg='#f0f0f0',
            fg='#333333'
        ).grid(row=0, column=0, sticky='w', pady=5)
        
        self.entry_usuario = tk.Entry(
            campos_frame,
            font=("Arial", 10),
            width=25,
            relief=tk.SOLID,
            borderwidth=1
        )
        self.entry_usuario.grid(row=0, column=1, pady=5, padx=(10, 0))
        
        # Password
        tk.Label(
            campos_frame,
            text="Contraseña:",
            font=("Arial", 10, "bold"),
            bg='#f0f0f0',
            fg='#333333'
        ).grid(row=1, column=0, sticky='w', pady=5)
        
        self.entry_password = tk.Entry(
            campos_frame,
            font=("Arial", 10),
            width=25,
            show="*",
            relief=tk.SOLID,
            borderwidth=1
        )
        self.entry_password.grid(row=1, column=1, pady=5, padx=(10, 0))
        
        # Botón de login
        self.btn_login = tk.Button(
            main_frame,
            text="INGRESAR",
            font=("Arial", 11, "bold"),
            bg='#4CAF50',
            fg='white',
            activebackground='#45a049',
            activeforeground='white',
            cursor='hand2',
            width=20,
            height=2,
            relief=tk.FLAT,
            command=self.realizar_login
        )
        self.btn_login.pack(pady=20)
        
        # Información
        info = tk.Label(
            main_frame,
            text="GR05 - SOAP Java Client",
            font=("Arial", 8),
            bg='#f0f0f0',
            fg='#999999'
        )
        info.pack(side='bottom')
        
        # Bind Enter key
        self.entry_password.bind('<Return>', lambda e: self.realizar_login())
        
        # Focus en usuario
        self.entry_usuario.focus()
    
    def realizar_login(self):
        """Valida las credenciales y realiza el login"""
        usuario = self.entry_usuario.get().strip()
        password = self.entry_password.get()
        
        # Validación de campos vacíos
        if not usuario or not password:
            messagebox.showwarning("Advertencia", "Por favor ingrese usuario y contraseña")
            return
        
        # Validación de credenciales locales
        if usuario != self.USUARIO_CORRECTO or password != self.PASSWORD_CORRECTO:
            messagebox.showerror("Error de Login", "Usuario o contraseña incorrectos")
            self.entry_password.delete(0, tk.END)
            return
        
        # Intentar login en el servicio SOAP
        resultado = self.soap_client.login(usuario, password)
        
        if resultado:
            messagebox.showinfo("Éxito", f"¡Bienvenido {usuario}!")
            self.abrir_ventana_principal()
        else:
            messagebox.showerror("Error", "No se pudo autenticar con el servicio SOAP")
    
    def abrir_ventana_principal(self):
        """Abre la ventana principal de la aplicación"""
        self.root.destroy()
        root_principal = tk.Tk()
        MainWindow(root_principal, self.soap_client)
        root_principal.mainloop()


class MainWindow:
    """Ventana principal de conversiones"""
    
    def __init__(self, root, soap_client):
        self.root = root
        self.soap_client = soap_client
        self.root.title("Conversor de Unidades - Cliente SOAP GR05")
        self.root.geometry("800x600")
        self.root.resizable(True, True)
        
        # Lista para almacenar referencias a los campos de entrada
        self.campos_entrada = []
        self.campos_resultado = []
        
        # Centrar ventana
        self.centrar_ventana()
        
        # Crear widgets
        self.crear_widgets()
    
    def centrar_ventana(self):
        """Centra la ventana en la pantalla"""
        self.root.update_idletasks()
        width = 800
        height = 600
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
    
    def crear_imagen_rectangular(self, ruta_imagen, ancho=200, alto=350):
        """Crea una imagen rectangular manteniendo proporciones"""
        try:
            if not os.path.exists(ruta_imagen):
                print(f"⚠️ No se encontró la imagen: {ruta_imagen}")
                return None
            
            # Abrir imagen
            imagen = Image.open(ruta_imagen)
            
            # Crear thumbnail manteniendo aspect ratio
            imagen.thumbnail((ancho, alto), Image.Resampling.LANCZOS)
            
            # Convertir a PhotoImage
            return ImageTk.PhotoImage(imagen)
        except Exception as e:
            print(f"❌ Error al cargar imagen rectangular: {e}")
            return None
    
    def crear_widgets(self):
        """Crea los widgets de la ventana principal"""
        # Frame superior con título
        header_frame = tk.Frame(self.root, bg='#2196F3', height=80)
        header_frame.pack(fill='x')
        header_frame.pack_propagate(False)
        
        # Frame para título y botones
        header_content = tk.Frame(header_frame, bg='#2196F3')
        header_content.pack(expand=True, fill='both', padx=10)
        
        # Título (izquierda)
        titulo = tk.Label(
            header_content,
            text="🔄 CONVERSOR DE UNIDADES",
            font=("Arial", 18, "bold"),
            bg='#2196F3',
            fg='white'
        )
        titulo.pack(side='left', pady=15)
        
        # Frame para botones (derecha)
        botones_frame = tk.Frame(header_content, bg='#2196F3')
        botones_frame.pack(side='right', pady=15)
        
        # Botón Limpiar Campos
        btn_limpiar = tk.Button(
            botones_frame,
            text="🗑️ Limpiar Campos",
            font=("Arial", 10, "bold"),
            bg='#FFA726',
            fg='white',
            activebackground='#FB8C00',
            activeforeground='white',
            cursor='hand2',
            relief=tk.FLAT,
            padx=15,
            pady=8,
            command=self.limpiar_campos
        )
        btn_limpiar.pack(side='left', padx=5)
        
        # Botón Cerrar Sesión
        btn_cerrar_sesion = tk.Button(
            botones_frame,
            text="🚪 Cerrar Sesión",
            font=("Arial", 10, "bold"),
            bg='#EF5350',
            fg='white',
            activebackground='#E53935',
            activeforeground='white',
            cursor='hand2',
            relief=tk.FLAT,
            padx=15,
            pady=8,
            command=self.cerrar_sesion
        )
        btn_cerrar_sesion.pack(side='left', padx=5)
        
        # Notebook para pestañas
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(expand=True, fill='both', padx=10, pady=10)
        
        # Crear pestañas
        self.crear_tab_temperatura()
        self.crear_tab_masa()
        self.crear_tab_longitud()
    
    def crear_tab_temperatura(self):
        """Crea la pestaña de conversiones de temperatura"""
        tab = tk.Frame(self.notebook, bg='#f5f5f5')
        self.notebook.add(tab, text='🌡️ Temperatura')
        
        # Container principal con grid layout
        container = tk.Frame(tab, bg='#f5f5f5')
        container.pack(expand=True, fill='both', padx=20, pady=20)
        
        # Configurar columnas del container
        container.grid_columnconfigure(0, weight=0)  # Imagen izquierda
        container.grid_columnconfigure(1, weight=1)  # Conversiones derecha
        container.grid_rowconfigure(0, weight=1)
        
        # Frame izquierdo para imagen - centrado verticalmente
        imagen_frame = tk.Frame(container, bg='#f5f5f5')
        imagen_frame.grid(row=0, column=0, sticky='ns', padx=(0, 15))
        
        # Cargar y mostrar imagen más pequeña
        ruta_imagen = os.path.join(os.path.dirname(__file__), "conten_pant.png")
        imagen_rect = self.crear_imagen_rectangular(ruta_imagen, 200, 350)
        
        if imagen_rect:
            self.imagen_temp_ref = imagen_rect
            label_img = tk.Label(imagen_frame, image=imagen_rect, bg='#f5f5f5')
            label_img.pack(expand=True, anchor='center')
        
        # Frame derecho para conversiones - centrado verticalmente
        main_frame = tk.Frame(container, bg='#f5f5f5')
        main_frame.grid(row=0, column=1, sticky='ns')
        main_frame.grid_rowconfigure(0, weight=1)
        main_frame.grid_rowconfigure(1, weight=1)
        main_frame.grid_rowconfigure(2, weight=1)
        
        # Celsius a Fahrenheit
        self.crear_conversor(
            main_frame,
            "Celsius a Fahrenheit",
            "°C",
            "°F",
            self.soap_client.celsius_a_fahrenheit,
            0
        )
        
        # Fahrenheit a Celsius
        self.crear_conversor(
            main_frame,
            "Fahrenheit a Celsius",
            "°F",
            "°C",
            self.soap_client.fahrenheit_a_celsius,
            1
        )
        
        # Celsius a Kelvin
        self.crear_conversor(
            main_frame,
            "Celsius a Kelvin",
            "°C",
            "K",
            self.soap_client.celsius_a_kelvin,
            2
        )
    
    def crear_tab_masa(self):
        """Crea la pestaña de conversiones de masa"""
        tab = tk.Frame(self.notebook, bg='#f5f5f5')
        self.notebook.add(tab, text='⚖️ Masa')
        
        # Container principal con grid layout
        container = tk.Frame(tab, bg='#f5f5f5')
        container.pack(expand=True, fill='both', padx=20, pady=20)
        
        # Configurar columnas del container
        container.grid_columnconfigure(0, weight=0)  # Imagen izquierda
        container.grid_columnconfigure(1, weight=1)  # Conversiones derecha
        container.grid_rowconfigure(0, weight=1)
        
        # Frame izquierdo para imagen - centrado verticalmente
        imagen_frame = tk.Frame(container, bg='#f5f5f5')
        imagen_frame.grid(row=0, column=0, sticky='ns', padx=(0, 15))
        
        # Cargar y mostrar imagen más pequeña
        ruta_imagen = os.path.join(os.path.dirname(__file__), "conten_pant.png")
        imagen_rect = self.crear_imagen_rectangular(ruta_imagen, 200, 350)
        
        if imagen_rect:
            self.imagen_masa_ref = imagen_rect
            label_img = tk.Label(imagen_frame, image=imagen_rect, bg='#f5f5f5')
            label_img.pack(expand=True, anchor='center')
        
        # Frame derecho para conversiones - centrado verticalmente
        main_frame = tk.Frame(container, bg='#f5f5f5')
        main_frame.grid(row=0, column=1, sticky='ns')
        main_frame.grid_rowconfigure(0, weight=1)
        main_frame.grid_rowconfigure(1, weight=1)
        main_frame.grid_rowconfigure(2, weight=1)
        
        # Toneladas a Kilogramos
        self.crear_conversor(
            main_frame,
            "Toneladas a Kilogramos",
            "t",
            "kg",
            self.soap_client.toneladas_a_kilogramos,
            0
        )
        
        # Kilogramos a Gramos
        self.crear_conversor(
            main_frame,
            "Kilogramos a Gramos",
            "kg",
            "g",
            self.soap_client.kilogramos_a_gramos,
            1
        )
        
        # Gramos a Miligramos
        self.crear_conversor(
            main_frame,
            "Gramos a Miligramos",
            "g",
            "mg",
            self.soap_client.gramos_a_miligramos,
            2
        )
    
    def crear_tab_longitud(self):
        """Crea la pestaña de conversiones de longitud"""
        tab = tk.Frame(self.notebook, bg='#f5f5f5')
        self.notebook.add(tab, text='📏 Longitud')
        
        # Container principal con grid layout
        container = tk.Frame(tab, bg='#f5f5f5')
        container.pack(expand=True, fill='both', padx=20, pady=20)
        
        # Configurar columnas del container
        container.grid_columnconfigure(0, weight=0)  # Imagen izquierda
        container.grid_columnconfigure(1, weight=1)  # Conversiones derecha
        container.grid_rowconfigure(0, weight=1)
        
        # Frame izquierdo para imagen - centrado verticalmente
        imagen_frame = tk.Frame(container, bg='#f5f5f5')
        imagen_frame.grid(row=0, column=0, sticky='ns', padx=(0, 15))
        
        # Cargar y mostrar imagen más pequeña
        ruta_imagen = os.path.join(os.path.dirname(__file__), "conten_pant.png")
        imagen_rect = self.crear_imagen_rectangular(ruta_imagen, 200, 350)
        
        if imagen_rect:
            self.imagen_long_ref = imagen_rect
            label_img = tk.Label(imagen_frame, image=imagen_rect, bg='#f5f5f5')
            label_img.pack(expand=True, anchor='center')
        
        # Frame derecho para conversiones - centrado verticalmente
        main_frame = tk.Frame(container, bg='#f5f5f5')
        main_frame.grid(row=0, column=1, sticky='ns')
        main_frame.grid_rowconfigure(0, weight=1)
        main_frame.grid_rowconfigure(1, weight=1)
        main_frame.grid_rowconfigure(2, weight=1)
        
        # Kilómetros a Metros
        self.crear_conversor(
            main_frame,
            "Kilómetros a Metros",
            "km",
            "m",
            self.soap_client.kilometros_a_metros,
            0
        )
        
        # Metros a Centímetros
        self.crear_conversor(
            main_frame,
            "Metros a Centímetros",
            "m",
            "cm",
            self.soap_client.metros_a_centimetros,
            1
        )
        
        # Centímetros a Milímetros
        self.crear_conversor(
            main_frame,
            "Centímetros a Milímetros",
            "cm",
            "mm",
            self.soap_client.centimetros_a_milimetros,
            2
        )
    
    def crear_conversor(self, parent, titulo, unidad_origen, unidad_destino, funcion_conversion, row):
        """Crea un widget de conversor individual"""
        # Frame contenedor
        frame = tk.LabelFrame(
            parent,
            text=titulo,
            font=("Arial", 11, "bold"),
            bg='white',
            fg='#333333',
            relief=tk.RAISED,
            borderwidth=2,
            padx=15,
            pady=15
        )
        frame.grid(row=row, column=0, sticky='ew', pady=10)
        parent.grid_columnconfigure(0, weight=1)
        
        # Frame interior
        inner_frame = tk.Frame(frame, bg='white')
        inner_frame.pack(fill='x')
        
        # Entrada
        entrada_frame = tk.Frame(inner_frame, bg='white')
        entrada_frame.pack(side='left', expand=True, fill='x')
        
        tk.Label(
            entrada_frame,
            text=f"Valor ({unidad_origen}):",
            font=("Arial", 10),
            bg='white'
        ).pack(side='left', padx=(0, 10))
        
        entry = tk.Entry(
            entrada_frame,
            font=("Arial", 10),
            width=12,
            relief=tk.SOLID,
            borderwidth=1
        )
        entry.pack(side='left')
        
        # Guardar referencia del campo de entrada
        self.campos_entrada.append(entry)
        
        # Botón convertir
        btn = tk.Button(
            inner_frame,
            text="➜ Convertir",
            font=("Arial", 10, "bold"),
            bg='#2196F3',
            fg='white',
            activebackground='#1976D2',
            activeforeground='white',
            cursor='hand2',
            relief=tk.FLAT,
            padx=20,
            command=lambda: self.realizar_conversion(entry, resultado_label, funcion_conversion, unidad_destino)
        )
        btn.pack(side='left', padx=20)
        
        # Resultado
        resultado_label = tk.Label(
            inner_frame,
            text="Resultado: --",
            font=("Arial", 11, "bold"),
            bg='white',
            fg='#4CAF50',
            width=30,
            anchor='w'
        )
        resultado_label.pack(side='left')
        
        # Guardar referencia del campo de resultado
        self.campos_resultado.append(resultado_label)
        
        # Bind Enter key
        entry.bind('<Return>', lambda e: self.realizar_conversion(entry, resultado_label, funcion_conversion, unidad_destino))
    
    def limpiar_campos(self):
        """Limpia todos los campos de entrada y resultados"""
        # Limpiar todos los campos de entrada
        for campo in self.campos_entrada:
            campo.delete(0, tk.END)
        
        # Resetear todos los campos de resultado
        for resultado in self.campos_resultado:
            resultado.config(text="Resultado: --")
        
        messagebox.showinfo("Campos Limpiados", "Todos los campos han sido limpiados correctamente")
    
    def cerrar_sesion(self):
        """Cierra la sesión actual y vuelve al login"""
        respuesta = messagebox.askyesno(
            "Cerrar Sesión",
            "¿Está seguro que desea cerrar la sesión?\n\nVolverá a la pantalla de login."
        )
        
        if respuesta:
            # Cerrar ventana actual
            self.root.destroy()
            
            # Crear nueva ventana de login
            root_login = tk.Tk()
            LoginWindow(root_login, self.soap_client)
            root_login.mainloop()
    
    def realizar_conversion(self, entry, resultado_label, funcion_conversion, unidad_destino):
        """Realiza la conversión usando el servicio SOAP"""
        try:
            valor = entry.get().strip()
            
            if not valor:
                messagebox.showwarning("Advertencia", "Por favor ingrese un valor")
                return
            
            # Convertir a float
            valor_float = float(valor)
            
            # Llamar al servicio SOAP
            resultado = funcion_conversion(valor_float)
            
            if resultado is not None:
                # Formatear con 4 decimales y unidad abreviada
                resultado_label.config(text=f"Resultado: {float(resultado):.4f} {unidad_destino}")
            else:
                resultado_label.config(text="Resultado: Error")
                
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese un número válido")
        except Exception as e:
            messagebox.showerror("Error", f"Error en la conversión:\n{str(e)}")


def main():
    """Función principal"""
    # URL del WSDL
    WSDL_URL = "http://localhost:8080/ConUni_Soap_Java_GR05/CONUNI?wsdl"
    
    # Crear cliente SOAP
    soap_client = SOAPClient(WSDL_URL)
    
    # Intentar conectar
    if not soap_client.conectar():
        return
    
    # Crear ventana de login
    root = tk.Tk()
    LoginWindow(root, soap_client)
    root.mainloop()


if __name__ == "__main__":
    main()
