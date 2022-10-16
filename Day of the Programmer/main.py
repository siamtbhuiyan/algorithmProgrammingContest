y = int(input())

def dayOfProgrammer(y):
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = 0
    month = 0
    
    if y <= 1917:
        if y % 4 == 0:
            months[1] = 29
        else:
            months[1] = 28
    elif y >= 1919:
        if (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0):
            months[1] = 29
        else:
            months[1] = 28
    else:
        months[1] = 15

    sum = 0
    for index, i in enumerate(months):
        if sum > 256:
            sum = sum - months[index - 1]
            day = 256 - sum
            month = index
            break
        sum = sum + i
        
    if month < 10:
        print(f"{day}.0{month}.{y}")
    else:
        print(f"{day}.{month}.{y}")

dayOfProgrammer(y)