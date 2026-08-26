class Solution(object):
    def twoSum(self, nums, target):
        seen = {}  
        
        for i in range(len(nums)):
            comp = target - nums[i]
            
            # If the complement is already in the dictionary, 
            # we found our two indices
            if comp in seen:
                return [seen[comp], i]
            
            # Otherwise, save the current number and its index
            seen[nums[i]] = i

        