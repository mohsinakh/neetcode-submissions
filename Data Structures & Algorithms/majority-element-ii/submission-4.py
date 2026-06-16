from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)//3
        res = set()
        # print(n)
        h = defaultdict(int)
        for num in nums:
            h[num]+=1
            if h[num]>n:
                res.add(num)
        return list(res)  
          