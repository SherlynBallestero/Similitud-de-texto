#User function Template for python3    


    
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





            
        
