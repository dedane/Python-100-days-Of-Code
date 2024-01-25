for number in range (1,100):
    if number % 3 == 0 and number % 5 == 0: 
        print('fizz')
    elif number % 5 == 0:
        print('buzz')
    elif number % 3 == 0:
        print('fizzBuzz')
    else:
        print(f'{number}')