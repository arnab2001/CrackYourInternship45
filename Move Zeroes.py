class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
    
        """
        c=0
        i=0
        while(i<len(nums)-1):
            if nums[i]==0:
                nums.pop(i)
                nums.append(0)
                c+=1
                if c>len(nums):
                    break
            else:
                i+=1
            if c>len(nums):
                break
                
        return nums        
        
