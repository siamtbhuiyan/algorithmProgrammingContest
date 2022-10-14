s = input()

def timeConversion(s):
  output = ""
  size = len(s)
  if s[-2] == "A":
    s = s[:size - 2]
    if s[0] == "1" and s[1] == "2":
      output = "00" + s[2:]
      return output
    else:
      return s
  elif s[-2] == "P":
    s = s[:size - 2]
    if s[0] == "1" and s[1] == "2":
      return s
    else:
      hour = str(int(s[:2]) + 12)
      output = hour + s[2:]
      return output

print(timeConversion(s))