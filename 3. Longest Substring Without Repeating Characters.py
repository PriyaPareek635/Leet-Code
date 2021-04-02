class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        mx=len(set(s))
        a=''
        ans=0
        for i in s:
            if i not in a:
                a+=i
            else:
                x=a.index(i)+1
                a=a[x:]
                a+=i
            ans=max(ans,len(a))
            if ans==mx:
                break
        return ans
        
