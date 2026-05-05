#User function Template for python3

class Solution:
    def convertMinToMaxHeap(self, N, arr):
        def max_heapify(i):
            largest = i
            left = 2*i + 1
            right = 2*i + 2
            
            if left < N and arr[left] > arr[largest]:
                largest = left
                
            if right < N and arr[right] > arr[largest]:
                largest = right
                
            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]
                max_heapify(largest)
        
        # Start from last non-leaf node
        for i in range(N//2 - 1, -1, -1):
            max_heapify(i)
        
