a1, a2, a3 = input().split()
b1, b2, b3 = input().split()

a = [int(a1), int(a2), int(a3)]
b = [int(b1), int(b2), int(b3)]


def compareTriplets(a, b):
  alice = 0
  bob = 0
  for i, x in enumerate(a):
    if a[i] > b[i]:
      alice += 1
    elif a[i] < b[i]:
      bob += 1

  print(alice, bob)


compareTriplets(a, b)