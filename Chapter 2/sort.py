
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
