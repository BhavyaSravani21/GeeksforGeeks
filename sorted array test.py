#User function Template for python3

class Solution:
    ##Complete this function
    def searchInSorted(self,arr, k):
        #Your code here
        low=0
        high=len(arr)-1
        while(low<=high):
            mid=(low+high)//2
            if(arr[mid]==k):
                return True
            elif(arr[mid]>k):
                high=mid-1
            else:
                low=mid+1
        return False
