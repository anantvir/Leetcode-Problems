"""Author - Anantvir Singh, Problem Source - Leetcode, Statement - Range Sum Query Mutable"""

"""A good approach for this type of questions is building a segmented tree"""

a = [2,4,5,7,8,9]
tree = [None]*(2*len(a))

def BuildTree(a):
    n = len(a)
    for i in range(n,2*n):
        tree[i] = a[i-n]
    for j in range(n-1,0,-1):
        tree[j] = tree[2*j] + tree[2*j+1]
    return tree
BuildTree(a)
print(tree)

new_element = 7             # add it at index 2

def UpdateTree(i,val):     # i = index in 'a' where we need to put new element
    n = int(len(tree)/2)
    i = i + n
    tree[i] = val
    print(tree)
    for j in range(n-1,0,-1):
        tree[j] = tree[2*j] + tree[2*j+1]
    return tree
UpdateTree(2,new_element)
print(tree)