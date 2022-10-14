user_input = input().split()
n, m = [int(i) for i in user_input]

user_input = input().split()
arr1 = [int(i) for i in user_input]

user_input = input().split()
arr2 = [int(i) for i in user_input]

def getTotalX(arr1, arr2):
    num = 0

    for i in range(1, 101):
        count = 0
        for j in arr1:
            if i%j == 0:
                count += 1
        
        if count == len(arr1):
            count = 0
            for j in arr2:
                if j%i == 0:
                    count += 1
            
            if count == len(arr2):
                num += 1

    return num

print(getTotalX(arr1, arr2))