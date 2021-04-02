class Solution(object):
    def isPalindrome(self, x):
        s = str(x)
        rs = "".join(list(reversed(s)))
        if rs != s:
            return False
        return True

        
