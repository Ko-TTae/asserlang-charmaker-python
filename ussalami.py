from ast import Str
import sys

# TODO: argv 값에서 asserlang 예약어 예외처리
maxArg = 5
argLen = len(sys.argv) - 1
if argLen < 1:
    print("몰?루")
    args = ["몰?루"]
elif argLen > maxArg:
    print("넘모많당!")
    sys.exit(1)
else:
    print("ㅋㅋ루삥뽕")
    args = sys.argv[1:maxArg+1]


def strToASCII(str):
    char_values = []
    ascii_values = []
    for character in str:
        char_values.append(character)
        ascii_values.append(ord(character))
    return char_values, ascii_values


def factorization(x):
    factors = []
    d = 2
    while d <= x:
        if x % d == 0:
            factors.append(d)
            x = x / d
        else:
            d = d + 1
    return factors


def mkAsserStr(factors):
    ㅋStr = ""
    for factor in factors:
        for i in range(factor):
            ㅋStr = ㅋStr + "ㅋ"
        ㅋStr = ㅋStr + "ㅌ"
    return ㅋStr[:-1]


allStr = "".join(args)
atomizedStr = "".join(dict.fromkeys(allStr))
charArr, asciiArr = strToASCII(atomizedStr)

f = open("ㅋㅌ루삥뽕.astv", 'w', encoding="UTF-8")

f.write("쿠쿠루삥뽕\n")
for idx, code in enumerate(asciiArr):
    asserLine = "우짤래미" + charArr[idx] + "~"
    ㅋStr = mkAsserStr(factorization(code))
    f.write(asserLine + ㅋStr + "\n")

for arg in args:
    ㅇㅉStr = "ㅇㅉ"
    for char in arg:
        ㅇㅉStr = ㅇㅉStr + char + " "
    ㅇㅉStr = ㅇㅉStr[:-1]
    f.write(ㅇㅉStr + "\n")
f.write("슉슈슉슉")

f.close()
