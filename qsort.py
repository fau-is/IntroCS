import sys

def pretty_printer(arr):
    print("Prettily printed result:")
    print("[ ", end="")
    for i in range(len(arr)-1):
        print("%c" % arr[i], end=", ")
    print("%c" % arr[len(arr)-1], end=" ]")


def partition(arr, lower, upper):
    idx = (lower - 1)
    pivot = arr[upper]

    for j in range(lower, upper):

        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:
            # increment index of smaller element
            idx = idx + 1
            arr[idx], arr[j] = arr[j], arr[idx]

    idx = idx + 1
    arr[idx], arr[upper] = arr[upper], arr[idx]
    return idx


# arr -> list t.b. sorted
# lower  -> starting index,
# upper  -> ending index
# sorts in in-situ!
def quickSort(arr, lower, upper):
    if lower < upper:
        pivot = partition(arr, lower, upper)

        # sort recursively
        quickSort(arr, lower, pivot - 1)
        quickSort(arr, pivot + 1, upper)
    return arr


if __name__ == '__main__':

    INPUT = list(sys.argv[1])

    pretty_printer(quickSort(INPUT, 0, len(INPUT) - 1))
