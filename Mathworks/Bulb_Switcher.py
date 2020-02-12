"""APPROACH is mathematical.
Consider a bulb 6.
It is 'on' intially, then it is toggled in round 2,3 and 6 which are also its factors. It is toggled k
times and it has total k+1 factors (including 1, but it was already on in round 1)
i.e total number of factors of 6 are 1,2,3,6 = even number of factors.
If a number i CANNOT be written as i = p/i then 'i' obviosly NOT A perfect squre and has even number of factors e.g 6
If a number i CAN be written as i = p/i then 'i' is obviosly A perfect squre and has odd number of factors e.g 9 has 1,3,9

If a number i has even number of factors then in the end it will be off, example 6 is on in round 1, then off,on,off
If a number i has odd number of factors i.e i is is a perfect square then the bulb i will be on in the end. Consider 4, round 1 its on,round 2 its off,then on, since it has 3 factors 1,2,4

Hence we just want to traverse the array once and check for all the perfect squares smaller than or equal to n i.e the number of bulbs
"""
from math import sqrt

"""----------Given Bulb Array -----------------"""
a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37]

count = 0
for i in range(0,len(a)):
    if sqrt(a[i]).is_integer():      # Increment count if sqrt(a[i]) is an integer which means its a perfect square
        count += 1

print(count)



