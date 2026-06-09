class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        Set<Integer> s1=new HashSet<>();
        for(int n:nums){
            s1.add(n);
        }
        List<Integer> l1=new ArrayList<>();
        for(int i=1;i<=nums.length;i++){
            if(!s1.contains(i)){
                l1.add(i);
            }
        }
        return l1;
    }
}