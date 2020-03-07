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
# Also check if  target - a[i] should not be i itself. Because we can use the same element twice

def Two_Sum_New(a,target):
    n = len(a)
    hashtable = dict()
    for i in range(n):
        hashtable[a[i]] = i
    for i in range(n):
        to_find = target - a[i]
        if to_find in hashtable and hashtable[to_find] != i:
            return [i,hashtable[to_find]]

nums = [3,2,4]
print(Two_Sum_New(nums,6))
            