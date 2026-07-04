class Solution {
    public void Reverse(int[] nums,int s,int e)
    {
        while(s<=e){
            int t= nums[s];
            nums[s]=nums[e];
            nums[e]=t;
            s++;
            e--;
        }
    }
    public void rotate(int[] nums, int k) {
        int n=nums.length;
        k=k%n;
        Reverse(nums,0,n-k-1);
        Reverse(nums,n-k,n-1);
        Reverse(nums,0,n-1);
    }
}