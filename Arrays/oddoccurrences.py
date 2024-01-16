def solution(A):
    seen_elements = set() ## could be done using a list but only a output retrieve the unique element
    for element in A:
        if element in seen_elements:
            seen_elements.remove(element)
        else:
            seen_elements.add(element)
    return seen_elements.pop()

A = [9,3,9,3,9,7,9]

print(solution(A))
print('1,2,3,4'.split(','))