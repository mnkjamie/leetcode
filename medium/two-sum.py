# attempt
class Solution:
    def twoSum(self, nums, target):
      h_map = {}
      for idx, val in enumerate(nums):
        n = target - val
        if n not in h_map:
          h_map[val] = idx
        else:
          return [idx, h_map[n]]
