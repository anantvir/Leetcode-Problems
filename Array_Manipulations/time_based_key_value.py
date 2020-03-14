from collections import defaultdict
import bisect
class TimeMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = defaultdict(list)

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        self.dict[key].append((timestamp,value))

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        if key in self.dict:
            lst = self.dict[key]
            idx = bisect.bisect(lst,(timestamp,chr(127)))       # chr(127) because we need to make a tuple of timstamp and a string, and if the timsestamp is same then we can sort on basis of the string. So we want a string which does not affect sorting. Ascii value of chr(127) = delete (it does not affect sorting)
            return lst[idx-1][1] if idx > 0 else ""
        else:
            return ""
    
kv = TimeMap()
kv.set("love", "high", 10)
kv.set("love", "low", 20)
print(kv.get("love", 5))
print(kv.get("love", 10))
print(kv.get("love", 15))
print(kv.get("love", 20))
print(kv.get("love", 25))