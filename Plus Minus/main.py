n = int(input())

user_input = input().split()
arr = [int(i) for i in user_input]

def plusMinus(arr):
  positive = 0
  negative = 0
  zero = 0
  for i in arr:
    if i < 0:
      negative += 1
    elif i > 0:
      positive += 1
    else:
      zero += 1

  print("{:6f}".format(positive/n))
  print("{:6f}".format(negative/n))
  print("{:6f}".format(zero/n))

plusMinus(arr)