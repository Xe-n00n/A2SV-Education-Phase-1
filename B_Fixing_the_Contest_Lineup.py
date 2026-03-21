tests = int(input())
for _ in range(tests):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    i = 0 
    j = 0 
    count = 0
    while i < len(a) and j<len(b):
        if a[i] > b[j]:
            count += 1
            j += 1
        else:
            i+=1
            j+=1 
    print(count)
# 4 5 6 7 8 9
# 1 2 3 4 5 6