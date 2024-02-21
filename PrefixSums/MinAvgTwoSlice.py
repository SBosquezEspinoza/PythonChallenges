def solution(A):
    N = len(A)
    min_avg = float('inf')
    min_index = 0

    for i in range(N-1):
        avg = (A[i] + A [i + 1]) / 2
        if avg < min_avg:
            min_avg = avg
            min_index = i
        
        if i < N-2:
            avg3 = (A[i] + A[i+1] + A[i+2])/3
            if avg3 < min_avg:
                min_avg = avg3
                min_index = i
    return min_index


A = [4,2,2,5,1,5,8]
print(solution(A))
