import unittest

def quickSort(A):
    def partition(A, low, high):
        pivot = A[high]
        i = low - 1
        for j in range(low, high):
            if A[j] < pivot:
                i+=1
                temp = A[i]
                A[i] = A[j]
                A[j] = temp

        temp = A[i+1]
        A[i+1] = A[high]
        A[high] = temp
        return i + 1

    def quickSortDriver(A, low, high):
        if(low < high):
            pi = partition(A, low, high)
            quickSortDriver(A, low, pi - 1)
            quickSortDriver(A, pi+1, high)
        
    A = quickSortDriver(A, 0, len(A)-1)


    

# Python program for implementation of MergeSort
def mergeSort(arr):
    if len(arr) >1:
        mid = len(arr)//2 # Finding the mid of the array
        L = arr[:mid] # Dividing the array elements 
        R = arr[mid:] # into 2 halves
 
        mergeSort(L) # Sorting the first half
        mergeSort(R) # Sorting the second half
 
        i = j = k = 0
         
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i+= 1
            else:
                arr[k] = R[j]
                j+= 1
            k+= 1
         
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i+= 1
            k+= 1
         
        while j < len(R):
            arr[k] = R[j]
            j+= 1
            k+= 1
    


def bubbleSort(A):
    """
    Description: Loop through array by len(A) times. Each time placing the last item at the correct spot
    """
    for iterator in range(len(A)): 
        less_than = 0
        greater_than = less_than + 1
        while(greater_than < len(A) - iterator):
            if (A[less_than] > A[greater_than]):
                temp = A[less_than]
                A[less_than] = A[greater_than]
                A[greater_than] = temp
            less_than += 1
            greater_than += 1

    return A


class TestSorts(unittest.TestCase):
    def test_quickSort(self):
        a = [1,1,2,2,4,6]
        quickSort(a)
        self.assertEqual(a, [1,1,2,2,4,6], "Should be [1,1,2,2,4,6]")


    def test_mergeSort(self):
        a = [2,2,1,1,6,4]
        mergeSort(a)
        self.assertEqual(a, [1,1,2,2,4,6], "Should be [1,1,2,2,4,6]")

    def test_bubbleSort(self):
        a = [2,2,1,1,6,4]
        self.assertEqual(bubbleSort(a), [1,1,2,2,4,6], "Should be [1,1,2,2,4,6]")

if __name__ == "__main__":
    unittest.main()