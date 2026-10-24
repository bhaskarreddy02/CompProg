class Solution:
    def countMonobit(self, n: int) -> int:
        size=abs(math.log(n+1)/log(2))
        return int(size+1)   