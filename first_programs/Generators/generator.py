# A generator is a special type of thing, that utilizes a keyward yeild. It can pause and resume functions. For example in this example below we create a list of numbers that are then stored in memory before being recalled. With generators you can generate the list without using up lots of memory.

def make_list(num):
    result = []
    for i in range(num):
        result.append(i*2)
    return result

my_list = make_list(100)
print(my_list)