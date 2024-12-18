def letterCombinations(digits):
    if not digits:
        return []
    digit_to_letters = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    result = []
    def backtrack(index, current_combination):
        if index == len(digits):
            result.append(current_combination)
            return
        current_digit = digits[index]
        letters = digit_to_letters[current_digit]
        for letter in letters:
            backtrack(index + 1, current_combination + letter)
    backtrack(0, "")
    return result
digits1 = "23"
print(letterCombinations(digits1))
digits2 = ""
print(letterCombinations(digits2))
digits3 = "2"
print(letterCombinations(digits3))
