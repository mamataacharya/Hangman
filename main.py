

# WORDLIST_FILENAME = "words.txt"

import random
import time


def word_selected(fname):  # select a random word from a text file
    word_file = open('words.txt', 'r+')
    word = random.choice(word_file.read().split())
    word_file.close()
    return word


word = word_selected('words.txt')


def word_selected_dashed():
    word_selected_dashed = []
    for i in range(len(word)):
        word_selected_dashed.append('_')
    return ''.join(word_selected_dashed)


print('The word contains', len(word), 'letters')

word_selected_dashed = word_selected_dashed()
print(word_selected_dashed)

trials = 5

guessed_word = list(word_selected_dashed)

while trials > 0:
    a = 0
    if ''.join(guessed_word) == word:
        print("Congratulations, you have guessed the correct word")
        break

    print('you have got ' + str(trials) + ' wrong tries ')
    user_guessed_letter = input('Guess a letter >>>>> \n')

    if user_guessed_letter in word:
        print('Correct!')
        for i in range(len(word)):
            if list(word)[i] == user_guessed_letter:
                guessed_word[i] = user_guessed_letter
        print(''.join(guessed_word))

    elif user_guessed_letter not in word:
        print('wrong!')
        trials -= 1
        tries = (4 - trials)
        print(user_guessed_letter, 'is not in my word')
        print(''.join(guessed_word))
        if trials == 4:
            print('------------')
            print('     |      ')
            print('     O      ')
        elif trials == 3:
            print('------------')
            print('     |      ')
            print('     O      ')
            print('     |      ')
        elif trials == 2:
            print('------------')
            print('     |      ')
            print('     O      ')
            print('   / | \    ')
        elif trials == 1:
            print('------------')
            print('     |      ')
            print('     O      ')
            print('   / | \    ')
            print('     |      ')
        elif trials == 0:
            print('------------')
            print('     |      ')
            print('     O      ')
            print('   / | \    ')
            print('     |      ')
            print('   / | \    ')

if trials == 0:
    print('Oops!! looks like you lost the game')
    print('The word you could not guess was ', word)

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the last lines to test
# (hint: you might want to pick your own
# word while you're doing your own testing)


# -----------------------------------

# Driver function for the program
if __name__ == "__main__":
    print()
# Uncomment the line below once you have finished testing.
# word = choose_random_word(wordlist)

# Uncomment the line below once you have implemented the hangman function.
# hangman(word)
