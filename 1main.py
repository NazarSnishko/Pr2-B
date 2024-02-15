S_Arefmetik = list(map(float, input().split()))
V_count = [num for num in S_Arefmetik if num >= 0]
Result = sum(V_count) / len(V_count) if V_count else "Немає невід'ємних чисел у списку"
print(Result)