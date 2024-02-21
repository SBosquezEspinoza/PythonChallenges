def solution(S, P, Q):
    dict = {'A' : 1,'C' : 2,'G' : 3,'T': 4}
    S = [dict[element] for element in S]
    valores = []
    for p,q in zip(P,Q):
        minimo = min(S[p:q+1])
        valores.append(minimo)
    return valores

S ='CAGCCTA'
P = [2, 5, 0]
Q = [4, 5, 6]
print(solution(S, P, Q))
###########
#pref sum
def solution(S, P, Q):
    dict = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
    
    # Convierte la cadena S a una lista de impact factors
    S = [dict[element] for element in S]
    
    # Calcula la suma de prefijos
    prefix_sum = [0] + S[:]
    for i in range(1, len(prefix_sum)):
        prefix_sum[i] += prefix_sum[i - 1]
    
    # Procesa las queries
    valores = []
    for p, q in zip(P, Q):
        if p == 0:
            valores.append(prefix_sum[q])
        else:
            valores.append(prefix_sum[q] - prefix_sum[p - 1])
    
    return valores

S = 'CAGCCTA'
P = [2, 5, 0]
Q = [4, 5, 6]
print(solution(S, P, Q))
