class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        ans=[]
        csum=0
        for i in range(0,len(nums)):
            csum+=nums[i]
            ans.append(csum)
        return ans
           
        