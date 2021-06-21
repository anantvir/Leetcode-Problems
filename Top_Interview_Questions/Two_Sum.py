# Make a hashtable and store {nums[i] : i}

def Two_Sum(nums, target):
    hashtable = {}
    for index, element in enumerate(nums):
        hashtable[element] = index

    for i in range(len(nums)):
        complement = target - nums[i]
        if hashtable.get(complement) and hashtable.get(complement) != i:    # USe hashtable.get() so that it returns None when key not avail. Direct access gives exception
            return [i, hashtable[complement]]
    raise Exception("No Two Sum Solution")
        

Two_Sum([2,5,5,11], 10)
