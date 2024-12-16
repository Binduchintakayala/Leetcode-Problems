def myAtoi(s: str) -> int:
    INT_MIN = -2**31
    INT_MAX = 2**31 - 1
    s = s.lstrip()
    if not s:
        return 0
    sign = 1  
    if s[0] == '-':
        sign = -1
        s = s[1:]
    elif s[0] == '+':
        s = s[1:]
    result = 0
    for char in s:
        if char.isdigit():
            result = result * 10 + int(char)
        else:
            break  
    result *= sign
    if result < INT_MIN:
        return INT_MIN
    if result > INT_MAX:
        return INT_MAX
    return result
s1 = "42"
print(myAtoi(s1)) 
s2 = " -042"
print(myAtoi(s2))  
s3 = "1337c0d3"
print(myAtoi(s3))  
s4 = "0-1"
print(myAtoi(s4))  
s5 = "words and 987"
print(myAtoi(s5))  











