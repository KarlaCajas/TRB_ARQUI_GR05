"""
Ventana Principal - Calculadora de Conversión de Unidades
"""
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from api_client import APIClient
import os


class MainWindow:
    """Ventana principal - Calculadora de conversiones"""
    
    def __init__(self, usuario: str):
        self.usuario = usuario
        self.api_client = APIClient()
        self.cerrar_sesion_activado = False
        
        self.root = tk.Tk()
        self.root.title(f"Calculadora de Conversión de Unidades - Usuario: {usuario}")
        self.root.geometry("650x680")
        self.root.resizable(False, False)
        
        # Configurar el evento de cierre de ventana
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        # Centrar ventana
        self.center_window()
        
        # Verificar conexión con el servidor
        self.servidor_disponible = self.api_client.verificar_conexion()
        
        # Definir conversiones disponibles
        self.conversiones = {
            "Temperatura": {
                "Celsius a Fahrenheit": self.celsius_a_fahrenheit,
                "Fahrenheit a Celsius": self.fahrenheit_a_celsius,
                "Celsius a Kelvin": self.celsius_a_kelvin
            },
            "Masa": {
                "Kilogramos a Gramos": self.kg_a_gramos,
                "Gramos a Miligramos": self.gramos_a_miligramos,
                "Toneladas a Kilogramos": self.toneladas_a_kg
            },
            "Longitud": {
                "Kilómetros a Metros": self.km_a_metros,
                "Metros a Centímetros": self.metros_a_cm,
                "Centímetros a Milímetros": self.cm_a_mm
            }
        }
        
        # Crear interfaz
        self.crear_interfaz()
        
        # Mostrar estado de conexión (solo informativo)
        if self.servidor_disponible:
            self.actualizar_estado_conexion("✅ Servidor disponible", "success")
        else:
            self.actualizar_estado_conexion("⚠️ Servidor no disponible", "warning")
        
    def center_window(self):
        """Centra la ventana en la pantalla"""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
    
    def crear_interfaz(self):
        """Crea la interfaz principal"""
        # Intentar cargar imagen de fondo
        try:
            fondo_path = os.path.join(os.path.dirname(__file__), "fondoes.jpg")
            imagen_fondo = Image.open(fondo_path)
            imagen_fondo = imagen_fondo.resize((650, 680), Image.Resampling.LANCZOS)
            self.bg_image = ImageTk.PhotoImage(imagen_fondo)
            
            # Label de fondo
            bg_label = tk.Label(self.root, image=self.bg_image)
            bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        except Exception as e:
            print(f"No se pudo cargar imagen de fondo: {e}")
            self.root.configure(bg="#f0f0f0")
        
        # Frame superior con título y usuario
        header_frame = tk.Frame(self.root, bg="#1976D2", height=60)
        header_frame.pack(fill="x")
        header_frame.pack_propagate(False)
        
        tk.Label(
            header_frame,
            text="🔄 Calculadora de Conversión de Unidades",
            font=("Segoe UI", 15, "bold"),
            bg="#1976D2",
            fg="white"
        ).pack(side="left", padx=20, pady=10)
        
        # Frame para usuario y botón cerrar sesión
        user_frame = tk.Frame(header_frame, bg="#1976D2")
        user_frame.pack(side="right", padx=20, pady=10)
        
        tk.Label(
            user_frame,
            text=f"👤 {self.usuario}",
            font=("Segoe UI", 11, "bold"),
            bg="#1976D2",
            fg="white"
        ).pack(side="left", padx=(0, 10))
        
        # Botón de cerrar sesión - solo icono
        btn_logout = tk.Button(
            user_frame,
            text="⎋",  # Símbolo de salida/escape
            font=("Segoe UI", 16, "bold"),
            bg="#455A64",
            fg="white",
            activebackground="#37474F",
            activeforeground="white",
            relief="raised",
            cursor="hand2",
            borderwidth=1,
            width=2,
            height=1,
            command=self.cerrar_sesion
        )
        btn_logout.pack(side="left")
        
        # Agregar tooltip al pasar el mouse
        def mostrar_tooltip(event):
            btn_logout.config(bg="#37474F")
        
        def ocultar_tooltip(event):
            btn_logout.config(bg="#455A64")
        
        btn_logout.bind("<Enter>", mostrar_tooltip)
        btn_logout.bind("<Leave>", ocultar_tooltip)
        
        # Frame principal con fondo blanco semi-transparente (NO expand para dejar espacio)
        main_frame = tk.Frame(self.root, bg="white", relief="raised", borderwidth=2)
        main_frame.pack(fill="x", padx=25, pady=(20, 10))
        
        # Título de sección con fondo azul
        titulo_frame = tk.Frame(main_frame, bg="#64B5F6", relief="solid", borderwidth=1)
        titulo_frame.pack(fill="x", padx=15, pady=(15, 10))
        
        tk.Label(
            titulo_frame,
            text="Selecciona el tipo de conversión",
            font=("Segoe UI", 13, "bold"),
            bg="#64B5F6",
            fg="white",
            pady=8
        ).pack()
        
        # Frame para selección de categoría con fondo blanco
        categoria_frame = tk.Frame(main_frame, bg="white")
        categoria_frame.pack(pady=12, fill="x", padx=15)
        
        tk.Label(
            categoria_frame,
            text="Categoría:",
            font=("Segoe UI", 11, "bold"),
            bg="white",
            fg="#1565C0",
            width=12,
            anchor="w"
        ).pack(side="left")
        
        self.combo_categoria = ttk.Combobox(
            categoria_frame,
            values=list(self.conversiones.keys()),
            state="readonly",
            font=("Segoe UI", 11),
            width=30
        )
        self.combo_categoria.pack(side="left", padx=5)
        self.combo_categoria.bind("<<ComboboxSelected>>", self.on_categoria_change)
        
        # Frame para selección de conversión específica
        conversion_frame = tk.Frame(main_frame, bg="white")
        conversion_frame.pack(pady=12, fill="x", padx=15)
        
        tk.Label(
            conversion_frame,
            text="Conversión:",
            font=("Segoe UI", 11, "bold"),
            bg="white",
            fg="#1565C0",
            width=12,
            anchor="w"
        ).pack(side="left")
        
        self.combo_conversion = ttk.Combobox(
            conversion_frame,
            state="readonly",
            font=("Segoe UI", 11),
            width=30
        )
        self.combo_conversion.pack(side="left", padx=5)
        
        # Línea separadora azul
        tk.Frame(main_frame, height=3, bg="#42A5F5").pack(fill="x", pady=15, padx=15)
        
        # Frame para entrada de valor con fondo blanco
        valor_frame = tk.Frame(main_frame, bg="white")
        valor_frame.pack(pady=12, fill="x", padx=15)
        
        tk.Label(
            valor_frame,
            text="Valor a convertir:",
            font=("Segoe UI", 11, "bold"),
            bg="white",
            fg="#1565C0",
            width=15,
            anchor="w"
        ).pack(side="left")
        
        self.entry_valor = tk.Entry(
            valor_frame,
            font=("Segoe UI", 12),
            width=20,
            relief="solid",
            borderwidth=2
        )
        self.entry_valor.pack(side="left", padx=5, ipady=3)
        self.entry_valor.bind("<Return>", lambda e: self.convertir())
        
        # Frame para botones de acción (Convertir y Limpiar)
        botones_accion_frame = tk.Frame(main_frame, bg="white")
        botones_accion_frame.pack(pady=15, padx=15)
        
        # Botón de convertir - azul grande
        self.btn_convertir = tk.Button(
            botones_accion_frame,
            text="🔄 CONVERTIR",
            font=("Segoe UI", 13, "bold"),
            bg="#1976D2",
            fg="white",
            activebackground="#1565C0",
            activeforeground="white",
            width=20,
            height=2,
            relief="raised",
            cursor="hand2",
            borderwidth=3,
            command=self.convertir
        )
        self.btn_convertir.pack(side="left", padx=5)
        
        # Botón de limpiar junto al convertir
        self.btn_limpiar = tk.Button(
            botones_accion_frame,
            text="🗑️ LIMPIAR",
            font=("Segoe UI", 13, "bold"),
            bg="#FF9800",
            fg="white",
            activebackground="#F57C00",
            activeforeground="white",
            width=20,
            height=2,
            relief="raised",
            cursor="hand2",
            borderwidth=3,
            command=self.limpiar
        )
        self.btn_limpiar.pack(side="left", padx=5)
        
        # Frame para resultado con fondo verde claro y borde
        resultado_frame = tk.Frame(main_frame, bg="#C8E6C9", relief="solid", borderwidth=3)
        resultado_frame.pack(pady=12, fill="x", padx=15)
        
        tk.Label(
            resultado_frame,
            text="✅ Resultado:",
            font=("Segoe UI", 12, "bold"),
            bg="#C8E6C9",
            fg="#2E7D32"
        ).pack(pady=(12, 5))
        
        self.lbl_resultado = tk.Label(
            resultado_frame,
            text="---",
            font=("Segoe UI", 18, "bold"),
            bg="#C8E6C9",
            fg="#1B5E20"
        )
        self.lbl_resultado.pack(pady=(5, 12))
        
        # Frame inferior solo para estado de conexión - más pequeño
        bottom_frame = tk.Frame(self.root, bg="white", relief="raised", borderwidth=2, height=50)
        bottom_frame.pack(fill="x", padx=25, pady=(10, 20))
        bottom_frame.pack_propagate(False)
        
        # Frame para estado de conexión centrado
        estado_frame = tk.Frame(bottom_frame, bg="white")
        estado_frame.pack(expand=True)
        
        self.lbl_estado_conexion = tk.Label(
            estado_frame,
            text="Verificando conexión...",
            font=("Segoe UI", 11, "bold"),
            bg="white",
            fg="#666666"
        )
        self.lbl_estado_conexion.pack()
        
        # Actualizar estado de conexión inicial
        if self.servidor_disponible:
            self.actualizar_estado_conexion("✅ Servidor disponible", "success")
        else:
            self.actualizar_estado_conexion("⚠️ Servidor no disponible", "warning")
    
    def on_categoria_change(self, event):
        """Actualiza las conversiones disponibles según la categoría seleccionada"""
        categoria = self.combo_categoria.get()
        if categoria:
            conversiones_disponibles = list(self.conversiones[categoria].keys())
            self.combo_conversion.config(values=conversiones_disponibles)
            self.combo_conversion.set("")
            self.lbl_resultado.config(text="---")
            self.entry_valor.delete(0, tk.END)
            self.entry_valor.focus()
    
    def actualizar_estado_conexion(self, mensaje: str, tipo: str = "info"):
        """Actualiza el mensaje de estado de conexión"""
        colores = {
            "info": "#2196F3",
            "success": "#4CAF50",
            "error": "#f44336",
            "warning": "#FF9800"
        }
        
        self.lbl_estado_conexion.config(
            text=mensaje,
            fg=colores.get(tipo, "#666666")
        )
    
    def guardar_en_servidor(self, categoria: str, conversion: str, valor_entrada: float, resultado_texto: str):
        """Guarda la conversión realizada en el servidor REST"""
        if not self.servidor_disponible:
            return  # No intentar guardar si el servidor no está disponible
        
        try:
            # Extraer unidades y valor del resultado
            partes = conversion.split(" a ")
            unidad_origen = partes[0].split()[-1] if len(partes) > 0 else ""
            unidad_destino = partes[1] if len(partes) > 1 else ""
            
            # Calcular el factor de conversión
            # Extraer el valor numérico del resultado
            resultado_partes = resultado_texto.split(" = ")
            if len(resultado_partes) > 1:
                valor_resultado = float(resultado_partes[1].split()[0])
                factor = valor_resultado / valor_entrada if valor_entrada != 0 else 0
            else:
                factor = 1
            
            # Preparar datos para enviar
            datos = {
                "tipoConversion": f"{categoria} - {conversion}",
                "unidadOrigen": unidad_origen,
                "unidadDestino": unidad_destino,
                "factorConversion": factor,
                "descripcion": f"Conversión realizada por {self.usuario}: {resultado_texto}"
            }
            
            # Enviar al servidor
            resultado_api = self.api_client.crear_conversion(datos)
            
            if resultado_api["success"]:
                self.actualizar_estado_conexion("✅ Guardado en servidor", "success")
            else:
                self.actualizar_estado_conexion("⚠️ No se pudo guardar", "warning")
                
        except Exception as e:
            print(f"Error al guardar en servidor: {e}")
            self.actualizar_estado_conexion("⚠️ Error al guardar", "warning")
    
    def convertir(self):
        """Realiza la conversión seleccionada"""
        # Validar que se haya seleccionado una categoría
        if not self.combo_categoria.get():
            messagebox.showwarning("Selección requerida", "Por favor, seleccione una categoría")
            self.combo_categoria.focus()
            return
        
        # Validar que se haya seleccionado una conversión
        if not self.combo_conversion.get():
            messagebox.showwarning("Selección requerida", "Por favor, seleccione un tipo de conversión")
            self.combo_conversion.focus()
            return
        
        # Validar que se haya ingresado un valor
        valor_texto = self.entry_valor.get().strip()
        if not valor_texto:
            messagebox.showwarning("Valor requerido", "Por favor, ingrese un valor a convertir")
            self.entry_valor.focus()
            return
        
        # Validar que el valor sea numérico
        try:
            valor = float(valor_texto)
        except ValueError:
            messagebox.showerror("Valor inválido", "Por favor, ingrese un número válido")
            self.entry_valor.focus()
            return
        
        # Obtener la función de conversión
        categoria = self.combo_categoria.get()
        conversion = self.combo_conversion.get()
        funcion_conversion = self.conversiones[categoria][conversion]
        
        # Realizar la conversión
        resultado = funcion_conversion(valor)
        
        # Mostrar resultado
        self.lbl_resultado.config(text=resultado)
        
        # NO guardar en el servidor - Solo cálculo local
        # self.guardar_en_servidor(categoria, conversion, valor, resultado)
    
    def limpiar(self):
        """Limpia todos los campos"""
        self.combo_categoria.set("")
        self.combo_conversion.set("")
        self.combo_conversion.config(values=[])
        self.entry_valor.delete(0, tk.END)
        self.lbl_resultado.config(text="---")
        self.combo_categoria.focus()
        
        # Verificar conexión nuevamente (solo informativo)
        self.servidor_disponible = self.api_client.verificar_conexion()
        if self.servidor_disponible:
            self.actualizar_estado_conexion("✅ Servidor disponible", "success")
        else:
            self.actualizar_estado_conexion("⚠️ Servidor no disponible", "warning")
    
    def cerrar_sesion(self):
        """Cierra la sesión actual y vuelve al login"""
        confirmacion = messagebox.askyesno(
            "Cerrar Sesión",
            f"¿Desea cerrar la sesión de {self.usuario}?"
        )
        
        if confirmacion:
            self.cerrar_sesion_activado = True
            self.root.destroy()
    
    def on_closing(self):
        """Maneja el evento de cierre de la ventana"""
        confirmacion = messagebox.askyesno(
            "Salir",
            "¿Desea salir de la aplicación?"
        )
        
        if confirmacion:
            self.root.destroy()
    
    # ========== CONVERSIONES DE TEMPERATURA ==========
    
    def celsius_a_fahrenheit(self, celsius):
        """Convierte Celsius a Fahrenheit"""
        fahrenheit = (celsius * 9/5) + 32
        return f"{celsius} °C = {fahrenheit:.4f} grados Fahrenheit"
    
    def fahrenheit_a_celsius(self, fahrenheit):
        """Convierte Fahrenheit a Celsius"""
        celsius = (fahrenheit - 32) * 5/9
        return f"{fahrenheit} °F = {celsius:.4f} grados Celsius"
    
    def celsius_a_kelvin(self, celsius):
        """Convierte Celsius a Kelvin"""
        kelvin = celsius + 273.15
        return f"{celsius} °C = {kelvin:.4f} Kelvin"
    
    # ========== CONVERSIONES DE MASA ==========
    
    def kg_a_gramos(self, kg):
        """Convierte Kilogramos a Gramos"""
        gramos = kg * 1000
        return f"{kg} kg = {gramos:.4f} gramos"
    
    def gramos_a_miligramos(self, gramos):
        """Convierte Gramos a Miligramos"""
        miligramos = gramos * 1000
        return f"{gramos} g = {miligramos:.4f} miligramos"
    
    def toneladas_a_kg(self, toneladas):
        """Convierte Toneladas a Kilogramos"""
        kg = toneladas * 1000
        return f"{toneladas} t = {kg:.4f} kilogramos"
    
    # ========== CONVERSIONES DE LONGITUD ==========
    
    def km_a_metros(self, km):
        """Convierte Kilómetros a Metros"""
        metros = km * 1000
        return f"{km} km = {metros:.4f} metros"
    
    def metros_a_cm(self, metros):
        """Convierte Metros a Centímetros"""
        cm = metros * 100
        return f"{metros} m = {cm:.4f} centímetros"
    
    def cm_a_mm(self, cm):
        """Convierte Centímetros a Milímetros"""
        mm = cm * 10
        return f"{cm} cm = {mm:.4f} milímetros"
    
    def ejecutar(self):
        """Ejecuta el loop principal de la ventana"""
        self.root.mainloop()
        return self.cerrar_sesion_activado


if __name__ == "__main__":
    app = MainWindow("MONSTER")
    app.ejecutar()
