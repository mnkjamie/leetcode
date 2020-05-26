# attempt
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = []
        longest = []
        for char in s:
            if char not in visited:
                visited.append(char)
            else:
                if len(visited) > len(longest):
                    longest = visited
                new_start = visited.index(char)
                visited = visited[new_start+1:]
                visited.append(char)
        return max(len(longest), len(visited))

# optimal
def lengthOfLongestSubstring(self, s):
    """
    :type s: str
    :rtype: int
    """

    str_list = []
    max_length = 0

    for x in s:
        if x in str_list:
            str_list = str_list[str_list.index(x)+1:]

        str_list.append(x)
        max_length = max(max_length, len(str_list))

    return max_length

# very similar, but thought it was much cleaner and easier to understand the process
