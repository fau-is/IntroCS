

def binary_search(arr, left, right, value):
    if right >= left:

        mid = left + (right - left) / 2

        if arr[mid] == value:
            return mid
        elif arr[mid] > value:
            return binary_search(arr, left, mid - 1, value)
        else:
            return binary_search(arr, mid + 1, right, value)

    else:
        return None
