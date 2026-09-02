class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if s[i] in s[:i]:        # check if the character s[i] has appeared before in s
                occur = s.index(s[i]) # get the index of the first occurrence of s[i]

                if t[i] != t[occur]:  # check if the corresponding character in t is the same as the one at the first occurrence
                    return False
            else:
                # check if the character t[i] has appeared before in 
                if t[i] in t[:i]:
                    return False

        return True

s = "egg"
t = "add"
print(Solution().isIsomorphic(s, t)) # True

s = "foo"
t = "bar"
print(Solution().isIsomorphic(s, t)) # False