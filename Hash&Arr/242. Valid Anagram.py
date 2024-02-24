# 242. Valid Anagram

def isAnagram(self, s, t) -> bool:
    if len(s) != len(t):
        return False
    countS, countT = {}, {}


s = ['e', 'e', 'r', 't']
t = ['r', 'e', 'e', 't']
w = {}
v = {}

for i in range(len(s)):
    if s[i] in w:
        w[s[i]] += 1
    else:
        w[s[i]] = 1

    if t[i] in v:
        v[t[i]] += 1
    else:
        v[t[i]] = 1


print(w)
print(v)
print(w == v)



