class Solution(object):
    def groupAnagrams(self, strs):
        a_m={}
        for word in strs:
            key=''.join(sorted(word))
            if key not in a_m:
                a_m[key]=[]
            a_m[key].append(word)
        return list(a_m.values())
        