def solution(A):
   expected_sum = (len(A)+1)*(len(A)+2)//2
   actual_sum =sum(A)
   not_found = expected_sum - actual_sum
   return int(not_found)



A = [2,3,1,5]

print(solution(A))

