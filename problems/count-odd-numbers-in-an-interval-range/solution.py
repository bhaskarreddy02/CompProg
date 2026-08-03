class Solution:
    def countOdds(self, low: int, high: int) -> int:

        n=high-low+1

        if n%2==0:
            return floor(n/2)
        else:
            if high%2 or low%2:
                return floor(n/2 +1)
            else:
                return floor(n/2)        