def reverse(x):
    INT_MIN = -2**31
    INT_MAX = 2**31 - 1
    sign = -1 if x < 0 else 1
    x = abs(x)  
    reversed_x = int(str(x)[::-1])
    reversed_x *= sign
    if reversed_x < INT_MIN or reversed_x > INT_MAX:
        return 0
    return reversed_x
x1 = 123
print(reverse(x1))  
x2 = -123
print(reverse(x2))  
x3 = 120
print(reverse(x3))  











