class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        count_s1 = [0] * 26
        count_window = [0] * 26

        for char in s1:
            count_s1[ord(char)-ord('a')] += 1

        l = 0
        for r in range(len(s2)):
            count_window[ord(s2[r]) - ord('a')] += 1

            if (r-l+1) > len(s1):
                count_window[ord(s2[l]) - ord('a')] -= 1
                l += 1
            if count_window == count_s1:
                return True
        return False

