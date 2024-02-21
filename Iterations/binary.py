### BINARY GAP
import sys
import os

def solution(N):
    binary_list = []
    while N > 0:
        binary_number = N % 2
        binary_list.append(binary_number)
        N = N // 2

    print(f"Number in binary form: {binary_list}")
    current_gap = 0
    max_gap = 0
    in_gap = False
    for element in binary_list:
        if element == 1:
            if in_gap:
                
                max_gap = max(max_gap,current_gap)
                current_gap = 0
            else:
                in_gap=True
        elif in_gap:
            current_gap +=1
    return max_gap


user_input = int(input("Type the number you want to know the bigger binary gap:"))


print(f"The bigger 0 gap is: {solution(user_input)}")



####second way

def solution(A):
    ## changing number to binary form 

    binary_number = [] 
    while A > 0:
        rest = A % 2
        A = A // 2
        binary_number.append(rest)
    
    binary_number = binary_number[::-1]

    ## biggest gap?
    in_gap = False
    max_gap = 0
    current_gap = 0

    for i in binary_number:
        if i == 1:
            if in_gap:
                max_gap = max(max_gap, current_gap)
                current_gap = 0

        elif i == 0:
            in_gap = True
            current_gap += 1

   
    return max_gap


A = 32
print(solution(A))