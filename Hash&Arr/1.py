# 1 Two Sum

def getSum(nums: list[int], target: int) -> list[int]:
    hMap = {}
    for i in range(len(nums)):
        x = target - nums[i]
        if x not in hMap:
            hMap[nums[i]] = i
        else:
            return [hMap[x], i]


a = [1, 2, 2, 9, 6]
b = 10
print(getSum(a, b))