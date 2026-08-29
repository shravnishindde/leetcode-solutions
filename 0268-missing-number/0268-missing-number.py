class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        csum=sum(nums)
        n=len(nums)
        e_sum=n*(n+1)/2
        return int(e_sum-csum)
        