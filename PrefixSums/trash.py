def solution(A):
    minimo = float('inf')
    position = None

    for index,element in enumerate(A[:-2]):

        min_avg_two = (element + A[index + 1])/2
        
        if min_avg_two < minimo:
            minimo = min_avg_two
            position = index
        
        min_avg_three = (element + A[index + 1] + A[index + 2])/3

        if min_avg_three < minimo:
            minimo = min_avg_three
            position = index

    return position 

A = [4,2,2,5,1,5,8]
print(solution(A))