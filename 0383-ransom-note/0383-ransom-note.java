class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        HashMap<Character,Integer> hm=new HashMap<>();
        for(char c:magazine.toCharArray())
        {
            hm.put(c,hm.getOrDefault(c,0)+1);
        }
        for(char s:ransomNote.toCharArray())
        {
            if(!hm.containsKey(s) ||  hm.get(s) == 0)
            return false;
            hm.put(s,hm.getOrDefault(s,0)-1);

        }
        return true;
    }
}