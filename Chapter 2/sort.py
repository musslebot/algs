
def insertion_sort(sequence):
    """ Return the sequence with elements ascending.

        In-place insertion sort.
    """
    for j in range(1, len(sequence)):
        key = sequence[j]
        i = j - 1
        while i >= 0 and key < sequence[i]:
            sequence[i+1] = sequence[i]
            i -= 1
        sequence[i+1] = key
    return sequence


def reverse_insertion_sort(sequence):
    """ Return the sequence with elements descending.

        In-place reverse insertion sort.
    """
    for j in range(1, len(sequence)):
        key = sequence[j]
        i = j - 1
        while i >= 0 and key > sequence[i]:
            sequence[i+1] = sequence[i]
            i -= 1
        sequence[i+1] = key
    return sequence


def selection_sort(sequence):
    """ Return the sequence with elements ascending.

        In-place selection sort.
    """
    for i in range(0, len(sequence)-1):
        j = i
        for k in range(i+1, len(sequence)):
            if sequence[k] < sequence[j]:
                j = k
        if j != i:
            key = sequence[i]
            sequence[i] = sequence[j]
            sequence[j] = key
    return sequence
