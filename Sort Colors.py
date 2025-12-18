class Solution:
    def sortColors(self, nums):
        low, mid, high = 0, 0, len(nums) - 1
        
        while mid <= high:
            if nums[mid] == 0:
                # Swap nums[low] and nums[mid] and increment both low and mid
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                # Just move mid forward
                mid += 1
            else:
                # Swap nums[mid] and nums[high] and decrement high
                nums[high], nums[mid] = nums[mid], nums[high]
                high -= 1
