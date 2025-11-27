class Solution:
    def binarysearch(self, arr, k):
        # Code Here
        n=len(arr)
        low=0
        high=n-1
        ans=-1
        while(low<=high):
            mid=(low+high)//2
            if (arr[mid]==k):
                ans=mid
                high=mid-1
            elif (arr[mid]<k):
                low=mid+1
            else:
                high=mid-1
        return ans
