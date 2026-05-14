class Solution {
    public boolean isGood(int[] nums) {

        Arrays.sort(nums);

        int n = nums.length;

        // Check 1 to n-1
        for(int i = 0; i < n - 1; i++) {

            if(nums[i] != i + 1)
                return false;
        }

        // Last element should be n-1
        return nums[n - 1] == n - 1;
    }
}