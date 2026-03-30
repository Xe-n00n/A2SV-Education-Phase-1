tests= int(input())
for _ in range(tests):
    n = int(input())
    before = list(map(int,input().split()))
    after = list(map(int,input().split()))
    i = 0
    j = 0
    online_count = 0
    while i< n and j <n:
        if before[i]!=after[j]:
            online_count +=1
            i+=1
            j+=1
        
    print(str(online_count))