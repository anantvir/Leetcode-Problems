from collections import OrderedDict
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.ordered_dict = OrderedDict()
        self.capacity = capacity
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.ordered_dict:
            return -1
        self.ordered_dict.move_to_end(key)
        return self.ordered_dict[key]
       

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.ordered_dict:
            self.ordered_dict.move_to_end(key)
        self.ordered_dict[key] = value
        if len(self.ordered_dict) > self.capacity:
            self.ordered_dict.popitem(last = False)
        


# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(2)
obj.put(1,1)
obj.put(2,2)
param_1 = obj.get(1)
obj.put(3,3)
param_2 = obj.get(2)
obj.put(4,4)
param_3 = obj.get(1)
param_4 = obj.get(3)
param_5 = obj.get(4)
