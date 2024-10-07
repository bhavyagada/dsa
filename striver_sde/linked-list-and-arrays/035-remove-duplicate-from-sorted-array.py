def remove_duplicates(nums):
    n = len(nums)
    k = 0
    for i in range(1, n):
        if nums[i] != nums[k]:
            k += 1
            nums[k] = nums[i]
    return k+1

nums = [0,0,1,1,1,2,2,3,3,4]
k = remove_duplicates(nums)
print(nums[:k])
assert nums[:k] == [0,1,2,3,4]