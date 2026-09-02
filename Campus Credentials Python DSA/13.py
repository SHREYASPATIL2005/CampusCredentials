class Solution:
    def romanToInt(self, s: str) -> int:
        sum = 0
        RD = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        for i in range(len(s) - 1, -1, -1):
            if i < len(s) - 1 and s[i + 1] != s[i] and s[i + 1] in RD and s[i] in RD and RD[s[i + 1]] > RD[s[i]]:
                sum -= RD[s[i]]
            else:
                sum += RD[s[i]]

        return sum