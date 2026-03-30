tests = int(input())
for _ in range(tests):
    n = int(input())
    students = list(map(int,input().split()))
    result = []
    possible = True
    i = 0
    while i < n:
        j=i
        sub_list = []
        while i+1 < n and students[i+1] == students[i]:
            sub_list.append(i+1)
            i += 1
            # print(sub_list)
        sub_list.append(i+1)
        i+=1
        if len(sub_list) == 1: 
            possible = False
            break
        sub_list = [sub_list[-1]]+sub_list[:-1]
        result.extend(sub_list)
    if possible:
        print(*result)
    else:
        print(-1)