import random

def read_word(file):
    with open(file, 'r') as fp:
        content = fp.read().splitlines()
    choosen_word = random.choice(content)
    print(choosen_word)
    return choosen_word

def get_letter(guess_available):
    letter = input('Guess a letter (' + str(guess_available) + ' guesses available): ')
    return letter

def replace_letters(letter, guess, choosen_word):
    occurrence = 0
    for i, j in enumerate(choosen_word):
        if letter == j:
            guess[i] = letter
            occurrence += 1
    if occurrence:
        print('Yes, there is ' + str(occurrence) + ' letter \'' + str(letter) + '\'')
    else:
        print('No, the letter \'' + str(letter) + '\' is not in my word')

    return guess



def main():
    file_name = 'dictionary'
    choosen_word = read_word(file_name)
    guess = [ ' ' if i == ' ' else '_' for i in choosen_word]
    print('I am thinking of a word. What word is it?:')
    print(' '.join(guess))
    guess_available = 9

    while True:
        letter = get_letter(guess_available)
        guess = replace_letters(letter, guess, choosen_word)
        print(' '.join(guess))

        if ''.join(guess) == choosen_word:
            print('\nCongatulations, you have won!\n')
            break

        guess_available -= 1
        if not guess_available:
            print('\nYou have lost. The word was:\n' + choosen_word)
            break

main()
