input_data = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]

input_data = sorted(input_data,key= len)                # Sort by length of each string because a word can be formed by words smaller than itself only

print(input_data)

def Concatenated_Words(input_data):
    output_list = []
    for k in range(len(input_data)):
        word_list = input_data[:k]
        word_to_check = input_data[k]
        if len(word_list) >= 2 and len(word_to_check) > len(word_list[-1]):  # Check that length of word_list must be greater than 2 because concatenated word means composed of minimum 2 words. 
            # Also check if length of current word i greater than previous word(A word can be formed by words longer than it in length)     
            """---------------- Word Break I Logic, DP Matrix same as matrix chain multiplication -----------------"""
            # Consider chains from len = 2 to n
            n = len(word_to_check)
            m = [[False for i in range(n)] for i in range(n)]
            for i in range(n):
                m[i][i] = False
            for l in range(2,len(word_to_check)+1):
                for i in range(len(word_to_check)-l+1): # For l=2 to n-l+1. But here it will go till n-l because it starts from 0
                    j = i+l-1
                    if word_to_check[i:j+1] in word_list:
                        m[i][j] = True
                    else:
                        for k in range(i,j):
                            if m[i][k] == True and m[k+1][j] == True:
                                m[i][j] = True
            if m[0][n-1] == True:
                output_list.append(word_to_check)
    return output_list

print(Concatenated_Words(input_data))
