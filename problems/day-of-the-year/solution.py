class Solution:
    def dayOfYear(self, date: str) -> int:
        dayslist=[31,28,31,30,31,30,31,31,30,31,30,31]
        month=int(date[5:7])
        rawdays=int(date[8:10])
        
        count=0
        for i in dayslist[0:month-1]:
            count=count+i
        if month>2:    
            return count+rawdays+self.isleapyear(date)
        else:
            return count+rawdays        
    def isleapyear(self, date: str)->int:
        year=int(date[0:4])
        if year%4==0 and year%100!=0 or year%400==0 :
            return 1
        else:
            return 0    

            
        