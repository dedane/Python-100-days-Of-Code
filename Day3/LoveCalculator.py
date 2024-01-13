print('welcome to Evans love calculator')

your_name= input('What is your name? ')
crushes_name= input('What is your crushes name? ' )



combined_names = your_name + crushes_name

lowercase_names = combined_names.lower()

t = lowercase_names.count('t')
r = lowercase_names.count('r')
u = lowercase_names.count('u')
e = lowercase_names.count('e')

true = t+r+u+e

l = lowercase_names.count('l')
o = lowercase_names.count('o')
v = lowercase_names.count('v')
e = lowercase_names.count('e')

love = l+o+v+e

lovescore = int(true) + int(love)

if (lovescore < 10) and (lovescore > 90):
    print(f'your score is {lovescore}, you go together like coke and mentos')
elif(lovescore > 40) and (lovescore <50):
    print(f'your lovescore is {lovescore}, you alright together')
else:
    print(f'your lovescore is {lovescore}, you shouldnt be together')

