class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        for char in s:        # checks from s[0] to s[n-1]
            if char not in t: # if the character is not present in t, return False
                return False
            t = t.replace(char, "", char.index(char) + 1) # removes the first occurrence of the character from t, so that it is not counted again
            print(t)
        return True

s = "anagram"
t = "nagaram"
print(Solution().isAnagram(s, t)) # True

s = "rat"
t = "car"
print(Solution().isAnagram(s, t)) # False


# Doubt ?
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        for char in s:
            if char not in t:
                return False
            t = t.replace(char, "", 1)
        return True
 

