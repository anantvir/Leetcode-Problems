"""Naive Solution"""
def Longest_Susbtring(arr):
    STR = []
    max_length = 0
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            if arr[j] in STR:
                if len(STR) > max_length:
                    max_length = len(STR)
                STR = []
                break
            else:
                STR.append(arr[j])
    return max_length

text = 'qrsrmnmtuvwxab'
text1 = 'pwwkewmnopqwer'
#print(Longest_Susbtring(list(text)))


"""Efficient using Sliding Hashset(Set in python). Put element in Hashset, if it already exists then stop and slide the Hashset to next pointer"""
def Longest_Substring_Hashed(arr):
    hashset = set()
    max_length = 0
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            if arr[j] in hashset:
                if len(hashset) > max_length:
                    max_length = len(hashset)
                hashset = set()
                break
            else:
                hashset.add(arr[j])
    return max_length

print(Longest_Substring_Hashed(list(text)))


