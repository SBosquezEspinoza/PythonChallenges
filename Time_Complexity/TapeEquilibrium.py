def solution(A):
    min_diff = 10000
    sum_left = 0
    total_sum = sum(A)
    for element in A[:-1]:
        sum_left += element
        sum_right = total_sum - sum_left
        diff = abs(sum_left-sum_right)
        if diff < min_diff:
            min_diff = diff
    return min_diff


A = [3,1,2,4,3]
print(solution(A))
