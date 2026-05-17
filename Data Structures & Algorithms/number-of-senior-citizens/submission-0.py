class Solution:
    def countSeniors(self, details: List[str]) -> int:
        res = 0

        for i in range(len(details)):
            s = details[i]
            age = int(s[-4:-2])

            if age > 60:
                res += 1
        return res