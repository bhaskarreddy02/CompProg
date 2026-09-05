class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)

        currmax = nums[0]

        currmin = [0] * n
        currmin[n - 1] = nums[n - 1]

        for i in range(n - 2, -1, -1):
            currmin[i] = min(nums[i], currmin[i + 1])

        for i in range(n):
            currmax = max(nums[i], currmax)

            diff = currmax - currmin[i]

            if diff <= k:
                return i

        return -1
