arr = [1,2,3,4,5,0]
# arr = [1,2,-3,0,-4,-5]

def max_product_subarray(arr):
    # optimal => TC: O(n), SC: O(1)
    n = len(arr)
    max_prod = float('-inf')
    pre, suff = 1, 1
    for i in range(n):
        if pre == 0: pre = 1
        if suff == 0: suff = 1
        pre *= arr[i]
        suff *= arr[n-i-1]
        max_prod = max(max_prod, max(pre, suff))
    return max_prod
print(max_product_subarray(arr))
