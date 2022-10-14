n = int(input())
user_input = input().split()

ar = [int(i) for i in user_input]


def aVeryBigSum(ar):
  sum = 0
  for x in ar:
    sum += x
  return sum

print(aVeryBigSum(ar))