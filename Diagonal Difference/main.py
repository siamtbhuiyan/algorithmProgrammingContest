n = int(input())

matrix = []

for i in range(n):
  user_input = input().split()
  arr = [int(i) for i in user_input]
  matrix.append(arr)


def diagonalDifference(matrix):
  sum1 = 0
  sum2 = 0
  for x in range(len(matrix)):
    sum1 += matrix[x][x]
    sum2 += matrix[x][len(matrix) - 1 - x]

  diff = abs(sum1 - sum2)
  print(diff)


diagonalDifference(matrix)