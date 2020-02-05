


wordDict = ["apple","pen","apple"]
s = "applepenapple"

def WordBreak_II(s,start):
    res = []
    if start == len(s):
        res.append('')
    for end in range(start,len(s)):
        #print(s[start:end+1])
        if s[start:end+1] in wordDict:
            last = []
            lst = WordBreak_II(s,end+1)
            for string in lst:
                temp = s[start:end+1]
                if string == "":
                    space = ""
                else:
                    space = " "
                res.append(temp+space+string)

    return res

print(WordBreak_II(s,0))