nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]

def merge_sorted_arrays(nums1, nums2):
    # optimal => TC: O(n+m), SC: O(1)
    n, m = len(nums1) - len(nums2), len(nums2)
    i, j = n - 1, m - 1
    k = n + m - 1

    while j >= 0:
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1

merge_sorted_arrays(nums1, nums2)
print(nums1)
