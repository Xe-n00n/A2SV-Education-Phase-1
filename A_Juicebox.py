tests = int(input())

for _ in range(tests):
    n,k = map(int, input().split())
    costs = [0]*(k+1)
    for _ in range(k):
        b,c =  map(int, input().split())
        costs[b] += c

    sorted_costs = sorted(costs,reverse=True)
    max_cost = sum(sorted_costs[:n])    
    print(max_cost)