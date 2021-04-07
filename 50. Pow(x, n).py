class Solution(object):
    def myPow(self, x, n):
        if n < 0:
            x = 1/x
        n = abs(n)
        if n == 0:
            return 1
        temp = self.myPow(x,n//2)
        if n%2 == 0:
            return temp*temp
        else:
            return x*temp*temp
        
