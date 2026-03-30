n,k = map(int,input().split())
array = list(map(int,input().split()))
array = sorted(array)
# debt keeps the total that was substracted
debt = 0
index = 0
for i in range(k):

    
    while  index < len(array) and array[index]-debt == 0 :
      index += 1
      continue 
    if index == len(array):
      print(0)
      continue
    # should be the min
    
    print(array[index]-debt) 
    debt = array[index]
    # print(f'debt after iteration {i} is {debt}, index is at {index}')
    

