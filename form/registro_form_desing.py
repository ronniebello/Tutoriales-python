import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import util.util_ventana as util_ventana
import styles.form_style as form_style


class FormularioRegistroDesing(tk.Tk):

    def __init__(self):
        super().__init__()
        self.config_window()
        self.crear_paneles()
        self.crear_controles()

    def config_window(self):
        self.title("Registro de productos")
        w, h = 800, 500
        util_ventana.centrar_ventana(self, w, h)
        self.config(bg=form_style.BACKGROUND_COLOR)

    def crear_paneles(self):
        self.marco_titulo = tk.Frame(
            self, bg="red", height=40
        )
        self.marco_titulo.pack(side=tk.TOP, fill="both")

        self.marco_registro = tk.Frame(
            self, bg="blue", height=50
        )
        self.marco_registro.pack(side=tk.TOP, fill="both", pady=10)

        self.marco_acciones = tk.Frame(
            self, bg="green", height=50
        )
        self.marco_acciones.pack(side=tk.TOP, fill="both")

        self.marco_productos = tk.Frame(
            self, bg="black"
        )
        self.marco_productos.pack(side=tk.TOP, fill="both",
                                  padx=30, pady=15, expand=True)

    def crear_controles(self):
        # titulo
        titulo = tk.Label(
            self.marco_titulo,
            text="Registro de productos",
            font=("Roboto", 20),
            fg="#485159",
            bg=form_style.BACKGROUND_COLOR_2,
            padx=20
        )
        titulo.pack(expand=True, fill=tk.BOTH)

        # etiqueta_id
        etiqueta_id = tk.Label(
            self.marco_registro,
            text="Id:",
            font=("Times", 14),
            fg=form_style.TEXT_COLOR,
            bg=form_style.BACKGROUND_COLOR,
            width=5
        )
        etiqueta_id.pack(side="left", padx=15, pady=10)

        # campo_id
        self.campo_id = tk.Entry(
            self.marco_registro,
            font=("Times", 14),
            state="readonly",
            width=5
        )
        self.campo_id.pack(side="left", padx=15, pady=10)

        # etiqueta_nombre
        etiqueta_nombre = tk.Label(
            self.marco_registro,
            text="Producto:",
            font=("Times", 14),
            fg=form_style.TEXT_COLOR,
            bg=form_style.BACKGROUND_COLOR,
            width=10
        )
        etiqueta_nombre.pack(side="left", padx=15, pady=10)

        # campo_nombre
        self.campo_nombre = tk.Entry(
            self.marco_registro,
            font=("Times", 14),
        )
        self.campo_nombre.pack(side="left", padx=15, pady=10)

        # etiqueta_precio
        etiqueta_precio = tk.Label(
            self.marco_registro,
            text="Precio:",
            font=("Times", 14),
            fg=form_style.TEXT_COLOR,
            bg=form_style.BACKGROUND_COLOR,
            width=5
        )
        etiqueta_precio.pack(side="left", padx=15, pady=10)

        # campo_precio
        self.campo_precio = tk.Entry(
            self.marco_registro,
            font=("Times", 14),
        )
        self.campo_precio.pack(side="left", padx=15, pady=10)

        # boton_registro
        self.btn_registro = tk.Button(
            self.marco_acciones,
            text="Registrar",
            font=("Times", 13),
            bg=form_style.BUTTON_REGISTRA_COLOR,
            bd=0,
            fg=form_style.BACKGROUND_COLOR,
            padx=15,
            command=self.registrar_producto
        )
        self.btn_registro.pack(**self.obtener_config_btn_pack())
        self.btn_registro.bind(
            "<Return>", (lambda event: self.registrar_producto()))

        # boton_eliminar
        self.btn_eliminar = tk.Button(
            self.marco_acciones,
            text="Eliminar",
            font=("Times", 13),
            bg=form_style.BUTTON_ELIMINA_COLOR,
            bd=0,
            fg=form_style.BACKGROUND_COLOR,
            padx=15,
            command=self.eliminar_producto
        )
        self.btn_eliminar.pack(**self.obtener_config_btn_pack())
        self.btn_eliminar.bind(
            "<Return>", (lambda event: self.eliminar_producto()))
        self.btn_eliminar.pack_forget()

        # Boton modificar
        self.btn_modificar = tk.Button(
            self.marco_acciones,
            text="Modificar",
            font=("Times", 13),
            bg=form_style.BUTTON_MODIFICAR_COLOR,
            bd=0,
            fg=form_style.BACKGROUND_COLOR,
            padx=15,
            command=self.modificar_producto
        )
        self.btn_modificar.pack(**self.obtener_config_btn_pack())
        self.btn_modificar.bind(
            "<Return>", (lambda event: self.modificar_producto()))
        self.btn_modificar.pack_forget()

        # Boton limpiar
        self.btn_limpiar_campos = tk.Button(
            self.marco_acciones,
            text="Limpiar Campo",
            font=("Times", 13),
            bg=form_style.BUTTON_LIMPIAR_COLOR,
            bd=0,
            padx=15,
            fg=form_style.BACKGROUND_COLOR,
            command=self.limpiar_campos
        )
        self.btn_limpiar_campos.pack(**self.obtener_config_btn_pack())
        self.btn_limpiar_campos.bind(
            "<Return>", (lambda event: self.limpiar_campos()))

        # Tabla
        style = ttk.Style(self)
        style.theme_use("clam")  # set theam to clam
        style.configure("Treeview.Heading",
                        background="#6f9a8d", foreground="#ffffff")

        tree_scroll = tk.Scrollbar(self.marco_productos)
        tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)

        self.tree = ttk.Treeview(self.marco_productos,
                                 show="headings", yscrollcommand=tree_scroll.set)

        self.tree["columns"] = ("Id", "Nombre", "Precio")
        self.tree.column("#0")
        self.tree.column("Id")
        self.tree.column("Nombre")
        self.tree.column("Precio")

        self.tree.heading("#0", text="")
        self.tree.heading("Id", text="Id")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Precio", text="Precio")

        self.tree.pack(expand=True, fill="both")
        self.tree.bind("<<TreeviewSelect>>", self.al_selecionar_treeview)

        self.tree.tag_configure("oddrow", background="#ffffe0")
        self.tree.tag_configure("evenrow", background="#eafbea")

        # actualizar lista
        self.actualizar_lista()

    def actualizar_lista(self):
        pass

    def al_selecionar_treeview(self, event):
        pass

    def limpiar_campos(self):
        pass

    def modificar_producto(self):
        pass

    def registrar_producto(self):
        pass

    def eliminar_producto(self):
        pass

    def obtener_config_btn_pack(self):
        return {
            "side": tk.RIGHT,
            "padx": 10,
            "pady": 10
        }

    def limpiar_campos(self):
        try:
            self.campo_nombre.delete(0, "end")
            self.campo_precio.delete(0, "end")
            self.campo_id.delete(0, "end")
            self.campo_id.config(state="readonly")
            self.btn_registro.pack(**self.obtener_config_btn_pack())
            self.btn_eliminar.pack_forget()
            self.btn_modificar.pack_forget()
        except Exception as e:
            messagebox.showerror("Error", f"Error en la limpieza: {e}")
