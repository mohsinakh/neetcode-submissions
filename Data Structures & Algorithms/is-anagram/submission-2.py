from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        s1 = defaultdict(int)
        for i in range(len(s)):
            s1[s[i]]+=1
            s1[t[i]]-=1
    
        for value in s1.values():
            if value!=0:
                return False
        return True