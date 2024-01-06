print('Welcome to evans tip calculator');

total_bill = input("What was the total bil: $")


percentage_tip = input('What percentage tip would you like to give ? 10, 12 or 15?')



total_friends = input('How many people want to split the bill?')

bill_percentage_tip = int(total_bill) * (1.00 + int(percentage_tip) / 100)

total_tip = round(bill_percentage_tip / int(total_friends), 2)

print(f'Each of you should tip: $ {total_tip}')

