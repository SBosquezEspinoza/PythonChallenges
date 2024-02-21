def solution(A):
    sorted_list = sorted(set(A))

    if not sorted_list or sorted_list[0] > 1:
        return 1

    for i in range(1, len(sorted_list)):
        if sorted_list[i] - sorted_list[i - 1] > 1:
            return sorted_list[i - 1] + 1

    return sorted_list[-1] + 1
