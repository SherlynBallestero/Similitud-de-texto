import os   


    
    #Function to find the length of longest common subsequence in two strings.
def lcs(s1,s2):  
    x = len(s1) 
    y = len(s2)  
    dp = [[0 for i in range(y + 1)] for j in range(x + 1)] 
    for i in range (1, x + 1):  
        for j in range (1, y + 1):  
            if s1[i - 1] == s2[j - 1]:   
                dp[i][j] = dp[i-1][j-1] + 1   
            else: 
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]) 
    
    i = x 
    j = y  
    z = ""  
    while i>0 and j > 0: 
        if s1[i - 1] == s2[j - 1]: 
            z = s1[i - 1] + z 
            i -= 1 
            j -= 1 
        else:  
            if dp[i - 1][j] > dp[i][j-1]: i-=1 
            else: j -=1  
    return z 


# Función para hallar la subsecuencia palíndromo más larga de una cadena
def longest_palindrome_subsequence(s):
    # Obtener la longitud de la cadena
    n = len(s)

    # Crear una matriz LPS de tamaño n x n e inicializarla con ceros
    LPS = [[0 for _ in range(n)] for _ in range(n)]

    # Recorrer la matriz por diagonales, empezando por la principal
    for k in range(n):
        for i in range(n-k):
            j = i + k

            # Si los caracteres en las posiciones i y j son iguales
            if s[i] == s[j]:
                # Si i y j son el mismo carácter o son adyacentes
                if i == j or i == j - 1:
                    # El palíndromo tiene longitud 1 o 2
                    LPS[i][j] = k + 1
                else:
                    # El palíndromo tiene longitud mayor que 2
                    LPS[i][j] = LPS[i+1][j-1] + 2
            else:
                # Si los caracteres en las posiciones i y j son diferentes
                # Se escoge el máximo entre los valores de las celdas adyacentes
                LPS[i][j] = max(LPS[i+1][j], LPS[i][j-1])

    # La longitud de la subsecuencia palíndromo más larga es LPS[0][n-1]
    length = LPS[0][n-1]

    # Crear una variable auxiliar para almacenar la subsecuencia palíndromo más larga
    palindrome = ""

    # Recorrer la matriz LPS en sentido inverso, desde la esquina superior derecha hasta la inferior izquierda
    i = 0
    j = n - 1
    while i <= j:
        # Si los caracteres en las posiciones i y j son iguales
        if s[i] == s[j]:
            # Se añade el carácter a la variable auxiliar
            palindrome += s[i]
            # Se avanza a la celda LPS[i+1][j-1]
            i += 1
            j -= 1
        else:
            # Si los caracteres en las posiciones i y j son diferentes
            # Se avanza a la celda LPS[i+1][j] o LPS[i][j-1], según cuál tenga el valor mayor
            if LPS[i+1][j] > LPS[i][j-1]:
                i += 1
            else:
                j -= 1

    # Si la longitud de la subsecuencia palíndromo más larga es impar
    if length % 2 == 1:
        # Se elimina el último carácter de la variable auxiliar, ya que se repite
        palindrome = palindrome[:-1]

    # Se devuelve la variable auxiliar como la subsecuencia palíndromo más larga, invirtiendo la segunda mitad
    return palindrome + palindrome[::-1]



#detecting  plagiarism between documentes 
def plagiarism_check(file1="contents/Abecedario.txt", file2="contents/AbecedarioCopia.txt"):
    print("Ruta completa del archivo 1:", os.path.abspath(file1))
    print("Ruta completa del archivo 2:", os.path.abspath(file2))
    with open(file1, 'r',encoding='utf-8',errors='ignore') as document1, open(file2, 'r', encoding='utf-8',errors='ignore') as document2:
        text1 = document1.read()
        text2 = document2.read()
        lcs_length = len(lcs(text1, text2))
        similarity = (lcs_length*2) / (len(text1) + len(text2))
        if similarity*100>=60:
            return "Es probable que haya plagio entre los documentos proporcionados, estos tienen una similitud superior al 50%"
        else:
            return "Es poco probable que haya plagio entre los documentos proporcionados, estos tienen una similitud inferior al 50%"
     
def LCS_inmultiplesStrings(cadenas: str):
    print(cadenas)
    aux=cadenas.split(',')
    print(aux)
    answer=aux[0]
    for cad in range(len(aux)):
        answer=lcs(answer,aux[cad])
    print(answer) 
    return answer





            
        
