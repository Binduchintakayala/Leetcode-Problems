def isValid(s: str) -> bool:
    bracket_map = {')': '(', '}': '{', ']': '['}
    stack = []
    for char in s:
        if char in bracket_map:
            top_element = stack.pop() if stack else '#'
            if bracket_map[char] != top_element:
                return False
        else:
            stack.append(char)
    return not stack
s1 = "()"
print(isValid(s1))
s2 = "()[]{}"
print(isValid(s2))  
s3 = "(]"
print(isValid(s3))  
s4 = "([])"
print(isValid(s4))  



