arr = [1,2,3,1,1,1,1,3,3]
k = 6

# (positives, zeroes AND negatives)
def longest_subarray(arr, k):
    # optimal => TC: O(n) / O(nlogn), SC: O(n)
    n = len(arr)
    summ, max_length = 0, 0
    prefix_sum = {}
    for i in range(n):
        summ += arr[i]
        if summ == k:
            max_length = max(max_length, i + 1)
        
        rem = summ - k
        if rem in prefix_sum:
            max_length = max(max_length, i - prefix_sum[rem])
        
        if summ not in prefix_sum:
            prefix_sum[summ] = i
    return max_length
print("positives, zeroes AND negatives:", longest_subarray(arr, k))

# (only positives and zeroes)
def longest_subarray(arr, k):
    # optimal => TC: O(2n), SC: O(1)
    n = len(arr)
    summ, max_length = 0, 0
    l, r = 0, 0
    while r < n:
        summ += arr[r]

        while summ > k and l <= r:
            summ -= arr[l]
            l += 1

        if summ == k:
            max_length = max(max_length, r - l + 1)

        r += 1
    return max_length
print("only positives and zeroes:", longest_subarray(arr, k))
