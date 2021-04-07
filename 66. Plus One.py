class Solution(object):
    def plusOne(self, digits):
        return [int(a) for a in str(int("".join(map(str, digits))) + 1)]
        
        
        
