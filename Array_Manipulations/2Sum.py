"""Author - Anantvir Singh, Problem Source - Leetcode, Statement - two sum"""


# -------------------- Brute Force --------------------------
# --> For each i, check if target - a[i] is available in the array or not

a = [-1,0,1,2,-1,-4]

def Two_Sum(a,target):
    lst = []
    for i in range(len(a)-1):
        for j in range(i+1,len(a)):
            if a[j] == target - a[i]:
                if [i,j] not in lst:
                    lst.append([i,j])
    return lst

print(Two_Sum(a,-2))



# --------------- Improvement over Brute Force (Hashtable)---------------

# Use hashtable to store the elements of array as keys and their indices as values so that when we 
# search for target - a[i], we check if target - a[i] is available in hashtable. If yes, then
# return its index i.e j, combine it with i and return list [i,j]

def Two_Sum_Hashtable(a,target):
    dic = dict()
    lst = []
    for i in range(len(a)):
        dic[a[i]] = i
    for i in range(len(a)-1):
        if target - a[i] in dic.keys() and target - a[i] != a[i]:
            index = dic[target - a[i]]
            if [i,index] not in lst:
                lst.append([i,index])
    return lst

print(Two_Sum_Hashtable(a,2))
            