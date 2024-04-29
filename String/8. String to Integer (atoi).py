# 8. String to Integer (atoi)

def solution(strs):
    res = ""
    leading_space, j = True, 0
    if strs == '':
        return 0
    # remove leading space
    while leading_space and j <= len(strs):
        for i in strs:
            if i != ' ':
                strs = strs[j:len(strs)]
                leading_space = False
                break
            j += 1
    if strs == '':
        return 0
    negative = False
    j = 0
    # check neg pos
    for i in strs:
        if i == ' ':
            break
        if j == 0 and (i != '-' and i != '+'):
            if not i.isdigit():
                break
        if i == "-" and j+1 < len(strs):
            if j != len(strs) and strs[j+1].isdigit():
                negative = True
            if strs[j+1] == "+":
                break
        if i == "+" and j + 1 < len(strs):
            if strs[j+1] == "-":
                break
        if i.isdigit():
            res += i
            if j+1 >= len(strs):
                break
            else:
                if not strs[j+1].isdigit():
                    break
        j += 1

    max = (2 ** 31) - 1
    min = -(2 ** 31)
    if res != '':
        res = int(res)
        if negative:
            res *= -1
        print(res)
        if res > max:
            res = max
        if res < min:
            res = min
    else:
        res = 0

    return res


def solution2(s):
    res = ''
    Negative = False
    s = s.strip(" ")
    if s == '':
        return 0

    if s[0] == '-' and len(s) >= 1:
        Negative = True
        s = s[1:len(s)]
    if s[0] == '+' and len(s) >= 1:
        s = s[1:len(s)]

    for i in range(len(s)):
        if s[i].isdigit():
            res += s[i]
            if i+1 < len(s):
                if not s[i + 1].isdigit():
                    break
        else:
            break

    if res != '':
        res = int(res)
        if Negative:
            res *= -1
        max = (2 ** 31) - 1
        min = -(2 ** 31)
        if res > max:
            res = max
        elif res < min:
            res = min
    else:
        return 0

    return res


a = "4193 with words"
b = '  -3'
c = '--111---'
d = "-91283472332"
e = "words and 987"
f = " +4"
print(solution2(f))