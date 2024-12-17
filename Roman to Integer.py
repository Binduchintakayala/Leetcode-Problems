def romanToInt(s):
    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    total = 0 
    for i in range(len(s) - 1):  
        current_value = roman_dict[s[i]]
        next_value = roman_dict[s[i + 1]]
        if current_value < next_value:
            total -= current_value
        else:
            total += current_value
    total += roman_dict[s[-1]]
    
    return total
s1 = "III"
print(romanToInt(s1)) 
s2 = "LVIII"
print(romanToInt(s2))  
s3 = "MCMXCIV"
print(romanToInt(s3))  
