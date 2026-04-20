def union(arr1, arr2):
    full_arr = arr1 + arr2

    final_arr = merge_sort(full_arr)
    while no_duplicates(final_arr) == True:
        for i in range(len(final_arr)):
            if final_arr[i] == final_arr[i+1]:
                final_arr.pop(i)
            break
    return final_arr
def no_duplicates(arr):
    for i in range(len(arr)):
        if arr[i] == arr[i+1]:
            return False
        else:
            return True
def merge_sort(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)
def merge(left, right):
    results = []
    i=j=0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            results.append(left[i])
            i+=1
        else:
            results.append(right[j])
            j+=1

    results.extend(left[i:])
    results.extend(right[j:])

    return results
arr1 = [1,2,2,3,5]
arr2 = [2,3,3,4,6]

print(union(arr1, arr2))
