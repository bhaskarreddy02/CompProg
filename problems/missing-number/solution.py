class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums2=sorted(nums)
        if len(nums2)==0 or nums2[0]!=0:
            return 0

        for i in range(0,len(nums2)-1):
            
            if nums2[i+1]-nums2[i]!=1:
                return nums2[i]+1
               
            else:
                continue      
        return nums2[-1]+1