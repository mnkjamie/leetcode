class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        idx = 0
        ans = 0
        while idx < len(s):
            # subtract case
            if idx+1 < len(s) and values[s[idx]] < values[s[idx+1]]:
                ans += values[s[idx+1]] - values[s[idx]]
                idx += 2
            # normal
            else:
                ans += values[s[idx]]
                idx += 1
        return ans

# think of how to divide the problem into subproblems based on problem definition
# in this case, either add normally, or subtract first and add - 2 cases
