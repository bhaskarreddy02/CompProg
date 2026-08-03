class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left=int(c**0.5)
        right=0

        while(left>=right):
            if(left**2 +right**2 >c ):
                left=left-1
            elif(left**2 +right**2 <c):
                right=right+1
            else:
                return True 

        return False              

        