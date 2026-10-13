def quick_sort(arr, left, right):
    if left >= right:
        return arr

    pivot = partition(arr, left, right)
    arr = quick_sort(arr, left, pivot - 1)
    arr = quick_sort(arr, pivot + 1, right)
    return arr


def partition(arr, left, right):
    pivot = right
    right -= 1
    while left <= right:
        if arr[left] <= arr[pivot]:
            left += 1
        elif arr[right] >= arr[pivot]:
            right -= 1
        else:
            #swaps values
            temp = arr[left]
            arr[left] = arr[right]
            arr[right] = temp
            left -= 1
            right -= 1
    temp = arr[left]
    arr[left] = arr[pivot]
    arr[pivot] = temp
    pivot = left
    return pivot

numbers = [4,3,5,6,1]
print(quick_sort(numbers, 0, len(numbers) - 1))