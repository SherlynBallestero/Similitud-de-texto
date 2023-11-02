# Importar tkinter
import tkinter as tk

# Importar el otro archivo
import lcs

# Crear la ventana principal
window = tk.Tk()
window.title("Proyecto de Longest Common Subsequence")
window.geometry("600x400")

# Crear los widgets
label1 = tk.Label(window, text="Ingrese la primera cadena:")
entry1 = tk.Entry(window)
label2 = tk.Label(window, text="Ingrese la segunda cadena:")
entry2 = tk.Entry(window)
button = tk.Button(window, text="Encontrar la mayor subsecuencia común", command=lambda: result.config(text=lcs.lcs(entry1.get(), entry2.get())),bg = "gray",fg="white")
label3 = tk.Label(window, text="La mayor subsecuencia común es:")
result = tk.Label(window, text="")
window.configure(bg="light blue")

# Colocar los widgets en la ventana
label1.pack()
entry1.pack()
label2.pack()
entry2.pack()
button.pack()
label3.pack()
result.pack()

# Iniciar el bucle principal de la ventana
window.mainloop()
