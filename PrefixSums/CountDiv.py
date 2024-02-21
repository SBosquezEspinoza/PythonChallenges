def solution(A, B, K):
    count = 0
    if A != B:
        for i in range(A, B+1):
            if i % K == 0:
                count += 1
        return count
    else:
        if A % K == 0:
            return 1


A = 6 
B = 11
K = 2
print(solution(A, B, K))

