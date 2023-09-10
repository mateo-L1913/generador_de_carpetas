# Prototipo 1 - creador de carpetas multiples - 1.1 #

import tkinter as tk
from tkinter import ttk
from tkinter import font
import os
from tkinter import filedialog

def agregar_elemento(event=None):
    elemento = folder_entry.get()
    folder_listbox.insert(tk.END, elemento)
    folder_entry.delete(0, tk.END)

def borrar_elemento():
    indice_seleccionado = folder_listbox.curselection()
    if indice_seleccionado:
        for index in reversed(indice_seleccionado):
            folder_listbox.delete(index)

def guardar_nombres():
    ruta_destino = ruta_entry.get()
    if not ruta_destino:
        print("No se seleccionó una ruta de destino.")
        return
    
    nombres_seleccionados = folder_listbox.get(0, tk.END)
    nombres_guardados = [nombre.strip() for nombre in nombres_seleccionados if nombre.strip()]
    
    try:
        for nombre in nombres_guardados:
            nueva_ruta = os.path.join(ruta_destino, nombre)
            os.makedirs(nueva_ruta)
            ruta_entry.delete(0, tk.END)
            folder_listbox.delete(0, tk.END)
            print("Carpeta creada en:", nueva_ruta)
    except OSError as e:
        print("Error al crear las carpetas:", e)

window_main = tk.Tk()
window_main.title("Generador de carpetas multiples")
window_main.configure(bg="gray36")

# Obtener dimensiones de la pantalla
screen_width = window_main.winfo_screenwidth()
screen_height = window_main.winfo_screenheight()

# Establecer la geometría de la ventana para que llene la pantalla
window_main.geometry(f"{screen_width}x{screen_height}")

font_title = font.Font(family="helvatica", size=15, weight="bold")
font_regular = font.Font(family="helvatica", size=14, weight="normal")
font_boton = font.Font(family="helvatica", size=12, weight="bold") 

estilo = ttk.Style()
estilo.configure("NuevoEstilo.TButton", background="gold3", foreground="black", font=font_title)
estilo.configure("ruta.TButton", background="royal blue", foreground="black", font=font_boton)
estilo.configure("folder.TButton", background="red2", foreground="black", font=font_boton)
estilo.configure("folder2.TButton", background="green4", foreground="black", font=font_boton)

label_ruta = tk.Label(window_main, text="Ruta deseada:", font=font_title, bg="gray36", fg="ghost white")
label_ruta.place(x=420,y=60)
ruta_entry = ttk.Entry(window_main, width=45, font=font_regular)
ruta_entry.place(x=420, y=100)

label_folder = tk.Label(window_main, text="Nombre de carpeta:", font=font_title, bg="gray36", fg="ghost white")
label_folder.place(x=600,y=160)
folder_listbox = tk.Listbox(window_main, width=45, height=15, font=font_boton, selectmode=tk.MULTIPLE)
folder_listbox.place(x=485,y=200)

folder_entry = ttk.Entry(window_main, width=37, font=font_regular)
folder_entry.place(x=485,y=520)

btn_agregar = ttk.Button(window_main, text="Agregar", command=agregar_elemento, style="folder2.TButton")
btn_agregar.place(x=550,y=575)
folder_entry.bind('<Return>', agregar_elemento)

btn_borrar = ttk.Button(window_main, text="Borrar", command=borrar_elemento, style="folder.TButton")
btn_borrar.place(x=720,y=575)

boton_seleccionar_ruta = ttk.Button(window_main, text="Seleccionar Ruta", command=lambda: ruta_entry.insert(0, filedialog.askdirectory()), style="ruta.TButton")
boton_seleccionar_ruta.place(x=930, y=100)

boton_generar = ttk.Button(window_main, text="Generar Carpetas", command=guardar_nombres, style="NuevoEstilo.TButton")
boton_generar.place(x=600, y=640)

window_main.mainloop() 
