class Solution:
    def isPalindrome(self, s: str) -> bool:
        text=s.replace(" ","").lower()
        print(text)
        l=0
        r=len(text)-1
        while l<r:
            if not text[l].isalnum():
                l=l+1
                continue
            if not text[r].isalnum():
                r=r-1
                continue
            if text[l] != text[r]:
                return False
            l=l+1
            r=r-1
        return True