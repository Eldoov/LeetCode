# 268. Missing Number

def solution(nums):
    hSet = set(nums)
    print(hSet, len(nums))
    for i in range(len(nums)+1):
        if i not in hSet:
            return i


arr = [0,1]
print(solution(arr))


