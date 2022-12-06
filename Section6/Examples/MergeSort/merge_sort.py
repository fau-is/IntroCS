from cs50 import get_int
def main():
    to_sort = []
    for i in range(10):
        n = get_int("Number: ")
        to_sort.append(n)

    print(mergeSort(to_sort))

    print(sorted(to_sort))


def mergeSort(arr):
    # Base Case
    if len(arr) <= 1:
        return arr

    # Middle Index
    middle = len(arr) // 2

    # Sort from start to middle
    l = mergeSort(arr[:middle])

    # Sort from middle to end
    r = mergeSort(arr[middle:])


    # merge the two sorted lists and return
    return merge(l,r)

def merge(l, r):
    arr_sort = []

    # Iterate as long as both lists still have numbers
    while len(l) > 0 and len(r) > 0:

        # If left less than right
        if l[0] < r[0]:
             # Append first element from left to sorted array
            arr_sort.append(l[0])
            # Remove the copied element from original l
            l.pop(0)

        # If r less than or equal to left
        else:
            # Append first element from right arr to sorted array
            arr_sort.append(r[0])
            # Remove copied element from original r
            r.pop(0)
    # Add remainiung lists to the sorted list and return
    return arr_sort + l + r

if __name__ == '__main__':
    main()
