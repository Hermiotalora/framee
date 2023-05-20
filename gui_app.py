import sys
import tkinter as tk
from tkinter import ttk


# Primera parte

class ventana(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller
        self.paginaPrincipal()

    def paginaPrincipal(self):
        self.bg = tk.PhotoImage(file="img/1.png")
        fondo = tk.Label(self, image=self.bg).place(x=0, y=0)
        self.boton_nuevo = tk.Button(
            self, text="Ingresar")
        self.boton_nuevo.config(font=('Times New Roman', 12, 'bold'),
                                fg='black', bg='grey', cursor='hand2', activebackground='gray63', command=self.ejecutoFrames)
        self.boton_nuevo.place(relx=0.7, rely=0.5, relwidth=0.1, relheight=0.1)

        self.boton_salir = tk.Button(
            self, text="Salir")
        self.boton_salir.config(font=('Times New Roman', 12, 'bold'),
                                fg='black', bg='grey', cursor='hand2', activebackground='gray63', command=self.salir)
        self.boton_salir.place(relx=0.7, rely=0.7, relwidth=0.1, relheight=0.1)

# funcion salir
    def salir(self):
        sys.exit()


# funcion que ejecuta todos los frame


    def ejecutoFrames(self):
        self.frameAlta()
        self.frameBaja()
        self.frameModificar()
        self.frameEliminar()


# frame alta


    def frameAlta(self):
        self.alta = tk.Frame(self, bg="black")
        self.boton_nuevo = tk.Button(self.alta, text="Alta")

        self.boton_nuevo.config(font=('Times New Roman', 12, 'bold'),
                                fg='black', bg='white', cursor='hand2', activebackground='gray63', command=self.alta.destroy)
        self.boton_nuevo.place(relx=0.3, rely=0.5, relwidth=0.4, relheight=0.1)
        self.alta.place(relx=0, rely=0, relwidth=0.25, relheight=1)

# frame baja

#     def frameBaja(self):
#         self.baja = tk.Frame(self, bg="green")
#         self.boton_nuevo = tk.Button(
#             self.baja, text="Baja")
#         self.boton_nuevo.config(font=('Times New Roman', 12, 'bold'),
#                                 fg='black', bg='white', cursor='hand2', activebackground='gray63', command=self.baja.destroy)
#         self.boton_nuevo.place(relx=0.3, rely=0.5, relwidth=0.4, relheight=0.1)
#         self.baja.place(relx=0.26, rely=0, relwidth=0.25, relheight=1)
# # frame modificacion

#     def frameModificar(self):
#         self.modificar = tk.Frame(self, bg="violet")
#         self.boton_nuevo = tk.Button(
#             self.modificar, text="modificacion")
#         self.boton_nuevo.config(font=('Times New Roman', 12, 'bold'),
#                                 fg='black', bg='white', cursor='hand2', activebackground='gray63', command=self.modificar.destroy)
#         self.boton_nuevo.place(relx=0.3, rely=0.5, relwidth=0.4, relheight=0.1)
#         self.modificar.place(relx=0.52, rely=0, relwidth=0.25, relheight=1)

# # frame eliminacion
#     def frameEliminar(self):
#         self.eliminar = tk.Frame(self, bg="red")
#         self.boton_nuevo = tk.Button(
#             self.eliminar, text="Eliminar")
#         self.boton_nuevo.config(font=('Times New Roman', 12, 'bold'),
#                                 fg='black', bg='white', cursor='hand2', activebackground='gray63', command=self.eliminar.destroy)
#         self.boton_nuevo.place(relx=0.3, rely=0.5, relwidth=0.4, relheight=0.1)
#         self.eliminar.place(relx=0.78, rely=0, relwidth=0.25, relheight=1)


class otraVentana(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller
        self.otraPagina()

    def otraPagina(self):
        pass  # aca declaras otras ventanas perteneciente a otra clase


    def campos_pelicula(self):
        self.label_nombre = tk.Label(self, text='Nombre:')
        self.label_nombre.config(font=('Times New Roman', 12))
        self.label_nombre.grid(row=0, column=0, padx=15, pady=10)

        self.label_puntacion = tk.Label(self, text='Puntuación:')
        self.label_puntacion.config(font=('Times New Roman', 12))
        self.label_puntacion.grid(row=1, column=0, padx=15, pady=10)

        self.label_genero = tk.Label(self, text='Género:')
        self.label_genero.config(font=('Times New Roman', 12))
        self.label_genero.grid(row=2, column=0, padx=15, pady=10)


# entrys de cada campo
        self.mi_nombre = tk.StringVar()
        self.entry_nombre = tk.Entry(self, textvariable=self.mi_nombre)
        self.entry_nombre.config(width=50, font=('Times New Roman', 12))
        self.entry_nombre.grid(row=0, column=1, padx=10, pady=10)

        self.mi_puntacion = tk.StringVar()
        self.entry_puntacion = tk.Entry(self, textvariable=self.mi_puntacion)
        self.entry_puntacion.config(width=50, font=('Times New Roman', 12))
        self.entry_puntacion.grid(row=1, column=1, padx=10, pady=10)

        self.mi_genero = tk.StringVar()
        self.entry_genero = tk.Entry(self, textvariable=self.mi_genero)
        self.entry_genero.config(width=50, font=('Times New Roman', 12))
        self.entry_genero.grid(row=2, column=1, padx=10, pady=10)


# botones nuevo

        self.boton_nuevo = tk.Button(
            self, text="Nuevo", command=self.ejecutoFrames)
        self.boton_nuevo.config(width=20, font=('Times New Roman', 12, 'bold'),
                                fg='black', bg='white', cursor='hand2', activebackground='gray63')
        self.boton_nuevo.grid(row=3, column=1, padx=10, pady=10)

# botones guardar

        self.boton_guardar = tk.Button(
            self, text="Guardar", command=self.guardar_datos)
        self.boton_guardar.config(width=20, font=('Times New Roman', 12, 'bold'),
                                  fg='#DAD5D6', bg='#666666', cursor='hand2', activebackground='gray63')
        self.boton_guardar.grid(row=4, column=2, padx=10, pady=10)

# botones cancelar

        self.boton_cancelar = tk.Button(
            self, text="Cancelar", command=self.desabilitar_campos)
        self.boton_cancelar.config(width=20, font=('Times New Roman', 12, 'bold'),
                                   fg='#DAD5D6', bg='red', cursor='hand2', activebackground='gray63')
        self.boton_cancelar.grid(row=5, column=3, padx=10, pady=10)

    def habilitar_campos(self):

        self.mi_nombre.set('')
        self.mi_puntacion.set('')
        self.mi_genero.set('')

        self.entry_nombre.config(state='normal')
        self.entry_puntacion.config(state='normal')
        self.entry_genero.config(state='normal')

        self.boton_guardar.config(state='normal')
        self.boton_cancelar.config(state='normal')

    def desabilitar_campos(self):

        self.mi_nombre.set('')
        self.mi_puntacion.set('')
        self.mi_genero.set('')

        self.entry_nombre.config(state='disabled')
        self.entry_puntacion.config(state='disabled')
        self.entry_genero.config(state='disabled')

        self.boton_guardar.config(state='disabled')
        self.boton_cancelar.config(state='disabled')

    def guardar_datos(self):

        self.desabilitar_campos()


