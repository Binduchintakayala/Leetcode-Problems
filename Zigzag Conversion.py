def convert(s, numRows):
    if numRows == 1 or numRows >= len(s):
        return s
    rows = [''] * numRows
    current_row = 0
    going_down = False  
    for char in s:
        rows[current_row] += char  
        if current_row == 0 or current_row == numRows - 1:
            going_down = not going_down
        current_row += 1 if going_down else -1
    return ''.join(rows)
s1 = "PAYPALISHIRING"
numRows = 3
print(convert(s1, numRows))  
s2 = "PAYPALISHIRING"
numRows = 4
print(convert(s2, numRows))  
s3 = "A"
numRows = 1
print(convert(s3, numRows))  











