user_input = input().split()
s, t = [int(i) for i in user_input]

user_input = input().split()
a, b = [int(i) for i in user_input]

user_input = input().split()
m, n = [int(i) for i in user_input]

user_input = input().split()
apples = [int(i) for i in user_input]

user_input = input().split()
oranges = [int(i) for i in user_input]


def countApplesAndOranges(s, t, a, b, apples, oranges):
  applesInHouse = 0
  orangesInHouse = 0
  for apple in apples:
    if apple + a >= s and apple + a <= t:
      applesInHouse += 1

  for orange in oranges:
    if orange + b >= s and orange + b <= t:
      orangesInHouse += 1

  return [applesInHouse, orangesInHouse]


ans = countApplesAndOranges(s, t, a, b, apples, oranges)

for i in ans:
  print(i)