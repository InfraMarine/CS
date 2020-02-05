import sys

def to64Char(x):
    if x < 26:
        return chr(x + ord('A'))
    if x < 52:
        return chr(x - 26 + ord('a'))
    if x < 62:
        return chr(x - 52 + ord('0'))
    if x == 62:
        return '+'
    return '/'

def toBase(filename):
    res = ""
    with open(filename, "rb") as f:
        chunk = f.read(3)
        while chunk != b"":
            n = len(chunk)
            conca = int.from_bytes(chunk, "big") << (3 - n) * 2
            for i in range(n + 1):
                res += to64Char(conca >> 6 * (3 - i) & 63)
            chunk = f.read(3)
    res += '=' * (3 - n)
    return res

if len(sys.argv) == 2:
    filename = sys.argv[1]
    with open("encoded_%s" % filename, 'w', encoding="utf8") as wf:
        wf.write(toBase(filename))

    