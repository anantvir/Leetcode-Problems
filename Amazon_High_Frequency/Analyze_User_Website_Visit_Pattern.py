"""Clear Statement --> For each user we need to get all possible combinations of 3 sequences
Then from those possible 3 sequences we need to return the 3 sequence which has been visited by maximum
number of users.
1) Create a dictionary 
{
    Joe:[home,about,career],
    Mary:[home,about,career],
    James:[home,cart,maps,home]
}
2) For each value in the above dictionary, create all possible combinations and append each combination
into a list and then apply counter on that list which will give count of each element in that list
i.e count of each 3 sequence. Return the 3 sequence having maximum count by using the most_common method
from Counter class
"""

from collections import defaultdict,Counter
from itertools import combinations
class Solution(object):
    def mostVisitedPattern(self, username, timestamp, website):
        """
        :type username: List[str]
        :type timestamp: List[int]
        :type website: List[str]
        :rtype: List[str]
        """
        data_dict = defaultdict(list)
        for i in range(len(username)):
            data_dict[username[i]].append(website[i])
        val_lst = list(data_dict.values())
        temp_lst = []
        for i in range(len(val_lst)):
            comb = list(combinations(val_lst[i],3))
            for val in comb:
                temp_lst.append(val)
        c = Counter(temp_lst)
        return c.most_common(1)[0][0]

username = ["joe","joe","joe","james","james","james","james","mary","mary","mary"]
timestamp = [1,2,3,4,5,6,7,8,9,10]
website = ["home","about","career","home","cart","maps","home","home","about","career"]

s = Solution()
print(s.mostVisitedPattern(username,timestamp,website))

