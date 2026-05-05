class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        keys = [0,1,2]
        count = defaultdict(int)
        for i in nums:
            count[i] += 1
        i = 0
        for key in keys:
            if key in count:
                while count[key]>0:
                    # print(key ,i)
                    nums[i] = key
                    count[key]-=1
                    i+=1
           