class Solution:
    def maxDifference(self, s: str) -> int:
        freq = {}

        for char in s:
            freq[char] = freq.get(char,0) + 1
        
        max_odd = float('-inf')
        min_even = float('inf')

        for char,value in freq.items():
            if value%2 != 0:
                max_odd = max(max_odd,value)
            else:
                min_even = min(min_even,value)

        return max_odd - min_even
        


        