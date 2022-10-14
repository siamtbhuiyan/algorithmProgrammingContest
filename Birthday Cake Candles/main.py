n = int(input())
user_input = input().split()
arr = [int(i) for i in user_input]


def birthdayCakeCandles(arr):
  max = 0
  count = 0
  for i in arr:
    if i >= max:
      max = i

  for i in arr:
    if i == max:
      count += 1

  return count


print(birthdayCakeCandles(arr))