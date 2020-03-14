import bisect

a = [(10,'love'),(20,'high'),(20,'jigh'),(20,'ligh')]
b = [2,3,4,4,4,6,7,8]

print(bisect.bisect(a,(20,'iigh')))