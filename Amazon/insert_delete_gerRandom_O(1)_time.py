"""insert, remove and getrandom element in constant time"""

"""
Approach --> Use 2 data structures, List and Hashmap. Hashmap provides constant time search, insert and remove but not gerRandom
because to get a random element we need to provide index and hashmap does not contain indices. So hashmaps keys must be
converted to list and index of that list will contain the hashed representation of the element. But to create that list takes
linear time. A simple List on the other hand provides constant time insertion and access (if the index is known) but deletion is expensive
So the solution is to always delete the last element. 
So get the index of element to be deleted. Swap the last element with the element to be deleted and delete the last element 
from the list. Thus deletion will be a constant time operation.
Create a dictionary {element : index} because when we get an element to be deleted we need its index in O(1) time so that we can
swap it with last and then pop last. To get index in O(1) time we maintain index of each element in a dict.
"""
from random import choice
class RandomizedSet(object):

    def __init__(self):
        self.data_list = []
        self.index_dict = {}
        

    def insert(self, val):
        if val not in self.index_dict:                      # Add if the element does not exist in dict
            self.index_dict[val] = len(self.data_list)      # len(data_list)-1 will be the last filled index in array and len(data_list) will be the one where any new element will be appended
            self.data_list.append(val)
            return True
        else:
            return False       

    def remove(self, val):
        if val not in self.index_dict:
            return False
        else:
            idx = self.index_dict[val]                      # get index of element to be deleted
            last_element = self.data_list[-1]               # Store last element
            self.data_list[idx] = last_element              # Store last in place of element to be deleted
            self.index_dict[last_element] = idx             # update index of last element in dictionary since earlier last element is now in place of deleted element
            self.data_list.pop()                            # Remove the last spot of the list
            del self.index_dict[val]                        # Remove the entry of deleted element from dictionary
            return True

    def getRandom(self):
        return choice(self.data_list)
        


# Your RandomizedSet object will be instantiated and called as such:
#// Init an empty set.
randomSet = RandomizedSet()

#// Inserts 1 to the set. Returns true as 1 was inserted successfully.
print(randomSet.insert(1))

#// Returns false as 2 does not exist in the set.
print(randomSet.remove(2))

#// Inserts 2 to the set, returns true. Set now contains [1,2].
print(randomSet.insert(2))

#// getRandom should return either 1 or 2 randomly.
print(randomSet.getRandom())

#// Removes 1 from the set, returns true. Set now contains [2].
print(randomSet.remove(1))

#// 2 was already in the set, so return false.
print(randomSet.insert(2))

#// Since 2 is the only number in the set, getRandom always return 2.
print(randomSet.getRandom())