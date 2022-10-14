n = int(input())

arr = []

for i in range(n):
  user_input = int(input())
  arr.append(user_input)


def gradingStudents(arr):
  new_arr = []
  for i in arr:
    if i < 38:
      new_arr.append(i)
    else:
      if (i + 1) % 5 == 0:
        new_arr.append(i + 1)
      elif (i + 2) % 5 == 0:
        new_arr.append(i + 2)
      else:
        new_arr.append(i)

  return new_arr


new_arr = gradingStudents(arr)

for i in new_arr:
  print(i)