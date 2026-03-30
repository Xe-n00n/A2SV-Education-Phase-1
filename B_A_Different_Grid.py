tests = int(input())
for _ in range(tests):
    n,m = map(int,input().split())

    elements = []
    for i in range(n):
        el = list(map(int,input().split()))
        elements.extend(el)
    # print(elements)
    if n == m and n == 1:
        print(-1)
        continue
    elements = [elements[-1]]+elements[:-1]
    # print(elements)
    for i in range(n):
       line = elements[i*m:(i+1)*m]
       print(*line)