class Solution {
    public int binaryGap(int n) {
        int c=0;
        int m=0;
       
        boolean f=false;
        while(n!=0)
        {
            int b=n%2;
            if(b==1){
               if(f){
                m=Math.max(m,c);
               }
               c=1;
               f=true;
            }else{
                if(f){
                    c++;
                }
            }
            n=n/2;
        }
return m;      
}
}