'''
Given a string A and a dictionary of n words B, 
find out if A can be segmented into a space-separated 
sequence of dictionary words.

Input:
n = 12
B = { "i", "like", "sam", "sung", "samsung", "mobile",
"ice","cream", "icecream", "man", "go", "mango" }
A = "ilike"
Output: 1
Explanation:The string can be segmented as "i like".

'''

def wordBreak(A,B):
    
    newWord = ""

    for letter in A:
        
        newWord += letter

        if newWord in B:
            A = A.replace(newWord, "", 1)
            newWord = ""
        
    if A == "" :
        return 1
    else:
        return 0
            
        
B = { "i", "like", "sam", "sung", "samsung", "mobile", "ice","cream", "icecream", "man", "go", "mango" }
A = "ilikesamsung"

print(wordBreak(A, B))