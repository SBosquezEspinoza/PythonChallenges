def solution(A):
    A.sort()

    # Consider two scenarios:
    # 1. The product of the three largest numbers.
    # 2. The product of the two smallest numbers (potentially negative) and the largest number.
    return max(A[-1] * A[-2] * A[-3], A[0] * A[1] * A[-1])

A = [-3, 1, 2, -2, 5, 6]
print(solution(A))
