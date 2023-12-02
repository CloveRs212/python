# list, set, dictionary
# List
my_list = [char for char in 'hello']
my_list2 = [num for num in range(0, 100)]
my_list3 = [num**2 for num in range(0,100)]
my_list4 = [num**2 for num in range(0,100) if num % 2 ==0]

# for char in 'hello':
#     my_list.append(char)
# is the same as the above code snipit for my_list

# print(my_list4)

# sets is the same as a list, you are just using {} instead of []. Sets only give unique numbers

# Dictionary
simple_dict = {
    'a': 1,
    'b': 2
}
my_dict = {k:v**2 for k,v in simple_dict.items()}

my_dict2 = {num:num*2 for num in [1,2,3]}

print(my_dict2)
