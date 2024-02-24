# 290. Word Pattern

def solution(pattern, s):
    p = list(pattern)
    s = s.split()
    if len(p) != len(s):
        return False
    hMap1 = {}
    hMap2 = {}
    for i in range(len(p)):
        if p[i] in hMap1 and hMap1[p[i]] != s[i]:
            return False
        print(p[i])
        if s[i] in hMap2 and hMap2[s[i]] != p[i]:
            return False
        hMap1[p[i]] = s[i]
        hMap2[s[i]] = p[i]
    return True


p = "abba"
s = "dog cat cat fish"

p1 = ['a', 'b', 'b', 'a']
s1 = ['dog', 'cat', 'cat', 'fish']

print(solution(p,s))