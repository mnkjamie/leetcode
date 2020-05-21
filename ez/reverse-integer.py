# attempt
class Solution:
    def reverse(self, x: int) -> int:
        ans = ''
        if x < 0:
            ans += '-'
        str_x = str(abs(x))
        for i in range(len(str_x)-1, -1, -1):
            ans += str_x[i]
        return int(ans)

# optimal
class Solution:
    def reverse(self, x: int) -> int:
        if x >= 2**31-1 or x <= -2**31: return 0
        else:
            str_x = str(x)
            if x >= 0 :
                rev_x = str_x[::-1]
            else:
                temp = str_x[-1:0:-1]
                rev_x = "-" + temp
            if int(rev_x) >= 2**31-1 or int(rev_x) <= -2**31: return 0
            else: return int(rev_x)

# added restrictions set by problem
# basically same idea, but used string slicing syntax
