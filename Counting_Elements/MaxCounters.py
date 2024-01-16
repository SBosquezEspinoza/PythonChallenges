def solution(N, A):
    counters = [0] * N
    # counters = [0 for i in range(0,N)]
    max_value = 0

    for value in A:
        
        #if value <= N and index <= N:         
        if 1 <= value <= N: 
            counters[value-1] += 1
            max_value = counters[value-1]
            #print(counters)

        elif value == N+1:
            counters = [ 1*max_value for i in range(0,N)]

    return tuple(counters)


A = [3,4,4,6,1,4,4]
print(solution(5,A))
