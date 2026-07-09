class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        c=0
        b=[0]+flowerbed+[0]
        for i in range(1,len(b)-1):
            if b[i-1]==0 and b[i]==0 and b[i+1]==0:
                b[i]=1
                c+=1
        return c>=n
        