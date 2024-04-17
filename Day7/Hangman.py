#Step 1 
import random
word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
print(chosen_word)

chosen_letter = list(chosen_word)
print(chosen_letter)
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input('Guess a letter available in the word list: ')
guess.lower()
#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
for i in chosen_word:
    if i == guess:
        print('Your letter is available in the word')
    elif i !=  guess:
        print('-')


