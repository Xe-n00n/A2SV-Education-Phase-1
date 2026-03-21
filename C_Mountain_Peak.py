tests = int(input())
for _ in range(tests):
    n = int(input())
    nums = list(map(int,input().split()))
    exists = False
    for i in range(1,len(nums)-1):
        if nums[i-1] < nums[i] and nums[i]> nums[i+1]:
            print('Yes')
            print(f'{i} {i+1} {i+2}')
            exists = True
            break
    if not exists:
        print('No')