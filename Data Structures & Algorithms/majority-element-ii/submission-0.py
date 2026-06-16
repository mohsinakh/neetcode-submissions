class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)//3
        res = []
        # print(n)
        h = {}
        for num in nums:
            if num in h.keys():
                h[num]+=1
            else:
                h[num]=1
        for key,val in h.items():
            if val > n:
                res.append(key)
        return res       