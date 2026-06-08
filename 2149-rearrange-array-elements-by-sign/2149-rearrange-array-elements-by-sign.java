class Solution {
    public int[] rearrangeArray(int[] nums) {
        int n=nums.length;
        int[] a=new int[n];
        int p=0;
        int n1=1;
        int i;
        for(i=0;i<n;i++){
            if(nums[i]>0){
                a[p]= nums[i];
                p+=2;
            }
            if(nums[i]<0){
                a[n1]=nums[i];
                n1+=2;
            }
        }
        return a;
    }
}