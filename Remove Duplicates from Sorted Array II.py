class Solution:
    def removeDuplicates(self, nums):
        if len(nums) <= 2:  # No duplicates to remove if the list has 2 or fewer elements
            return len(nums)

        i = 2  # Start checking from the third element

        for j in range(2, len(nums)):
            if nums[j] != nums[i - 2]:  # Check if current element is not equal to the one two places before
                nums[i] = nums[j]  # Place it in the valid position
                i += 1  # Move the index for the next valid element

        return i  # The length of the array with valid elements
