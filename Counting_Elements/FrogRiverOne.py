def solution(X, A):
    position_set = set()

    for time, position in enumerate(A):
        position_set.add(position)
        if len(position_set) == X:
            return time
    return -1

# Example usage:
A = [6, 1, 2, 3, 5, 4]
print(solution(6, A))
