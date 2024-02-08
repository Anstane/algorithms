from typing import List


def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    nums1.extend(nums2) # К одному массиву добавляем второй
    nums1.sort() # Сортируем их
    n = len(nums1) # Берём за основу длину первого массива
    if n % 2 == 1:
        med1 = n // 2
        return nums1[med1] # Если нечётное - просто центральное число
    else:
        med2 = n // 2
        avg = (nums1[med2 - 1] + nums1[med2]) / 2 # Если чётное - сумма двух центральных / 2
        return avg

nums1 = [1,2]
nums2 = [3,4]
print(findMedianSortedArrays(nums1, nums2))
