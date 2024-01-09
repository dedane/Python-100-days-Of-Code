year = int(input('which year do you want to check: '))

if year % 4 == 0 :
    if year % 100 != 0:
        print('leap year')
    elif year % 400 == 0:
            print('this is a leap year')
else:
    print('This is not a leap year')
