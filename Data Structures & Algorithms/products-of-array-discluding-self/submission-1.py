class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod , count0= 1, 0
        res= []

        for num in nums:
            if num:
                prod *= num
            else:
                count0+=1
        print(prod)
        if count0>1:
            res = [0 for _ in range(len(nums))]
            return res
        for num in nums:
            if num and count0:
                res.append(0)   
            elif num:
                res.append(prod//num)
            else:
                res.append(prod)


        return res