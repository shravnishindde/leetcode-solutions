class Solution(object):
    def removeAnagrams(self, words):
        r=[]
        prev=""
        for word in words:
            pres=''.join(sorted(word))
            if pres!=prev:
                r.append(word)
                prev=pres
        return r
        