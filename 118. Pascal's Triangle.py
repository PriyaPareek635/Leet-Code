class Solution(object):
    def generate(self, numRows):
        ans = []
        for i in range(numRows):
            row = [1]*(i+1)
            if len(row)>2:
                for k in range(1, len(row)-1):
                    row[k] = ans[-1][k-1] + ans[-1][k]
            ans.append(row)
        return ans
