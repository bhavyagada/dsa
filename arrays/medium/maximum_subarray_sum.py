nums = [-2,1,-3,4,-1,2,1,-5,4]

def max_subarray_sum(nums):
    # optimal => TC: O(n), SC: O(1)
    summ, max_sum = 0, float('-inf')
    start, arr_s, arr_e = 0, -1, -1
    for i in range(len(nums)):
        if summ == 0:
            start = i

        summ += nums[i]

        if summ > max_sum:
            max_sum = summ
            arr_s = start
            arr_e = i

        if summ < 0:
            summ = 0

    return max_sum, nums[arr_s:arr_e+1]
print(max_subarray_sum(nums))
