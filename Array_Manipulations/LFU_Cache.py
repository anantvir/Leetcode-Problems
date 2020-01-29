"""For understanding refer to https://deepakvadgama.com/blog/lfu-cache-in-O%281%29/

Maintain 3 data structures.
1) k_v_dict --> contains key value pairs i.e actual data
2) freq_dict --> contains frequencey of how many times each element has been used till now freq_dict =
{
    element : frequency
}

3) freq_element_dict --> keys here represent frequencey i.e 1,2,3... etc and each value is a list where items corresponding to that frequency are appended
freq_element_dict = {
    1 : [10,2,5]       Here 10, 2 and 5 are the elements which have frequency = 1
    4: [67,9]           67 and 9  are elements having frequency = 4
}

"""

from collections import defaultdict
class LFUCache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.k_v_dict = {}
        self.freq_dict = {}
        self.freq_element_dict = defaultdict(list)

    def get(self, key):
        if key in self.k_v_dict:                                # Check if key already exists
            val = self.k_v_dict[key]
            old_freq = self.freq_dict[key]                      # Keep old frequency
            self.freq_dict[key] += 1
            new_freq = self.freq_dict[key]                      # Keep new frequency. Pass old and new freq to move_key_to_diff_freq method
            self.move_key_to_diff_freq(old_freq,new_freq,key)
            if len(self.freq_element_dict[old_freq]) == 0:      # If a frequencey key has no element in the corresponding list, then no need of freq as key. Just delete it
                del self.freq_element_dict[old_freq]
            return val
        else:
            return -1

    def move_key_to_diff_freq(self,old_freq,new_freq,key):      # Moves an element from one freq to another in self.freq_element_dict  
        self.freq_element_dict[old_freq].remove(key)
        self.freq_element_dict[new_freq].append(key)


    def put(self, key, value):
        if key not in self.k_v_dict:                                                        # If key doesnt exist in data dict
            least_freq_used_item = None
            """--------------------- Key Eviction Logic ---------------------------"""
            if len(self.k_v_dict) >= self.capacity:                                         # If ucrr size >= capacity. = because we want to remove LFU item as soon as cache reaches its capacity
                lowest_non_null_freq = list(self.freq_element_dict.keys())[0]               # Gets the lowest frequency which has some element corresponding to it
                least_freq_used_item = self.freq_element_dict[lowest_non_null_freq][0]      # Item corresponding to lowest frequency             
                del self.k_v_dict[self.freq_element_dict[lowest_non_null_freq][0]]          # delete that key from data dict
                del self.freq_dict[self.freq_element_dict[lowest_non_null_freq][0]]         # delete key from frequencey dict as well
                self.freq_element_dict[lowest_non_null_freq].pop(0)                         # Pop the 1st element from list corresponding to lowest frequency
                if len(self.freq_element_dict[lowest_non_null_freq]) == 0:                  # after popping if the length of that list becomes zero, delete that frequencey and list(key,value) pair from freq_element_dict
                    del self.freq_element_dict[lowest_non_null_freq]
                print("Key :",least_freq_used_item," evicted !")
            """--------------------------------------------------------------------"""
            self.k_v_dict[key] = value                                                      # Add the new key to data dict        
            self.freq_dict[key] = 1                                                         # set its frequency to 1
            self.freq_element_dict[1].append(key)                                           # add it to freq_element_dict where key is frequency = 1 and values are items which have 1 frequency
            return least_freq_used_item
        else:
            self.k_v_dict[key] = value                                                      # Add the new key to data dict 
            old_freq = self.freq_dict[key]
            self.freq_dict[key] += 1
            new_freq = self.freq_dict[key]
            self.move_key_to_diff_freq(old_freq,new_freq,key)                               # If key already exists then its frequency will be changed so move it to new freq in freq_element_dict
            return self.k_v_dict[key]


cache = LFUCache(2)
print(cache.put(1, 1))
print(cache.put(2, 2))
print(cache.get(1))  
print(cache.put(3, 3))   
print(cache.get(2))      
print(cache.get(3))     
print(cache.put(4, 4))  
print(cache.get(1))     
print(cache.get(3))      
print(cache.get(4))