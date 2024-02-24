# 49 Group Anagrams
from collections import defaultdict


def groupAnagrams(strs):
    hMap = defaultdict(list)

    for w in strs:
        count = [0] * 26
        for c in w:
            num = ord(c) - ord('a')
            count[num] += 1
        hMap[tuple(count)].append(w)

    lst = list(hMap.values())
    print(lst)


def groupAnagrams2(strs):
    hMap = {}
    for word in strs:
        sorted_word = "".join(sorted(word))
        if sorted_word in hMap:
            hMap[sorted_word].append(word)
        else:
            hMap[sorted_word] = [word]
    print(list(hMap.values()))

a = ["eat","tea","tan","ate","nat","bat"]
b = ['eat', 'ate', 'tan']
groupAnagrams2(a)
