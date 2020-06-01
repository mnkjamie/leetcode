# attempt
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        water = 0
        while left < right:
            water = max(water, (right-left)*min(height[left], height[right]))
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return water

# think about how to approach problem most efficiently
# how the problem changes as you go through it
# in this case, water can only increase by eliminating the shorter rod
