def binary_search(lst, item, first, last):
    if item not in lst:
        return -1
    else:
        mid = (first + last) // 2
        if lst[mid] == item:
            print(mid)
            return mid
        elif lst[mid] > item:
            return binary_search(lst, item, first, mid)
        elif lst[mid] < item:
            return binary_search(lst, item, mid, last)
num_lst = [int(x) for x in input("Enter any number list").split()]
itemToBeSearched = int(input("Enter the number to search "))
index = binary_search(sorted(num_lst), itemToBeSearched, 0, (len(num_lst)-1))
if index == -1:
    print("Number is NOT IN THE LIST")
else:
    print(f'After sorting, the number is in index {index}')