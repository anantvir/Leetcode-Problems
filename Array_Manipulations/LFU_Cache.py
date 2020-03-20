"""For understanding refer to https://deepakvadgama.com/blog/lfu-cache-in-O%281%29/

Maintain 3 data structures.
1) k_v_dict --> contains key value pairs i.e actual data
2) freq_dict --> contains frequencey of how many times each element has been used till now freq_dict =
{
    element : frequency
}

3) freq_element_dict (Ordered Dict) --> keys here represent frequencey i.e 1,2,3... etc and each value is a list where items corresponding to that frequency are appended
freq_element_dict = {
    1 : [10,2,5]       Here 10, 2 and 5 are the elements which have frequency = 1
    4: [67,9]           67 and 9  are elements having frequency = 4
}  ====> We use an Ordered Dict because when we increase the frequency during get or put operation, we need to move the element
in the value list of freq_element_dict from existing frequency to one higher frequency. So we need to access to the lowest frequency
int he freq_element_dict, which we can only get if the freq_element_dict is sorted. Hence use Sorted Map or Ordered Dict

"""

from collections import defaultdict,OrderedDict
class LFUCache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.k_v_dict = {}
        self.freq_dict = defaultdict(int)
        self.freq_element_dict = OrderedDict()

    def get(self,key):
        if key not in self.k_v_dict:
            return -1
        val = self.k_v_dict[key]
        old_freq_val = self.freq_dict[key]
        self.freq_dict[key] += 1
        new_freq_val = self.freq_dict[key]
        self.move_key_to_diff_freq(old_freq_val,new_freq_val,key)
        if len(self.freq_element_dict[old_freq_val]) == 0:
            del self.freq_element_dict[old_freq_val]
        return val

    def move_key_to_diff_freq(self,old_freq,new_freq,key):
        self.freq_element_dict[old_freq].remove(key)
        if new_freq not in self.freq_element_dict:
            self.freq_element_dict[new_freq] = []
            self.freq_element_dict[new_freq].append(key)
        else:
            self.freq_element_dict[new_freq].append(key)

    def put(self,key,value):
        least_freq_used_item = None
        if key in self.k_v_dict:
            val = self.k_v_dict[key]
            old_freq_val = self.freq_dict[key]
            self.freq_dict[key] += 1
            new_freq_val = self.freq_dict[key]
            self.move_key_to_diff_freq(old_freq_val,new_freq_val,key)
            return val
        else:
            if len(self.k_v_dict) >= self.capacity:
                lowest_freq_in_dict = list(self.freq_element_dict.items())[0][0]
                least_freq_used_item = self.freq_element_dict[lowest_freq_in_dict][0]
                del self.k_v_dict[least_freq_used_item]
                del self.freq_dict[least_freq_used_item]
                self.freq_element_dict[lowest_freq_in_dict].pop(0)
                if len(self.freq_element_dict[lowest_freq_in_dict]) == 0:
                    del self.freq_element_dict[lowest_freq_in_dict]
            self.k_v_dict[key] = value
            self.freq_dict[key] += 1
            if 1 not in self.freq_element_dict:
                self.freq_element_dict[1] = []
                self.freq_element_dict[1].append(key)
            else:
                self.freq_element_dict[1].append(key)
            return least_freq_used_item

cache = LFUCache(3)
print(cache.put(2, 2))
print(cache.put(1, 1))
print(cache.get(2))  
print(cache.get(1))
print(cache.get(2))      
print(cache.put(3, 3))  
print(cache.get(3))
print(cache.get(2))     
print(cache.get(1))      
print(cache.get(4))
