# Error Handling
## instead of erroring out if someone inputs a word or last name, it will prompt the user to enter a number. Restarting the function over again till user completes it. Else exicutes right after it is done trying the function, then it will stop running at the break command.
while True:
    try:
        age = int(input('what is your age?'))
        10/age
        raise ValueError('hey cut it out')
    except ValueError:
        print('Please enter a number')
        continue
    except ZeroDivisionError:
        print('Please enter age higher than 0')
        break
    else: 
        print('thank you!')
    finally:
        print('ok, I am finally done')
    print('can you hear me?')

###
# def sum(num1, num2):
#     try:
#         return num1 + num2
#     except TypeError as err:
#         print('Please Enter Numbers! ' + err)

# print(sum('1', 2))