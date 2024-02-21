def solution(S):
    stack = []
    characters = {')':'(', '(': ')'}

    for char in S:
        if char == '(':
            stack.append(char)
            
        else:
            if not stack or stack.pop() != characters[char]:
                return 0
    return 1

S = "(()(())())"

print(solution(S))