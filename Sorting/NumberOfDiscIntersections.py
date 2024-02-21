def solution(A):
    N = len(A)
    if N < 2:
        return 0

    # Create an array to store the left and right boundaries of the discs
    left_boundary = [0] * N
    right_boundary = [0] * N

    for i in range(N):
        left_boundary[i] = i - A[i]
        right_boundary[i] = i + A[i]

    left_boundary.sort()
    right_boundary.sort()

    intersections = 0
    active_circles = 0
    right_index = 0

    for left_index in range(N):
        # Count the active circles that have left boundary less than or equal to the current right boundary
        while right_index < N and right_boundary[right_index] < left_boundary[left_index]:
            active_circles -= 1
            right_index += 1

        # Count the number of intersections
        intersections += active_circles
        if intersections > 10000000:
            return -1

        active_circles += 1

    return intersections

# Example usage
A = [1, 5, 2, 1, 4, 0]
print(solution(A))  # Output should be 11
