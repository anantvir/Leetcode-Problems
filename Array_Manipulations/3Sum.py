"""Author - Anantvir Singh, Problem Source - Leetcode, Statement - 3 sum"""

"""# Use hashtable to store the elements of array as keys and their indices as values so that when we 
# search for target - a[i], we check if target - a[i] is available in hashtable. If yes, then
# return its index i.e j, combine it with i and return list [i,j]"""

"""O(n^2) using 2Sum approach. 3Sum uses 2Sum inside it"""

a = [-1,0,1,2,-1,-4]

def Three_Sum(a):
    dic = dict()
    lst = []
    a = sorted(a)                   # Sorted them because we have to apply condition at line 16
    hashtable = {}
    for i in range(len(a)):
        hashtable[a[i]] = i     
    for i in range(len(a)-1):       # i = 1 to n-1
        target = -a[i]
        if a[i] != a[i-1]:          # E.g if both a[i], and a[i-1] are -1,-1 respectively, then target required = 1. So results are same. This condition prevents duplicates in output
            for j in range(i+1,len(a)):
                if target - a[j] in hashtable.keys() and target - a[j] != a[j]:     # target - a[j] != a[j]. If this condition does not hold then we will have output like sum of 1 has indices [2,2] or [3,3]. i.e indices will repeat. Because we will choose a[i] and also pick a[i] from hashtable resulting in same indices in output array
                    print(target-a[j])
                    ind = hashtable[target - a[j]]
                    if j < ind:     # to prevent output like [3,4] and [4,3],--> https://leetcode.com/problems/3sum/discuss/7498/Python-solution-with-detailed-explanation
                        lst.append([a[i],a[j],a[ind]])
    return lst

print(Three_Sum(a))