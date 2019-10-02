"""Author - Anantvir Singh, Problem Source - Leetcode, Statement - Range Sum Query Mutable"""

"""A good approach for this type of problems is building a segmented tree
For details refer   https://leetcode.com/articles/a-recursive-approach-to-segment-trees-range-sum-queries-lazy-propagation/#

------->>> Why we follow this approach ? Runtime = O(log n)

Segmented trees can be used in many other similar situations like finding minimum, maximum, sum, greatest common divisor, 
least common denominator in array in logarithmic time """

import math

a = [2,4,5,7,8,9]
tree = [None]*(2*len(a))
n = len(a)
def buildTree(a):
    n = len(a)
    for i in range(n,2*n):
        tree[i] = a[i-n]
    for j in range(n-1,0,-1):
        tree[j] = tree[2*j] + tree[2*j+1]
    return tree
buildTree(a)
print(tree)

new_element = 7             # add it at index 2

def updateTree(i,val):     # i = index in 'a' where we need to put new element
    n = int(len(tree)/2)
    i = i + n
    tree[i] = val
    print(tree)
    for j in range(n-1,0,-1):
        tree[j] = tree[2*j] + tree[2*j+1]
    return tree
updateTree(2,new_element)
print(tree)

def sumRange(l,r):
    l += n
    r += n
    Sum = 0
    while(l <= r):
        if(l%2 == 1):
            Sum += tree[l]
            l += 1
        if(r%2 == 0):
            Sum += tree[r]
            r -= 1
        l = math.floor(l/2)
        r = math.floor(r/2)
    return Sum

print(sumRange(1,4))
    

