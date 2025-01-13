from collections import defaultdict

arr = [3,1,2,4]
k = 6

def count_subarrays(arr, k):
    # optimal => TC: O(n), SC: O(n)
    cnt = 0
    summ = 0
    hashmap = defaultdict(int)
    hashmap[0] = 1
    for i in range(len(arr)):
        summ += arr[i]
        rem = summ - k
        cnt += hashmap[rem]
        hashmap[summ] += 1
    return cnt
print(count_subarrays(arr, k))
