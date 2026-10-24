class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        arr = []
        for i in range(0, len(nums)):
            hashset1 = set()
            hashset2 = set()
            hashset1.update(nums[0:i+1])
            hashset2.update(nums[i+1:len(nums)+1])
            arr.append(len(hashset1) - len(hashset2))

        return arr
