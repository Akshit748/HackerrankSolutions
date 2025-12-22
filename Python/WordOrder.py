# Enter your code here. Read input from STDIN. Print output to STDOUT

N = int(input())
dicts = {}
orders = []

for _ in range(N):
    orders.append(str(input()))
    
    if orders[_] not in dicts:
        dicts[orders[_]] = 1
    else:
        dicts[orders[_]] += 1
        
print(len(set(orders)))

print(" ".join(map(str, dicts.values())))
