class Solution:
    def checkDivisibility(self, n: int) -> bool:
        ds=t=0
        dp=1
        n1=n
        while n>0:
            t=n%10
            ds+=t
            dp*=t
            n=n//10
        return n1%(ds+dp)==0
           
        
            
        