# Pure Function

# def multiply_by2(li):
#     new_list = []
#     for item in li:
#         new_list.append(item * 2)
#     return new_list


# map, filter, zip, and reduce
# lambda expressions
from functools import reduce

my_list = [1, 2, 3]


# your_list = [10, 20, 30]


# def multiply_by2(item):
#     return item * 2


def only_odd(item):
    return item % 2 != 0


def accumulator(acc, item):
    print(acc, item)
    return acc + item


# print(list(map(multiply_by2, my_list)))
# print(list(filter(only_odd, my_list)))
# print(list(zip(my_list, your_list)))
# print(reduce(accumulator, my_list, 0))
print(list(map(lambda item: item * 2, my_list)))
print(my_list)

# lambda param: action(param)
