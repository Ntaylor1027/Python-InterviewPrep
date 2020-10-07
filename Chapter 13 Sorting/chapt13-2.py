# Given 2 sorted arrays and one has enough space to hold the other merge them


def merge_two_sorted_arrays(A, m, B, n):
    # Algorithm: Backwards traverse both arrays and place largest
    # value in the back
    a, b, write_idx = m-1, n-1, m+n-1
    while a >= 0 and b >= 0:
        if A[a] > B[b]:
            A[write_idx] = A[a]
            a -= 1
        else:
            A[write_idx] = B[b]
            b -= 1
        write_idx -= 1
    while b >= 0:
        A[write_idx] = B[b]
        write_idx, b = write_idx - 1, b - 1
