class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        bill5=bill10=bill20=0
        if bills[0]!=5:
            return False
        for i in range(len(bills)):
            if bills[i]==5: 
                bill5+=1

            elif bills[i]==10:
                if bill5!=0:
                    bill5-=1
                    bill10+=1
                else:
                    return False
            elif bills[i]==20:
                
                if bill5>0 and bill10>0:
                    bill5=bill5-1
                    bill10-=1
                    bill20+=1
                elif bill5>2:
                    bill5=bill5-3
                    bill20+=1    
                else:
                     return False

        return True                    




            
        