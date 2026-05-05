class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0]*3
        for i in nums:
            count[i] += 1
        i = 0
        for key in range(3):
            while count[key]:
                # print(key ,i)
                nums[i] = key
                count[key]-=1
                i+=1
        