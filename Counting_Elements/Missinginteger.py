def solution(A):
    min_value = min(A)
    #print(f"Min value: {min_value}")
    max_value = max(A)
    #print(f"Max value: {max_value}")
    sorted_list = sorted(A)
    #print(sorted_list)
    
    for i in range(min_value, max_value + 1):
        if not sorted_list or(min_value < 0 and max_value < 0):
            return 1
        if i in sorted_list:
            if i == max_value:
                return max_value + 1
        elif i not in sorted_list:
            return i
        
    
    

A = [1,3,6,4,1,2]
print(solution(A))
# print(min(A))     1
# print(max(A))     6
# print(list(range(min(A), max(A))))  [1,2,3,4,5]