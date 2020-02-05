"""
Counter counts how many times each element appears in that list and returns a dictionary in the format
{
    element 1 : count of element 1
    element 2 : count of element 2
}
Pass the input array nums to Counter class to get the count dictionary. Then use nlargest() method from heapq module
nlargest() take an argument key. What function we give in key is used for comparision to give the k largest
items. Example key can be a lambda function or key in this case gets the value corresponding the 
key we get from counter.keys() list
"""

from collections import Counter
import heapq

nums = [1,1,1,2,2,3,5,5,5,5,5,6,3,8,9,9,9,9,9,9,9,5,5,5,5,5]

def K_Most_Frequent(nums,k):
    counter = Counter(nums)
    output = heapq.nlargest(k,counter.keys(),key=counter.get)
    return output

print(K_Most_Frequent(nums,2))

        