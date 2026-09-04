class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        if len(nums)==1:
            return 0
        for i in range(len(nums)):
            diff=max(nums[:i+1]) - min(nums[i:])
            if diff <= k:
                return i
        return -1        
   
            
        