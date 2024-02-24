# 202 Happy Number

def isHappy(n):
    x = n[0] ** 2
    for i in range(len(n)-1):
        y = n[i+1] ** 2
        x = x+y
    if x == 1:
        return True
    else:
        x = getList(x)
        print(x)
        if len(x) > 10:
            return False
        isHappy(x)


def getList(n):
    l = [0]
    while (n > 0):
        l.append(n%10)
        n = int(n/10)
    l = list(reversed(l))
    return l


def isHappier(n):
    hMap = set()

    while n not in hMap:
        hMap.add(n)
        n = cal(n)
        if n == 1:
            return True
    return False

def cal(n):
    res = 0
    while n > 0:
        tmp = (n % 10) ** 2
        n = int(n / 10)
        res += tmp
    return res


n = 19
print(isHappier(n))

