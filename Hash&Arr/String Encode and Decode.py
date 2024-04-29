# String Encode and Decode

def encode(arr):
    res = ""
    for word in arr:
        res += str(len(word)) + "#" + word
    return res


def decode(s):
    res = []
    i = 0

    while i < len(s):
        j = i
        while s[j] != '#':
            j += 1
        length = int(s[i:j])
        i = j + 1
        j = i + length
        res.append(s[i:j])
        i = j
    return res


e1 = ["neet", "code", "love", "you"]
e2 = ["The quick brown fox","jumps over the","lazy dog","1234567890","abcdefghijklmnopqrstuvwxyz"]
e3 = ["","   ","!@#$%^&*()_+","LongStringWithNoSpaces","Another, String With, Commas"]
e4 = ["String with new\nline","Another\nLine","And\nOne\nMore"]
d1 = encode(e3)
print(d1)
print(decode(d1))
