class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for n,m in enumerate(nums):
            if m == target:
                return n
        return -1
        