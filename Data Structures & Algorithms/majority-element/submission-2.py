from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m = len(nums)//2
        d = defaultdict(int)
        for num in nums:
            d[num]+=1
        for i, value in d.items():
            if value>=m:
                return i
        return 0