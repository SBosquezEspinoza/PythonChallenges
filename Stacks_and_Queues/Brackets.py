def solution(S):
    stack = []
    # Dictionary to check matching parentheses
    pairs = {')': '(', '}': '{', ']': '['}

    for char in S:
        if char in {'(', '{', '['}:
            # If it's an opening parenthesis, push onto the stack
            stack.append(char)
        elif char in {')', '}', ']'}:
            # print(char)
            # print(pairs[char])
            # If it's a closing parenthesis, check if it matches the top of the stack
            print(stack)
            if not stack or stack.pop() != pairs[char]:
                return 0  # Mismatched parenthesis
        else:
            pass
            # Ignore other characters in the string

    # The stack should be empty if the string is properly nested
    return int(not stack)

# Example usage:
S1 = "{[()()]}"
print(solution(S1))  # Output: 1

S2 = "([)()]"
#print(solution(S2))  # Output: 0
