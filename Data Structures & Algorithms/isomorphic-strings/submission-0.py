class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        stot = {}
        ttos = {}

        for i,j in zip(s,t):
            if i in stot and stot[i] != j:
                return False
            if j in ttos and ttos[j] != i:
                return False

            stot[i] = j
            ttos[j] = i
        return True
                