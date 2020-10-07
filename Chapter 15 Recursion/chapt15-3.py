def permutations(A):
    def directed_permutations(i):
        if i == len(A)-1:
            result.append(A.copy())
            return

        # Try every possibility for A[i]
        for j in range(i, len(A)):
            A[i], A[j] = A[j], A[i]
            # Generate all permutations for A[i + 1:]
            directed_permutations(i+1)
            A[i], A[j] = A[j], A[i]  # Correct A format
    result = []
    directed_permutations(0)
    return result


if __name__ == "__main__":
    print(permutations([1, 2, 3, 4]))
