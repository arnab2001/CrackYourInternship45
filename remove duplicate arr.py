class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        holder = None
        i = 0
        
        for num in nums:
            
            if num == holder:                
                continue                              
                
            holder = num
            nums[i] = num
            i+=1
        
        return i
        
