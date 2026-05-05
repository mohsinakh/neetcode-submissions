class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr , l , mid, r):
            n1 = mid - l + 1
            n2 = r - mid

            L = [0]* n1
            R = [0]* n2

            for i in range(n1):
                L[i] = arr[l + i]
            for j in range(n2):
                R[j] = arr[mid+1+j]


            i , j ,k = 0,0, l
            while i<n1 and j<n2:
                if L[i]>=R[j]:
                    arr[k] = R[j]
                    j+=1
                else:
                    arr[k] = L[i]
                    i+=1
                k+=1

            while i< n1:
                arr[k]= L[i]
                k+=1
                i+=1
        

            while j< n2:
                arr[k] = R[j]
                k+=1
                j+=1


        def merge_sort(arr , l , r):
            if l < r:
                mid = (l+r)//2
                merge_sort(arr , l , mid)
                merge_sort(arr , mid+1, r)
                merge(arr , l , mid , r)

        merge_sort(nums , 0, len(nums)-1)
        return nums