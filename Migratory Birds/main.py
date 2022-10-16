n = int(input())

user_input = input().split()
arr = [int(i) for i in user_input]

def migratoryBirds(arr):
    num = [0, 0, 0, 0, 0]
    for i in arr:
        if i == 1:
            num[0] += 1
        if i == 2:
            num[1] += 1
        if i == 3:
            num[2] += 1
        if i == 4:
            num[3] += 1
        if i == 5:
            num[4] += 1
    
    return num.index(max(num)) + 1

print(migratoryBirds(arr))
    