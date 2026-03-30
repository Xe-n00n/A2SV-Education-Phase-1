


tests= int(input())
for _ in range(tests):
    n, c = map(int,input().split())
    items = sorted(map(int,input().split()),reverse= True)
    
    coupons = sorted(map(int,input().split()))
    total_price = sum(items)
    # index on the items
    idx = 0 
    for coupon in coupons:
        idx += coupon
        if idx <= n:
            total_price -= items[idx-1]
    print(total_price)