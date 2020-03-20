from collections import Counter,defaultdict
class Solution(object):
    """----------------- Just follow what the question says ----------------------"""
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        if len(paragraph) == 0:
            return ""
        banned = set(banned)
        for c in "!?',;.":              # Replace all these punctuations with ' '
            paragraph = paragraph.replace(c," ")
        paragraph = paragraph.lower().split(" ")    # Split by space and create a list with lower case letters
        c = defaultdict(int)
        for word in paragraph:
            """If there are 2 spaces in a sentence then "" in between those 2 spaces will be counted as a word. So we should skip that"""
            if word != "":                         
                c[word] += 1
        max_count = 0
        max_val = None
        for k,v in c.items():
            if k not in banned:
                if v > max_count:
                    max_count = v
                    max_val = k
        return max_val


paragraph = "Bob hit a ball the hit BALL flew far after it was hit."
banned = ["hit"]
s = Solution()
print(s.mostCommonWord(paragraph,banned))
        