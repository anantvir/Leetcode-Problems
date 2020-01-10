a = [2,7,11,15]
b = [9,2,3,8,11]

def Two_Sum(a,target):
    l = []
    for i in range(0,len(a)-1):
        for j in range(i+1,len(a)):
            if a[i] + a[j] == target:
                l.append(i)
                l.append(j)
    return l

#print(Two_Sum(a,18))

def Two_Sum_Hashed(a,target):
    # Create hashtable
    hashtable = {}
    l = set()
    for index,element in enumerate(a):
        hashtable[element] = index
    for key in hashtable:
        if target - key in hashtable.keys() and target-key != key:
            l.add(hashtable[key])
            l.add(hashtable[target-key])
    return list(l)

print(Two_Sum_Hashed(b,10))