# attempt
class Solution:
    def myAtoi(self, str: str) -> int:
        if not str:
            return 0
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        ans = ''
        for _ in str:
            if _ == ' ' and ans == '':
                continue
            elif (_ == '-' or _ == '+') and ans == '':
                ans += _
            elif not _.isdigit() and ans == '':
                return 0
            elif _.isdigit():
                ans += _
            elif not _.isdigit() and ans != '':
                break
        if ans == '-' or ans=='+' or ans=='':
            return 0
        num = int(ans)
        if num > INT_MAX:
            return INT_MAX
        elif num < INT_MIN:
            return INT_MIN
        else:
            return num

# optimal
class Solution(object):
    def myAtoi(self, s):
        """
        :type str: str
        :rtype: int
        """
        ###better to do strip before sanity check (although 8ms slower):
        #ls = list(s.strip())
        #if len(ls) == 0 : return 0
        if len(s) == 0 : return 0
        ls = list(s.strip())

        sign = -1 if ls[0] == '-' else 1
        if ls[0] in ['-','+'] : del ls[0]
        ret, i = 0, 0
        while i < len(ls) and ls[i].isdigit() :
            ret = ret*10 + ord(ls[i]) - ord('0')
            i += 1
        return max(-2**31, min(sign * ret,2**31-1))

# basically if-else practice, attention to details
# optimal is cleaner than my code, more compact
