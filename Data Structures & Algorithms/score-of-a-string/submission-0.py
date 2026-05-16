class Solution:
    def scoreOfString(self, s: str) -> int:
        i = 0
        res = 0
        for i in range(len(s)-1):
            count = abs(ord(s[i+1]) - ord(s[i]))
            res = res + count

        return res
