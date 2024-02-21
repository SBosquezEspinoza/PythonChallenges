def solution(A, B):
    counter = []
    bigger = 0

    
    for index,(a,b) in enumerate(zip(A[:-1],B[:-1])):
        if b == 0 and index == 0:
            counter.append(a)

        elif b != B[index + 1]:
            bigger = max(a, A[index + 1])

    if B[-1] == 0:
        counter.append(A[-1])
    return len(counter)

A = [4,3,2,1,5]

B = [0,1,0,0,0]

print(solution(A,B))
############


def solution(A, B):
    downstream_fish = []  # Stack to keep track of downstream fish

    alive_fish = 0  # Count of fish that will stay alive

    for i in range(len(A)):
        size = A[i]
        direction = B[i]

        if direction == 0:  # Upstream fish
            while downstream_fish:
                downstream_size = downstream_fish.pop()

                if downstream_size > size:
                    # Upstream fish is eaten by downstream fish
                    downstream_fish.append(downstream_size)
                    break
            else:
                # No downstream fish to eat the upstream fish
                alive_fish += 1
        else:
            # Downstream fish, push it onto the stack
            downstream_fish.append(size)

    # The remaining downstream fish are guaranteed to stay alive
    alive_fish += len(downstream_fish)

    return alive_fish

# Example usage:
A = [4, 3, 2, 1, 5]
B = [0, 1, 0, 0, 0]
result = solution(A, B)
print(result)  # Output: 2
