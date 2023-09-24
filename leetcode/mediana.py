def findMedianSortedArrays(nums1, nums2):
    nums1.extend(nums2)
    nums1.sort()
    n = len(nums1)
    if n % 2 == 1:
        med1 = n // 2
        return nums1[med1]
    else:
        med2 = n // 2
        avg = (nums1[med2 - 1] + nums1[med2]) / 2
        return avg

nums1 = [1,2]
nums2 = [3,4]
print(findMedianSortedArrays(nums1, nums2))
