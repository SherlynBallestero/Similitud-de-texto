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
     






            
        
