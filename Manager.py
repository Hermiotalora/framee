
from inspect import Attribute
import tkinter as tk
from gui_app import ventana, otraVentana


class Manager(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("pagina principal")
        #self.attributes("-fullscreen", True)
        container = tk.Frame(self)  # contiene todos los frame
        container.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        container.grid_columnconfigure(0, weight=1)  # weight peso
        # hago un cuadrado donde va a contener todo
        container.grid_rowconfigure(0, weight=1)

        self.frames = {}
        for F in (ventana, otraVentana):
            # container es el parent,app Manager, controlller nuestros self, incrusatrar cada frame en el frame manager
            frame = F(container, self)
            self.frames[F] = frame  # guardo cada screen en el dict
            frame.grid(row=0, column=0, sticky=tk.NSEW)
        self.show_frame(ventana)

    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()
