from ast import Str
import sys

maxArg = 5
argLen = len(sys.argv) - 1
if argLen < 1:
    print ("몰?루")
    args = ["몰?루"]
elif argLen > maxArg:
    print ("넘모많당!")
    sys.exit(1)
else:
    print("ㅋㅋ루삥뽕")
    args = sys.argv[1:maxArg]


def strToASCII(str):
    char_values = []
    ascii_values = []
    for character in str:
        char_values.append(character)
        ascii_values.append(ord(character))
    return char_values ,ascii_values

def factorization(x):
    factors =[]
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
            # print("ㅋ", end='')
        ㅋStr = ㅋStr + "ㅌ"
        # print("ㅌ", end='')
    return ㅋStr
    # print()
    

f = open("ㅋㅌ루삥뽕.astv", 'w', encoding="UTF-8")

f.write("쿠쿠루삥뽕\n")
for i, arg in enumerate(args):
    charArr, asciiArr = strToASCII(arg)
    for idx, code in enumerate(asciiArr):
        asserLine = "우짤래미" + charArr[idx] +"~"
        ㅋStr=mkAsserStr(factorization(code))

        f.write(asserLine)
        f.write(ㅋStr)
        f.write("\n")
        f.write("ㅇㅉ" + charArr[idx] + "\n\n")
f.write("슉슈슉슉")
f.close()

