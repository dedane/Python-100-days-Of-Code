print('Welcome to Evans Pizza Deliveries')

size = input("What size of pizza do you want? S, M, L ")
size_price=0
print(type(size))

add_pepperoni = input('Do you want pepperoni? Y or N ')
pepperoni_prize=0

extra_cheese = input('Do you want extra cheese? Y or N ')
extra_cheese_prize=0

if size == "S":
    size_price += 15
    print(f'price of of pizza is {size_price}')
    if add_pepperoni == "Y":
        pepperoni_prize += 2
        

elif size == "M":
    size_price += 20
    print(f'price of of pizza is {size_price}')
    if add_pepperoni == "Y":
        pepperoni_prize += 3
        
else:
    size_price += 25
    print(f'price of of pizza is {size_price}')
    if add_pepperoni == "Y":
        pepperoni_prize += 3
        


if extra_cheese == "Y":
    extra_cheese_prize += 1
    

else:
    print(f'price of of pizza is {size_price}') 

final_bill=size_price + pepperoni_prize + extra_cheese_prize
print(type(final_bill))

print(f'Your final bill is: {final_bill}')
