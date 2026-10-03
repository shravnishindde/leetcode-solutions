class Solution:
    def canJump(self, nums: list[int]) -> bool:
        max_reach=0
        for i in range(len(nums)):
            if i > max_reach:
                return False
            cur_reach=i+nums[i]
            if cur_reach > max_reach:
                max_reach=cur_reach
        return True        