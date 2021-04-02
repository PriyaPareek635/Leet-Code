class Solution:
    def reverse(self, x: int) -> int:
        y = str(x)
        if y[0] == '-':
            y = y[1:][::-1]
            y = '-' + y
        else:
            y = y[::-1]
        return int(y) if (-2147483647 < int(y) < 2147483647) else 0
            
