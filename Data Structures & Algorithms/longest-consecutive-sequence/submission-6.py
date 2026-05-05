class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        s = set()
        longest = 1
        for num in nums:
            s.add(num)
        
        nums = sorted(s)
        i=0
        # print(nums)
        while i<len(nums):
            j= i+1
            while j<len(nums) and  nums[j] - nums[j-1] == 1:
                # print(nums[i],nums[j])
                longest = max(longest, j-i+1)
                j+=1
          
            i+=1
        return longest
