#recursively splits array until it is size one then merges the ordered arrays
def merge_sort(arr):
    #base case
    if len(arr) <= 1:
        return arr

    #splits array
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    #recursion
    left = merge_sort(left)
    right = merge_sort(right)
    arr = merge(left, right)

    return arr

#combines two sorted arrays
def merge(left, right):
    combined = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            combined.append(left[i])
            i += 1
        else:
            combined.append(right[j])
            j += 1

    while i < len(left):
        combined.append(left[i])
        i += 1

    while j < len(right):
        combined.append(right[j])
        j += 1
    
    return combined

print(merge_sort([9,12,1,10,3]))
print(merge_sort([3,4,5,2,3,6,1]))
print(merge_sort([8,7,6,5,4,3,2,1]))


    