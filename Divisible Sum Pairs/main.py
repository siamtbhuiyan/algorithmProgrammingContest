user_input = input().split()
n, k = [int(i) for i in user_input]

user_input = input().split()
arr = [int(i) for i in user_input]

def divisibleSumPairs(n, arr, k):
    pairs = 0
    for index, i in enumerate(arr):
        for j in range(index + 1, n):
            if (i + arr[j]) % k == 0:
                pairs += 1

    return pairs

print(divisibleSumPairs(n, arr, k))