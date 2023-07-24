### Programa para gestionar una Biblioteca de Libros ###
### Almacenando los Datos en un Archivo CSV ###


# Importacion de Librerias
from tkinter import *
from tkinter import ttk, messagebox
import tkinter as tk
import csv


def agregar_libro():
    nombre = entry_nombre.get()
    autor = entry_autor.get()
    genero = entry_genero.get()
    año = entry_año.get()
    if nombre and autor and genero and año:
        with open('biblioteca.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([nombre, autor, genero, año])
        entry_nombre.delete(0, END)
        entry_autor.delete(0, END)
        entry_genero.delete(0, END)
        entry_año.delete(0, END)
        mostrar_libros()
    else:
        messagebox.showerror("Error", "Por favor, completa todos los campos.")
    
def mostrar_libros():
    tree.delete(*tree.get_children())

    with open('biblioteca.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            tree.insert('', 'end', values=row)



def borrar_libro():
    selected_item = tree.selection()
    if selected_item:
        for item in selected_item:
            libro = tree.item(item)['values']
            with open('biblioteca.csv', 'r') as file:
                reader = csv.reader(file)
                libros = list(reader)
            with open('biblioteca.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                for row in libros:
                    if row != libro:
                        writer.writerow(row)
        mostrar_libros()
 
def editar_libro():
    selected_item = tree.selection()
    if selected_item:
        for item in selected_item:
            libro = tree.item(item)['values']
            ventana_editar = Toplevel(ventana)
            ventana_editar.title("Editar Libro")
            ventana_editar.geometry("200x180")
             # Crear etiquetas y campos de entrada para editar los datos del libro
            label_nombre_editar = Label(ventana_editar, text="Nombre:")
            label_nombre_editar.grid(row=0, column=0)
            entry_nombre_editar = Entry(ventana_editar)
            entry_nombre_editar.grid(row=0, column=1)
            entry_nombre_editar.insert(0, libro[0])
            label_autor_editar = Label(ventana_editar, text="Autor:")
            label_autor_editar.grid(row=1, column=0)
            entry_autor_editar = Entry(ventana_editar)
            entry_autor_editar.grid(row=1, column=1)
            entry_autor_editar.insert(0, libro[1])
            label_genero_editar = Label(ventana_editar, text="Género:")
            label_genero_editar.grid(row=2, column=0)
            entry_genero_editar = Entry(ventana_editar)
            entry_genero_editar.grid(row=2, column=1)
            entry_genero_editar.insert(0, libro[2])
            label_año_editar = Label(ventana_editar, text="Año:")
            label_año_editar.grid(row=3, column=0)
            entry_año_editar = Entry(ventana_editar)
            entry_año_editar.grid(row=3, column=1)
            entry_año_editar.insert(0, libro[3])
             # Función para guardar los cambios realizados en el libro
            def guardar_cambios():
                nuevo_nombre = entry_nombre_editar.get()
                nuevo_autor = entry_autor_editar.get()
                nuevo_genero = entry_genero_editar.get()
                nuevo_año = entry_año_editar.get()
                if nuevo_nombre and nuevo_autor and nuevo_genero and nuevo_año:
                    with open('biblioteca.csv', 'r') as file:
                        reader = csv.reader(file)
                        libros = list(reader)
                    with open('biblioteca.csv', 'w', newline='') as file:
                        writer = csv.writer(file)
                        for row in libros:
                            if row == libro:
                                writer.writerow([nuevo_nombre, nuevo_autor, nuevo_genero, nuevo_año])
                            else:
                                writer.writerow(row)
                    ventana_editar.destroy()
                    mostrar_libros()
                else:
                    messagebox.showerror("Error", "Por favor, completa todos los campos.")
             # Botón para guardar los cambios
            boton_guardar = Button(ventana_editar, text="Guardar Cambios", command=guardar_cambios)
            boton_guardar.grid(row=4, columnspan=2, padx=10, pady=10)
 
 
 
 
# Crear ventana
ventana = Tk()
ventana.title("Gestión de Biblioteca")
s = ttk.Style()
s.theme_use('clam')


# Configure the style of Heading in Treeview widget
s.configure('Treeview.Heading', background="green3")

# Crear etiquetas y campos de entrada
label_nombre = Label(ventana, text="Nombre:")
label_nombre.grid(row=0, column=0)
entry_nombre = Entry(ventana)
entry_nombre.grid(row=0, column=1)
label_autor = Label(ventana, text="Autor:")
label_autor.grid(row=1, column=0)
entry_autor = Entry(ventana)
entry_autor.grid(row=1, column=1)
label_genero = Label(ventana, text="Género:")
label_genero.grid(row=2, column=0)
entry_genero = Entry(ventana)
entry_genero.grid(row=2, column=1)
label_año = Label(ventana, text="Año:")
label_año.grid(row=3, column=0)
entry_año = Entry(ventana)
entry_año.grid(row=3, column=1)

# Crear botones
boton_agregar = Button(ventana, text="Agregar Libro", command=agregar_libro)
boton_agregar.grid(row=4, column=0, padx=10, pady=10)
boton_borrar = Button(ventana, text="Borrar Libro", command=borrar_libro)
boton_borrar.grid(row=4, column=1, padx=10, pady=10)

# Posicionar el boton editar debajo del TreeView
boton_editar = Button(ventana, text="Editar Libro", command=editar_libro)
boton_editar.grid(row=6, column=0, padx=10, pady=10)



# Crear Treeview


tree = ttk.Treeview(ventana, columns=(1, 2, 3, 4), show="headings")


tree.grid(row=5, columnspan=2)
tree.heading(1, text="Nombre", anchor="w")
tree.heading(2, text="Autor", anchor="w")
tree.heading(3, text="Género", anchor="w")
tree.heading(4, text="Año", anchor="w")




 # Mostrar libros existentes al iniciar el programa
mostrar_libros()

 # Ejecutar ventana
ventana.mainloop()