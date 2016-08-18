import math


def find_maximum_subarray_brute(A, low, high):
    """ Brute-force algorithm to finx the maximum sum subarray in A.
    """
    max_low = 0
    max_high = 0
    max_sum = float("-inf")
    for i in range(low, high):
        current_sum = A[i]
        for j in range(i+1, high):
            current_sum += A[j]
            if current_sum > max_sum:
                max_sum = current_sum
                max_low, max_high = i, j
    return max_low, max_high, max_sum


def find_maximum_crossing_subarray(A, low, mid, high):
    """ Return maximum subarray that crosses the mid point of A.
    """
    # mid-left
    left_sum = float("-inf")
    max_left = 0
    sum_ = 0
    for i in range(mid, low-1, -1):
        sum_ += A[i]
        if sum_ > left_sum:
            left_sum = sum_
            max_left = i
    # mid-right
    right_sum = float("-inf")
    max_right = 0
    sum_ = 0
    for j in range(mid+1, high+1):
        sum_ += A[j]
        if sum_ > right_sum:
            right_sum = sum_
            max_right = j
    return max_left, max_right, left_sum + right_sum


def find_maximum_subarray_divide_and_conquer(A, low, high):
    """ Return maximum subarray using a recursive, d&c algorithm.
    """
    if high-1 == low:
        return (low, high, A[low])
    else:
        mid = int(math.floor((low+high)/2))
        left_low, left_high, left_sum = find_maximum_subarray_divide_and_conquer(A, low, mid)
        right_low, right_high, right_sum = find_maximum_subarray_divide_and_conquer(A, mid+1, high)
        cross_low, cross_high, cross_sum = find_maximum_crossing_subarray(A, low, mid, high)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_low, left_high, left_sum
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum


if __name__ == "__main__":
    original = [
        13, -3, -25, 20,
        -3, -16, -23, 18,
        20, -7, 12, -5,
        -22, 15, -4, 7
    ]
    expected = (7, 10, 43)  # 0-indexing

    print("Testing find_maximum_subarray_brute..."),
    assert find_maximum_subarray_brute(original, 0, len(original)) == expected
    print("Passed")

    print("Testing find_maximum_subarray_divide_and_conquer..."),
    assert find_maximum_subarray_divide_and_conquer(original, 0, len(original)-1) == expected
    print("Passed")
