N = int(input())
choice = 0

for k in range(2, N + 1):
    temp = N 
    while temp >= k:
        if temp % k == 0:
            temp = temp // k
        else:
            temp = temp % k  
            
    if temp == 1:
        choice = choice + 1

print(choice)
