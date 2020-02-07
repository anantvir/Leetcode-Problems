from itertools import combinations
from collections import Counter
 
a = ['home','cart','maps']
d = {'a':[('anant','vir','singh')],
'b':[('simrat','vir','singh'),('anant','vir','singh')],
'c':[('sai','mahesh','chandra')]
}
mat = [(1,2,3),(5,6,7),(7,8,9),(1,2,3)]

c = Counter(mat)
print(c.most_common(2)[0][0])