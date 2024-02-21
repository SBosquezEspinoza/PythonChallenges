def solution(A):
    sorted_list = sorted(A)
    print(sorted_list)
    if len(sorted_list) == 1:
        return 1
    else:
        for index, element in enumerate(sorted_list[:-1]):
            next_element = sorted_list[index + 1]
            if next_element != element + 1:
                return 0
        return 1
        




A = [4,5,6]
print(solution(A))