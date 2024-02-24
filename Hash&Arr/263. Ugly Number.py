# 263. Ugly Number

def solution(n):
    if n == 0:
        return False
    for p in [2,3,5]:
        while n % p == 0:
            n = n // p
    return n == 1


arr = [20, 14, 56, 200]
for i in range(len(arr)):
    print(solution(arr[i]))