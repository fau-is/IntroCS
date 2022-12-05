from cs50 import get_int

def main():
    to_sort = []
    for i in range(10):
        n = get_int("Number: ")
        to_sort.append(n)
    arr = list(to_sort)
    print(heapSort(arr))

    print(sorted(to_sort))

def heapSort(arr):
    sort_arr = []
    arr_len = len(arr)
    for i in range(arr_len):
        arr = reheap(arr)
        sort_arr.append(arr.pop(0))
    return sort_arr


def reheap(arr):
    swap = True

    while swap:
        swap = False
        for i in range(len(arr) // 2):
            left = i * 2 + 1
            right = i * 2 + 2

            if left < len(arr) and arr[i] > arr[left]:
                arr[i], arr[left] = arr[left], arr[i]
                swap = True
            if right < len(arr) and arr[i] > arr[right]:
                arr[i], arr[right] = arr[right], arr[i]
                swap =  True
    return arr

if __name__ == '__main__':
    main()
