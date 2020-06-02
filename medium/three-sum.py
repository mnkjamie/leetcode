# attempt
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        trips = []
        length = len(nums)
        nums.sort()
        for i in range(length-2):
            if nums[i] > 0: break
            if i > 0 and nums[i] == nums[i-1]: continue
            left, right = i+1, length -1
            while left < right:
                tot = nums[i] + nums[left] + nums[right]
                if tot > 0:
                    right -= 1
                elif tot < 0:
                    left += 1
                else:
                    trips.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
        return trips

# key was to organize problem where for each number, we wanted to find all other pairs that satisfy the requirements
# sorting the array made this easier as it allowed to use two pointers for bigger/smaller numbers
