def convertIntegerToRoman(num):
    holder=[
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I")
    ]
    res=""
    for value, symbol in holder:
        while num>=value:
            num-=value
            res+=symbol

    return res


def convertRomanToInteger(s):
    holder={
        "M":1000,
        "D":500,
        "C":100,
        "L":50,
        "X":10,
        "V":5,
        "I":1
    }

    res2=0
    for i in range(len(s)-1):
        if holder[s[i]]<holder[s[i+1]]:
            a=holder[s[i]]*-1
            res2+=a
        else:
            res2+=holder[s[i]]
    res2+=holder[s[len(s)-1]]
    return res2
# ss="MCCCLXXIX"
# print(convertRomanToInteger(ss))




num = 1379
print(convertIntegerToRoman(num))
