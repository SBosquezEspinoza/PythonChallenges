def solution(X, Y, D):
    nr_jumps = 0
    while X < Y:
        
        X += D
        nr_jumps += 1
    return nr_jumps

print(solution(10,85,30))
        