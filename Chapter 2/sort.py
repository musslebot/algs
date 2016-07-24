
import math


def insertion_sort(A):
    """ Modify a sequence, in place, such that its elements are in ascending order.
    """
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and key < A[i]:
            A[i+1] = A[i]
            i -= 1
        A[i+1] = key


def reverse_insertion_sort(A):
    """ Modify a sequence, in place, such that its elements are in descending order.
    """
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and key > A[i]:
            A[i+1] = A[i]
            i -= 1
        A[i+1] = key


def selection_sort(A):
    """ Modify a sequence, in place, such that its elements are in ascending order.
    """
    for i in range(0, len(A)-1):
        j = i
        for k in range(i+1, len(A)):
            if A[k] < A[j]:
                j = k
        if j != i:
            key = A[i]
            A[i] = A[j]
            A[j] = key


def merge_sort(A, p=None, r=None):
    """ Modify a sequence, in place, such that its elements are in ascending order.
    """
    def merge(A, p, q, r):
        """ Merge two subsequences of a sequence (defined by indices p, q, and r) in place.
        """
        # Define subsequences
        L = A[p:q+1] + [float("inf")]
        R = A[q+1:r+1] + [float("inf")]
        # Merge
        i = 0
        j = 0
        for k in range(p, r+1):
            if L[i] <= R[j]:
                A[k] = L[i]
                i += 1
            else:
                A[k] = R[j]
                j += 1
    if p is None:
        p = 0
    if r is None:
        r = len(A) - 1
    if p < r:
        q = int(math.floor((p+r)/2))
        merge_sort(A, p, q)
        merge_sort(A, q+1, r)
        merge(A, p, q, r)


if __name__ == "__main__":
    import copy
    import random
    print("Generating random sequence of 100 numbers and expected sort..."),
    original = [random.randint(0, 100) for _ in range(100)]
    expected = sorted(original)
    print("Done")

    print("Testing insertion_sort..."),
    sequence = copy.deepcopy(original)
    insertion_sort(sequence)
    assert sequence == expected
    print("Passed")

    print("Testing reverse_insertion_sort..."),
    sequence = copy.deepcopy(original)
    reverse_insertion_sort(sequence)
    assert sequence == sorted(original, reverse=True)
    print("Passed")

    print("Testing selection_sort..."),
    sequence = copy.deepcopy(original)
    selection_sort(sequence)
    assert sequence == expected
    print("Passed")

    print("Testing merge_sort..."),
    sequence = copy.deepcopy(original)
    merge_sort(sequence)
    assert sequence == expected
    print("Passed")
