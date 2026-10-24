class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        arr1=[]
        n=len(nums)
        count=0
        for i in range(0,n-1):
            arr1.append(sum(nums[0:i+1])-sum(nums[i+1:n]))
            if arr1[i]%2==0:
                count+=1
            else:
                continue

        return count        