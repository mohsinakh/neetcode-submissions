from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = defaultdict(int)
        for char in s:
            s1[char]+=1
        for char in t:
            if char not in s1:
                return False
            s1[char]-=1
        for value in s1.values():
            if value!=0:
                return False
        return True