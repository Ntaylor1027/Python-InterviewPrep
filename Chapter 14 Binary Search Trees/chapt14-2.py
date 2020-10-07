# Find the first key greater than a given value
# Save last biggest one and try to find the value or first smallest
# return last bigget


def find_first_greater_than_k(tree, k):
    subtree, first_so_far = tree, None
    while subtree:
        if subtree.data > k:
            first_so_far, subtree = subtree, subtree.left
        else:  # Root and all keys in the left subtree are <= k, so skip them
            subtree = subtree.right
    return first_so_far
