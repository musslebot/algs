
import math


def insertion_sort(A):
    """ Return the sequence with elements ascending.

        In-place insertion sort.
    """
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and key < A[i]:
            A[i+1] = A[i]
            i -= 1
        A[i+1] = key
    return A


def reverse_insertion_sort(A):
    """ Return the sequence with elements descending.

        In-place reverse insertion sort.
    """
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and key > A[i]:
            A[i+1] = A[i]
            i -= 1
        A[i+1] = key
    return A


def selection_sort(A):
    """ Return the sequence with elements ascending.

        In-place selection sort.
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
    return A


def merge_sort(A, p=None, r=None):
    """ Return the sequence with elements ascending.

        In-place merge sort.
    """
    def merge(A, p, q, r):
        """ Return merged sequence of two subsequences.

            In-place modification of sequence.
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
        return A
    if p is None:
        p = 0
    if r is None:
        r = len(A) - 1
    if p < r:
        q = int(math.floor((p+r)/2))
        merge_sort(A, p, q)
        merge_sort(A, q+1, r)
        merge(A, p, q, r)
    return A
