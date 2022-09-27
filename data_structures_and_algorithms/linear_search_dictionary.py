from re import X


def linear_search_dictionary(the_dictionary, the_value):

    # the_list = list(the_dictionary)
    for key, value in the_dictionary.items():
        if value == the_value:
            print("Found at key ", key)
            return key

    print("Target is not in the dictionary")
    return None


my_dictionary = {"red": 5, "blue": 3, "yellow": 12, "green": 7}

# linear_search_dictionary(my_dictionary, 5)
# linear_search_dictionary(my_dictionary, 3)
# linear_search_dictionary(my_dictionary, 8)


my_set = set()  # Create an empty Set
my_set = {(1, 2), (3, 4), (4, 5)}  # literal Set

my_set.add(tuple([6, 9]))  # Add new tuple to Set, must be in list

# print(my_set)  # {(4, 5), (1, 2), (6, 9), (3, 4)}
# for n in my_set:         # print or get item in Set
#     print(n[0], n[1])

my_tuple = my_set.pop()
print(my_tuple[0], my_tuple[1])
my_tuple = my_set.pop()
print(my_tuple[0], my_tuple[1])
# print(my_set.pop())
