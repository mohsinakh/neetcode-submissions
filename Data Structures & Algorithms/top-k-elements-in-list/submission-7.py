class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        for i in nums:
            count[i]+=1

        arr = []   
        for num, cnt in count.items():
            arr.append([cnt,num])
        arr.sort()
        res = []
        while k:
            res.append(arr.pop()[1])
            k-=1
        return res
            
       
