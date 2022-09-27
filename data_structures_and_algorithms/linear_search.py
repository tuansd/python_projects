# def linear_search(the_list, target):
#     for x in range(len(the_list)):
#         if the_list[x] == target:
#             print("Found at index", x)
#             return x
#     print("Target is not in the list")
#     return -1


# my_list = [6, 3, 4, 2, 5, 7]
# print("Yes" if 10 in my_list else "No")
# A linear search sequentially checks each element of the list until it finds an element that matches the target value. If the algorithm reaches the end of the list, the search terminates unsuccessfully.

# Hash table search: is a list with value store in it not in order, it depend of the function keys. So when search for value in the hash table, it is using the same key function so it is fast like O(1),

# linear_search(my_list, 5)
# linear_search(my_list, 3)
print(linear_search(my_list, 5))
