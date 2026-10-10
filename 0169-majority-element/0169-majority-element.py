class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        s1={}
        for num in nums:
            s1[num]=s1.get(num,0)+1
        for key in s1:
            if s1[key] > len(nums)//2:
                return key
        