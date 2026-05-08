class Solution:

    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_sorted = sorted(s1)  # sort s1 once

        for i in range(len(s2) - len(s1) + 1):
            # cut a window of s1's size from s2
            window = s2[i : i + len(s1)]

            # sort the window and compare
            if sorted(window) == s1_sorted:
                return True

        return False