class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i, a in enumerate(nums):

            if i > 0  and nums[i-1] == nums[i]:
                continue
            L = i + 1
            R = len(nums) - 1
            while L < R:
                total = nums[i] + nums[L] + nums[R]

                if total > 0:
                    R = R - 1
                elif total < 0:
                    L = L + 1
                else:
                    res.append([nums[i],nums[L],nums[R]])
                    L += 1
                    R -= 1
                    while L < R and  nums[L-1] == nums[L]:
                        L = L + 1
                    while L < R and nums[R+1] == nums[R]:
                        R = R - 1
        return res
            
