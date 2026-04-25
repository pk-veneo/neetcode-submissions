class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        x = 0
        y = len(numbers) - 1

        while x < y:
            total = numbers[x] + numbers[y]
            if total > target:
                y = y-1
            elif total < target:
                x = x+1
            else:
                return [x+1, y+1]
        