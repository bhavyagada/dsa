nums = [3,1,2,5,3]
# 15 - 14 = 1 (m - r)
# 55 - 48 = 7 (m^2 - r^2) = (m + r) * (m - r)

def find_repeating_missing(nums):
    # optimal => TC: O(n), SC: O(1)
    n = len(nums)
    sn = n * (n + 1) // 2
    s2n = n * (n + 1) * (2 * n + 1) // 6

    total, total_sq = 0, 0
    for i in range(n):
        total += nums[i]
        total_sq += (nums[i]**2)
    
    val1 = total - sn # m - r
    val2 = total_sq - s2n # m^2 - r^2

    val2 = val2 // val1 # m + r = (m^2 - r^2) // (m - r)

    x = (val1 + val2) // 2
    y = x - val1

    return [x, y]
print(find_repeating_missing(nums))
