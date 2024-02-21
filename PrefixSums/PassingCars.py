def solution(A):
    east_cars = 0  # Count of cars traveling east
    passing_cars = 0  # Count of passing cars

    for car in A:
        if car == 0:
            east_cars += 1
        else:
            passing_cars += east_cars

            if passing_cars > 1000000000:
                return -1  # Check for the limit

    return passing_cars

# Test case
A = [0, 1, 0, 1, 1,1,1,1,1]
print(solution(A))
#####
def solution(A):
    counter = 0
    for i, car in enumerate(A):
        if car == 0:
            for index,value in enumerate(A):
                if value == 1 and index > i:
                    counter += 1
        if counter > 1000000000:
            return -1
    return counter

A =[0,1,0,1,1]
print(solution(A))