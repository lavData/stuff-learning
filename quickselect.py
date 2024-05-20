def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def kthSmallest(arr, low, high, k):
    if k > 0 and k <= high - low + 1:
        index = partition(arr, low, high)

        if index - low == k - 1:
            return arr[index]

        if index - low > k - 1:
            return kthSmallest(arr, low, index - 1, k)

        return kthSmallest(arr, index + 1, high, k - (index - low + 1))


arr = [12, 3, 5, 7, 4, 19, 26]
n = len(arr)
k = 3
print("K'th smallest element is", kthSmallest(arr, 0, n - 1, k))
