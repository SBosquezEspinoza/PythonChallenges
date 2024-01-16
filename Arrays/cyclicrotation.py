def solution(A,K):
    N = len(A)
    K = K % N 
    rotated_array = A[-K:] + A[:-K]
    return rotated_array
