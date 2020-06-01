# attemp
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        row_list = [''] * numRows
        row = 0
        step = 1
        for char in s:
            row_list[row] += char
            if row == 0:
                step = 1
            elif row == numRows - 1:
                step = -1
            row += step
        return ''.join(row_list)

# think of how to do one pass of the string
# in this case, the key was to separate the problem into rows and go char by char, assigning to the right row
# if it seems to complex, probably inefficient
