class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        p_s=defaultdict(int)
        p_ss=0
        c=0
        p_s[0]=1
        for num in nums:
            p_ss+=num
            c+=p_s[p_ss-k]
            p_s[p_ss]+=1
        return c


        