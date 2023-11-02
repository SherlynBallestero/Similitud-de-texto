import tkinter as tk
from tkinter import ttk
import lcs
from PIL import ImageTk, Image




#Cambiar de ventana
def cambiar_ventana(principalWindows,newWindows):
    principalWindows.withdraw()  # Ocultar la ventana actual
    newWindows.deiconify()  # Mostrar la ventana secundaria

# Crear la ventana secundaria1
window2 = tk.Tk()
# Crear la ventana secundaria1
window3 = tk.Tk()
#pantalla principal 
window=tk.Tk()
window.title("Proyecto de Longest Common Subsequence")
window.geometry("600x400")
window.configure(bg="light blue")
# # Crear botón en la ventana principal
boton1 = tk.Button(window, text="mayor subsecuencia común ", command=lambda: cambiar_ventana(window, window2),bg = "gray",fg="white")
boton1.pack(pady=40)
boton2 = tk.Button(window, text="Plagio entre documentos", command=lambda: cambiar_ventana(window, window3),bg = "gray",fg="white")
boton2.pack(pady=20)

#definicion ventana2
window2.title("mayor subsecuencia común entre dos cadenas")
window2.geometry("600x400")

# Crear los widgets
label1 = tk.Label(window2, text="Ingrese la primera cadena:",bg="light blue")
entry1 = tk.Entry(window2)
label2 = tk.Label(window2, text="Ingrese la segunda cadena:",bg="light blue")
entry2 = tk.Entry(window2)
button = tk.Button(window2, text="Encontrar la mayor subsecuencia común", command=lambda: result.config(text=lcs.lcs(entry1.get(), entry2.get())),bg = "gray",fg="white")
label3 = tk.Label(window2, text="La mayor subsecuencia común es:",bg="light blue")
result = tk.Label(window2, text="")
window2.configure(bg="light blue")
# Colocar los widgets en la ventana secundaria
label1.pack(pady=20)
entry1.pack()
label2.pack(pady=10)
entry2.pack()
button.pack(pady=10)
label3.pack(pady=10)
result.pack(pady=10)
boton5=tk.Button(window2,text="atras", command=lambda: cambiar_ventana(window2, window),bg = "gray",fg="white")
boton5.pack(pady=30)
window2.withdraw()

#definicion ventana secundaria2
window3.title("Plagio entre documentos")
window3.geometry("600x400")
window3.withdraw()
window3.configure(bg="light blue")
#crear combobox
opciones = ["contents/Abecedario.txt", "contents/AbecedarioCopia.txt", "contents/Arianne.txt","contents/Choque de reyes.txt"]
lb = tk.Label(window3, text="Seleccione el documento1",bg="light blue")
lb.pack(pady=20)
combobox1 = ttk.Combobox(window3, values=opciones)
combobox1.pack(pady=10)
valorSeleccionado1=combobox1.get()
lb2 = tk.Label(window3, text="Seleccione el documento2",bg="light blue")
lb2.pack(pady=10)
combobox2=ttk.Combobox(window3, values=opciones)
combobox2.pack(pady=10)
valorSeleccionado2=combobox2.get()
def seleccionarOpcion():
    valorSeleccionado1 = combobox1.get()
    valorSeleccionado2 = combobox2.get()
    resultb3.config(text=lcs.plagiarism_check(str(valorSeleccionado1), str(valorSeleccionado2)))

boton3 = tk.Button(window3, text="Detectando Plagio", command=lambda: seleccionarOpcion(),bg = "gray",fg="white")
boton3.pack(pady=20)
resultb3 = tk.Label(window3, text="")
resultb3.pack(pady=20)
boton4=tk.Button(window3,text="atras", command=lambda: cambiar_ventana(window3, window),bg = "gray",fg="white")
boton4.pack(pady=20)
# Iniciar el bucle principal de la ventana
window.mainloop()
