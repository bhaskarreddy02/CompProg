class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        sum=0
        g.sort()
        s.sort()
        for i in range(min(len(g),len(s))):
            if g[i]<=s[i]:
                sum=sum+1

        return sum        


        