arr = [1,2,3,4,5,6,1]
k = 3

def find_max(arr, k):
    n = len(arr)
    current_sum = sum(arr[:k])
    max_sum = current_sum

    for i in range(k):
        current_sum += arr[n - i - 1] - arr[k - i - 1]
        max_sum = max(max_sum, current_sum)
    return max_sum
print(find_max(arr, k))
