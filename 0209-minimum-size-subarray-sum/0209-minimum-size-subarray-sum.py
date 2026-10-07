class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        mlen=float('inf')
        left=0
        c_s=0
        for right in range(len(nums)):
            c_s+=nums[right]

            while c_s>=target:
                mlen=min(mlen,right-left+1)
                c_s-=nums[left]
                left+=1
        return mlen if mlen != float('inf') else 0
                  