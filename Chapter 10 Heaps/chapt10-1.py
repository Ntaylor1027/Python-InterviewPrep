import heapq
import unittest
import functools
import collections


def mergeSortedFiles(sorted_arrays):
    min_heap = []
    sorted_arrays_iters = [iter(x) for x in sorted_arrays] # create iterators for each array
    for i, it in enumerate(sorted_arrays_iters): # append first element of each array and the index of the array
        first_element = next(it, None)
        if first_element is not None:
            heapq.heappush(min_heap, (first_element,i))
    
    result = []
    while min_heap: 
        smallest_entry, smallest_array_i = heapq.heappop(min_heap) # Grab smallest element in heap and iterator index
        smallest_array_iter = sorted_arrays_iters[smallest_array_i] # Grab the iterator for smallest element
        result.append(smallest_entry) # append smallest entry
        next_element = next(smallest_array_iter,None) # Grab the next element in the iterator
        if next_element is not None:
            heapq.heappush(min_heap, (next_element,smallest_array_i)) # Append next_element to our min heap
    return result



class TestMergeSortedFiles(unittest.TestCase):
    def test_mergeSortedFiles(self):
        sa = [[3, 5, 7], [0, 6], [0, 6, 28]]
        self.assertEqual(mergeSortedFiles(
            sa), [0, 0, 3, 5, 6, 6, 7, 28], "Should be [0, 0, 3, 5, 6, 6, 7, 28]")


if __name__ == '__main__':
    unittest.main()
