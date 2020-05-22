# attemp
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) < 1:
            return ''
        elif len(strs) == 1:
            return strs[0]
        shortest = min(strs, key=len)
        ans = ''
        words = len(strs)
        same = True
        for i in range(len(shortest)):
            cur_letter = strs[0][i]
            cur_word = 1
            while cur_word < words:
                if strs[cur_word][i] != cur_letter:
                    same = False
                    break
                cur_word += 1
            if same:
                ans += cur_letter
            else:
                break
        return ans


# make sure to account for empty or possibly invalid inputs
# don't make assumptions (I assumed there had to be at least 2 words after getting first error)
# longest prefix can only be as long as the shortest string in list
