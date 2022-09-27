def binary_search(the_list, target):
    lower_bound = 0
    upper_bound = len(the_list) - 1

    while lower_bound <= upper_bound:
        pivot = (lower_bound + upper_bound) // 2
        print(pivot)
        pivot_value = the_list[pivot]

        if pivot_value == target:
            return pivot
        if pivot_value > target:
            upper_bound = pivot - 1
        else:
            lower_bound = pivot + 1

    return -1


test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# test_list = [18, 21, 27, 47, 52, 76, 82]
print(binary_search(test_list, 10))
print(binary_search(test_list, 76))
