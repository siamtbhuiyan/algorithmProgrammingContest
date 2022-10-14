user_input = input().split()
arr = [int(i) for i in user_input]

def miniMaxSum(arr):
  sums = []
  temp = 0
  for i in range(len(arr)):
    for j in range(len(arr)):
      if j != i:
        temp += arr[j]
    sums.append(temp)
    temp = 0
  
  temp1 = 0
  temp2 = 5000000000
  for i in range(len(sums)):
    if sums[i] >= temp1:
      temp1 = sums[i]
    if sums[i] <= temp2:
      temp2 = sums[i]

  print(temp2, temp1)
  
miniMaxSum(arr)