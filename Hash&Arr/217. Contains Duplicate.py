# 217. Contains Duplicate

def containsDuplicate(nums):
    for x in range(0, len(nums)-1):
        print('x=', x)
        for y in range(x+1, len(nums)):
            print('y=', y)
            if nums[x] == nums[y]:
                return True
    return False

def hashSet(nums):
    hashset = set()
    for x in nums:
        if x in hashset: return True
        hashset.add(x)
    return False


arr = [1, 2, 3, 1]
print(hashSet(arr))

arr = [1, 2, 3, 4]
print(hashSet(arr))

arr = [1,1,1,3,3,4,3,2,4,2]
print(hashSet(arr))