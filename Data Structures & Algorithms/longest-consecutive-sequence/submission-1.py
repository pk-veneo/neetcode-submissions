class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num = set(nums)
        x = 0

        for i in num:
            if i-1 not in num:
                length = 1

                while i + length in num:
                    length += 1
                x = max(x,length)
        return x
