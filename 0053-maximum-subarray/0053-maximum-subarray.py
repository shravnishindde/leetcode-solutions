class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        c_max,max_till_now=0,-inf
        for c in nums:
            c_max=max(c,c_max+c)
            max_till_now=max(max_till_now,c_max)
        return max_till_now

        