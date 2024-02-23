# 49 Group Anagrams

def groupAnagrams(strs):
    hMap1 = {}
    for i in range(len(strs)):
        str1 = list(strs[i])
        hMap1[i] = str1
        if str1 in hMap1:
            print('b')
        print(hMap1)



a = ["eat","tea","tan","ate","nat","bat"]
b = ['eat', 'ate', 'tan']
groupAnagrams(b)