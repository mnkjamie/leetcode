# attempt
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      for i in range(len(nums)):
        for j in range(1, len(nums)):
          if nums[i] + nums[j] == target:
            return [i, j]
      return []

# optimal
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}
        for idx, val in enumerate(nums):
            remaining = target - val
            if remaining in visited:
                return [visited[remaining], idx]
            visited[val] = idx
        return []

# can go through the list once, checking back on previous values
# enumrate to make indexing values easier
