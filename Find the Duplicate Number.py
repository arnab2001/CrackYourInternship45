class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0
        
        while i < len(nums):
            
            index = nums[i]
            if nums[index - 1] == index:
                i += 1
            else:
                nums[i], nums[index - 1] = nums[index - 1], nums[i]
        
        for j in range(len(nums)):
            if nums[j] != j + 1:
                return nums[j]
        return - 1
