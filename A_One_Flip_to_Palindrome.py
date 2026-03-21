tests = int(input())

for _ in range(tests):
    n = int(input())
    nums = list(input())
    half = n // 2 
    differences = []
    for i in range(half):
        if nums[i] != nums[n-i-1]:
            differences.append( 1)
        else:
            differences.append(0)

    blocks = 0
    in_block = False 
    for d in differences:
        if d == 1 and not in_block:
            blocks += 1 
            in_block = True
        if d == 0:
            in_block = False
    if blocks > 1:
        print('No')
    else:
        print('Yes')
    
