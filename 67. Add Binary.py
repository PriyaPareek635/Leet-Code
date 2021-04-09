class Solution(object):
    def addBinary(self, a, b):
        add = bin(int(a,2) + int(b,2))
        return add[2::]        
