class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cs=set()
        mlen=0
        left=0
        for right in range(len(s)):
            while s[right] in cs:
                cs.remove(s[left])
                left+=1
            cs.add(s[right])
            mlen=max(mlen,right-left+1)
        return mlen