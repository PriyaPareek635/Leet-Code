class Solution(object):
    def longestPalindrome(self, s):
        """ 
        Given a string : "abcdef", expanding left and right at index 2 means
        checking if (cba == def) || (cba == cde) == True. 
        """
        
        sLen = len(s) 
        start = 0
        end = 0
        prev_max = 0
        
        for i in range(0,sLen):    
            (len1,i1,j1) = self.f(s,i,i,sLen) 
            (len2,i2,j2) = self.f(s,i,i+1,sLen) # even len

            if len1 > prev_max:
                start = i1
                end = j1
                prev_max = len1
            
            if len2 > prev_max:
                start = i2
                end = j2
                prev_max = len2

        return s[start:end+1]
        
        # returns the length, start and end of the palindromic string
        # formed by expanding left from i and right from j
    
    def f(self, s, i, j, sLength):
        left = i
        right = j
        while (left >= 0 and right < sLength and s[left] == s[right]):
            left -= 1
            right += 1
        
        # Since the above is a while loop, i-=1 and j+=1 happened 1 extra time
        start = left+1 ; end = right-1
        length = end-start+1 
        # => length =  j-1-(i+1)+1 = j-i-1
        
        return (length, start, end)
