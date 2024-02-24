# 219. Contains Duplicates II

def solution(nums, k):
    hMap = {}
    for i in range(len(nums)):
        if nums[i] in hMap:
            j = hMap[nums[i]]
            if abs(i - j) <= k:
                return True
        hMap[nums[i]] = i
    return False


arr=[1,2,3,1,2,3]
k = 3
print(solution(arr, k))
