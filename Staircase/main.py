n = int(input())


def staircase(n):
  for i in range(n, 0, -1):
    for j in range(n + 1):
      if j + 1 < i:
        print(" ", end="")
      elif j > i:
        print("#", end="")
    print("#")

staircase(n)