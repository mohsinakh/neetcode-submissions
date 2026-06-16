class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)//3
        res = set()
        # print(n)
        h = {}
        for num in nums:
            if num in h.keys():
                h[num]+=1
            else:
                h[num]=1
            if h[num]>n:
                res.add(num)
        return list(res)  
          