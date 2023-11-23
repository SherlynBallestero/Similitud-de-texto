import tkinter as tk
from tkinter import ttk
import lcs

# Función para cambiar de ventana
def cambiar_ventana(principalWindow, newWindow):
    principalWindow.withdraw()  # Ocultar la ventana actual
    newWindow.deiconify()  # Mostrar la ventana secundaria

# Crear la ventana principal
window = tk.Tk()
window.title("Proyecto de Longest Common Subsequence")
window.geometry("600x400")
window.configure(bg="light blue")

# Crear botón en la ventana principal para abrir ventana2
boton1 = tk.Button(window, text="Mayor subsecuencia común", command=lambda: cambiar_ventana(window, window2), bg="gray", fg="white")
boton1.pack(pady=40)

# Crear botón en la ventana principal para abrir ventana3
boton2 = tk.Button(window, text="Plagio entre documentos", command=lambda: cambiar_ventana(window, window3), bg="gray", fg="white")
boton2.pack(pady=20)

# Crear botón en la ventana principal para abrir ventana4
boton3 = tk.Button(window, text="Mayor subsecuencia palíndroma", command=lambda: cambiar_ventana(window, window4), bg="gray", fg="white")
boton3.pack(pady=20)

# Crear botón en la ventana principal para abrir ventana5
boton3 = tk.Button(window, text="Mayor subsecuencia en varias cadenas", command=lambda: cambiar_ventana(window, window5), bg="gray", fg="white")
boton3.pack(pady=20)

# Definición de ventana2
window2 = tk.Toplevel(window)
window2.title("Mayor subsecuencia común entre dos cadenas")
window2.geometry("600x400")
window2.configure(bg="light blue")

# Crear los widgets en la ventana2
label1 = tk.Label(window2, text="Ingrese la primera cadena:", bg="light blue")
entry1 = tk.Entry(window2)
label2 = tk.Label(window2, text="Ingrese la segunda cadena:", bg="light blue")
entry2 = tk.Entry(window2)
button = tk.Button(window2, text="Encontrar la mayor subsecuencia común", command=lambda: result.config(text=lcs.find_longest_palindromic_subsequence(entry1.get(), entry2.get())), bg="gray", fg="white")
label3 = tk.Label(window2, text="La mayor subsecuencia común es:", bg="light blue")
result = tk.Label(window2, text="")
boton5 = tk.Button(window2, text="Atrás", command=lambda: cambiar_ventana(window2, window), bg="gray", fg="white")

# Colocar los widgets en la ventana2
label1.pack(pady=20)
entry1.pack()
label2.pack(pady=10)
entry2.pack()
button.pack(pady=10)
label3.pack(pady=10)
result.pack(pady=10)
boton5.pack(pady=30)

# Definición de ventana3
window3 = tk.Toplevel(window)
window3.title("Plagio entre documentos")
window3.geometry("600x400")
window3.configure(bg="light blue")

# Crear combobox en la ventana3
opciones = ["contents/Abecedario.txt", "contents/AbecedarioCopia.txt", "contents/Arianne.txt", "contents/Choque de reyes.txt"]
lb = tk.Label(window3, text="Seleccione el documento 1", bg="light blue")
combobox1 = ttk.Combobox(window3, values=opciones)
lb2 = tk.Label(window3, text="Seleccione el documento 2", bg="light blue")
combobox2 = ttk.Combobox(window3, values=opciones)
boton3 = tk.Button(window3, text="Detectando Plagio", command=lambda: resultb3.config(text=lcs.plagiarism_check(combobox1.get(), combobox2.get())), bg="gray", fg="white")
resultb3 = tk.Label(window3, text="")
boton4 = tk.Button(window3, text="Atrás", command=lambda: cambiar_ventana(window3, window), bg="gray", fg="white")

# Colocar los widgets en la ventana3
lb.pack(pady=20)
combobox1.pack(pady=10)
lb2.pack(pady=10)
combobox2.pack(pady=10)
boton3.pack(pady=20)
resultb3.pack(pady=20)
boton4.pack(pady=20)

# Definición de ventana4
window4 = tk.Toplevel(window)
window4.title("Mayor subsecuencia palíndroma")
window4.geometry("600x400")
window4.configure(bg="light blue")

# Crear los widgets en la ventana4
l1 = tk.Label(window4, text="Ingrese la primera cadena:", bg="light blue")
e1 = tk.Entry(window4)
b = tk.Button(window4, text="Encontrar la mayor subsecuencia palíndroma", command=lambda: r.config(text=lcs.longest_palindrome_subsequence(e1.get())), bg="gray", fg="white")
l3 = tk.Label(window4, text="La mayor subsecuencia palindómica es:", bg="light blue")
r = tk.Label(window4, text="")
b5 = tk.Button(window4, text="Atrás", command=lambda: cambiar_ventana(window4, window), bg="gray", fg="white")

# Colocar los widgets en la ventana4
l1.pack(pady=20)
e1.pack()
b.pack(pady=10)
l3.pack(pady=10)
r.pack(pady=10)
b5.pack(pady=30)

# Definición de ventana5
window5 = tk.Toplevel(window)
window5.title("Mayor subsecuencia en varias cadenas")
window5.geometry("600x400")
window5.configure(bg="light blue")
# Crear los widgets en la ventana5
l51 = tk.Label(window5, text="Ingrese las cadenas que quiera analizar separadas por coma:", bg="light blue")
e51 = tk.Entry(window5)
b52=tk.Button(window5,text="ok",command=lambda:r5.config(text=lcs.LCS_inmultiplesStrings(e51.get())), bg="gray", fg="white")
r5 = tk.Label(window5, text="")
b51 = tk.Button(window5, text="Atrás", command=lambda: cambiar_ventana(window5, window), bg="gray", fg="white")
# Colocar los widgets en la ventana5
l51.pack(pady=20)
e51.pack(pady=20)
b52.pack(pady=20)
b51.pack(pady=20)
r5.pack(pady=20)

# Ocultar las ventanas secundarias al inicio
window2.withdraw()
window3.withdraw()
window4.withdraw()
window5.withdraw()

# Iniciar el bucle principal de la ventana
window.mainloop()