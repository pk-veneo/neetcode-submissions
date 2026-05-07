class Solution:

    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        count_s1 = {}
        for char in s1:
            count_s1[char] = count_s1.get(char, 0) + 1

        count_window = {}
        l = 0

        for r in range(len(s2)):
            count_window[s2[r]] = count_window.get(s2[r], 0) + 1

            if r - l + 1 > len(s1):
                count_window[s2[l]] -= 1
                if count_window[s2[l]] == 0:
                    del count_window[s2[l]]
                l += 1

            if count_window == count_s1:
                return True

        return False
            