class Solution(object):
    def lengthOfLastWord(self, s):
        res = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == " ":
                if res == 0:
                    continue
                else:
                    return res
            else:
                res += 1
        return res
