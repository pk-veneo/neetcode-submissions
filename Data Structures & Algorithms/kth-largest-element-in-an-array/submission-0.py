class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        result = sorted(nums)[-(k)]
        return result
