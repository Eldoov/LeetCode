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


def solution2(nums):
    pre, post, res = [1], [1], []
    x, y = 1, 1
    for i in range(len(nums)-1):
        x *= nums[i]
        pre.append(x)
    for i in range(len(nums)-1, 0, -1):
        y *= nums[i]
        post.append(y)
    post.reverse()
    for i in range(len(nums)):
        n = pre[i] * post[i]
        res.append(n)
    return res



a = [1, 2, 3, 4]
b = [-1, 1, 0, -3, 3]
c = [-1,-1,1,-1,-1,1,-1,-1,-1,1,1,-1,1,1,1,1,-1,1,1,-1,-1,1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,-1,1,1,-1,-1,1,-1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,-1,1,1,1,-1,1,-1,-1,-1,-1,1,1,1,-1,1,1,-1,1,1,-1,1,-1,-1,-1,1,-1,1,-1,1,1,1,1,1,-1,1,-1,1,-1,-1,-1,1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,1,-1,1,1,1,-1,1,1,-1,-1,1,1,-1,1,-1,1,1,-1,-1,1,-1,-1,-1,1,1,1,1,-1,1,1,-1,-1,1,1,1,-1,1,-1,1,-1,-1,1,-1,1,-1,1,-1,1,-1,1,1,1,-1,1,1,1,1,-1,-1,1,-1,1,1,1,1,1,-1,1,-1,1,-1,-1,-1,1,1,1,1,-1,-1,1,-1,-1,-1,1,1,-1,1,-1,-1,1,-1,1,-1,-1,1,1,-1,-1,-1,1,1,-1,1,1,-1,-1,-1,1,1,1,-1,1,-1,1,1,-1,-1,-1,-1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1,-1,-1,1,1,-1,1,-1,1,-1,1,-1,1,-1,1,1,1,1,-1,1,-1,-1,-1,1,1,-1,1,1,1,-1,1,-1,-1,-1,1,1,1,1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,-1,1,1,-1,-1,-1,1,1,1,-1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,1,-1,-1,1,1,1,-1,-1,1,1,1,-1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1,1,1,1,1,-1,1,1,1,-1,1,-1,1,1,1,1,1,1,-1,1,-1,1,1,1,-1,1,-1,-1,1,1,1,-1,1,1,-1,1,-1,1,1,-1,1,1,1,-1,1,1,1,1,1,-1,-1,1,1,1,1,-1,1,1,1,-1,-1,-1,-1,1,-1,-1,-1,1,1,-1,-1,1,-1,-1,-1,1,1,1,-1]
print(solution2(c))
