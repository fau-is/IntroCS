import argv

def main():
    if len(argv) <= 2:
        print("Usage: python merge_sort.py INT1 INT2 [...]")
    to_sort = [int(x) for x in argv[1:]]
    mergeSort(to_sort)

def mergeSort(arr):
    

