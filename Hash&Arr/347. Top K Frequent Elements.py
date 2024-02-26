# 347. Top K Frequent Elements

def solution(nums, k):
    hMap = {}
    for i in range(len(nums)):
        if nums[i] in hMap:
            hMap[nums[i]] += 1
        else:
            hMap[nums[i]] = 1
    sortedMap = sorted(hMap.items(), key=lambda x:x[1])
    l = list(dict(sortedMap).keys())
    l.reverse()
    res = []
    for i in range(k):
        res.append(l[i])
    return res


def solution2(nums, k):
    count = {}
    freq = [[]for i in range(len(nums))]

    for n in nums:
        count[n] = 1 + count.get(n, 0)
    for n, c in count.items():
        freq[c].append(n)
    res = []
    for i in range(len(freq)-1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res
    return res




a = [1, 1, 1, 2, 2, 3, 4, 4, 4]
b = [-1,-1]
c = [1,1,1,2,2,3]
print(solution(b, 1))
