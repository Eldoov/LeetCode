# LeetCode 242 Valid Anagram

def isAnagram(self, s, t) -> bool:
    if len(s) != len(t):
        return False
    countS, countT = {}, {}


s = ['e', 'e', 'r', 't']
w = {}

for x in range(len(s)):
    w[s[x]] = 1 + w.get(s[x], 0)
    print(w[s[x]])

