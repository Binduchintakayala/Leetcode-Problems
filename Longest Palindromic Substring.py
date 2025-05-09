def longestPalindrome(s):
    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]
    if len(s) <= 1:
        return s
    longest = ""
    for i in range(len(s)):
        palindrome1 = expand_around_center(i, i)
        palindrome2 = expand_around_center(i, i + 1)

        longest = max(longest, palindrome1, palindrome2, key=len)

    return longest
s1 = "babad"
print(longestPalindrome(s1)) 
s2 = "cbbd"
print(longestPalindrome(s2))










