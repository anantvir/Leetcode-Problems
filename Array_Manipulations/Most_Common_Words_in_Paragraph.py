from collections import defaultdict
class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        freq_dict = defaultdict(int)            # To maintain frequency of each word
        banned_words = set(banned)              # Create set for O(1) time access
        for i in range(len(paragraph)):
            if paragraph[i] not in banned_words:    # If word not in banned words
                if paragraph[i][-1] in ['@','!','.',':','-','#','(',')','{','}','?',',']:       # If word has punctutation at the end
                    word = paragraph[i][:-1]                                                    # Trim the last character if it has punctuation
                else:
                    word = paragraph[i]
                word_cleaned = word.lower()                     # Convert to lower case
                freq_dict[word_cleaned] += 1                    # Increment frequency
        max_count,max_count_word = 0,None
        for k in freq_dict.keys():                              # Iterate over keys of dict and store the current max frequency in a variable
            if freq_dict[k] > max_count:
                max_count = freq_dict[k]
                max_count_word = k
        return max_count_word


text = "Bob hit a ball, the hit BALL flew far after flew it was flew hit."
paragraph = text.split(" ")         # Split the given paragraph by space
banned = ["hit"]
s = Solution()
print(s.mostCommonWord(paragraph,banned))

