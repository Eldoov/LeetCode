# 238. Product of Array Except Self

def solution(nums):
    hMap = {}
    res = []
    for i in range(len(nums)):
        hMap[i] = nums[i]
    for i in range(len(nums)):
        y = 1
        if i in hMap:
            del hMap[i]
            for x in hMap.values():
                y = y * x
            res.append(y)
            hMap[i] = nums[i]
    return res







a = [1, 2, 3, 4]
b = [-1, 1, 0, -3, 3]
print(solution(a))
