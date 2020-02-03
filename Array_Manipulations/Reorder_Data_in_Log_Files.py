"""------------------------------------- Approach (Lengthy and Space Inefficient)-----------------------------------------"""

class Solution(object):

    """Maintain a dictionary for letter logs and list for digit logs. For letter logs, key = identifier
    and value = rest of string"""
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        data_dict = {}                          
        dig_temp = []
        # for i in range(len(logs)):                # To split by only 1st word we can use split(" ",1) or find index of first space and then slice the arrays
        #     key,value = logs[i].split(" ",1)
        #     data_dict[key] = value
        
        for i in range(len(logs)):
            if logs[i][0] == 'l':               # If word starts with l, find index of 1st space and put it in dictionary             
                idx = logs[i].find(' ')
                key = logs[i][:idx]
                data_dict[key] = logs[i][idx+1:]
            else:
                dig_temp.append(logs[i])           # Append digit logs to a separate list as they dont need to be sorted

        temp_list = []
        for k,v in data_dict.items():
            temp_list.append((k,v))                 # Make a list of tuples of letter logs as [(identifier,log)] example [("let1","art can")]
        temp_list.sort(key=lambda x:(x[1],x[0]))    # Sort by first log and then by identifier
        output_list = []
        for i in range(len(temp_list)):
            output_list.append(temp_list[i][0]+' '+temp_list[i][1]) # After sorting append both elements of each tuple
        return output_list + dig_temp                               # Append digit logs directly to sorted letter logs

    """---------- Custom sorted order from Leetcode -------------------"""
    """Provide a key function. Split each log only till first word, if the first character of the
    remaining words after the first word is an alphabet, then return (0,rest of words,first word).
    0 in the beginning because letters need to come before digits and sorting happens according to tuple
    order i.e 0 comes before 1, then rest of words, then first word"""
    def reorderLogFiles2(self, logs):
        def f(log):
            id_, rest = log.split(" ", 1)
            print(rest[0])
            return (0, rest, id_) if rest[0].isalpha() else (1,)

        return sorted(logs, key = f)

logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
s = Solution()
print(s.reorderLogFiles(logs))







      