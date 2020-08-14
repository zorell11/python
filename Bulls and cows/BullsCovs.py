import random
import time

#############################################################################################
# print greetings at the beginning
def print_intro():
    print('''
Hi there!
Welcome on game Bulls and Cows.
I've generated a secret random 4 digit number for you.
Your task is to guess, what number it is.
Enter a 4 digit number where
    * the digits will not repeat and
    * the number cannot begin with 0.
If the matching digits:
    * are in their right positions, they are "bulls",
    * if in different positions, they are "cows".
Try to guess what number I am thinking of
''')

#############################################################################################
# get username
def get_username():
    name = input('Add your username: ')
    return name if name != '' else '-'
#############################################################################################
# generate random 4 digit number
def generate_number():
    number = random.sample(range(9), k=4)
    while True:
        if number[0] == 0:
            random.shufle(number)
        else:
            break
    return number

#############################################################################################
# check if the user provided valid number
def check_guess(guess_number):
    if guess_number == 'q':
        print('GoodBye')
        exit()
    elif not guess_number.isnumeric():
        print('Wrong input. Guess needs to be a number.')
        return False
    elif guess_number.isnumeric() and (not len(guess_number) == 4):
        print("Wrong input. Guess needs to be a 4 digit number.")
        return False
    elif len(set(guess_number)) != 4:
        print("Wrong input. Guess cannot contain duplicate digits.")
        return False
    else:
        return True

#############################################################################################
# get number from user
def read_gues(num_guess):
    guess = []
    while True:
        guess_number = input('>>>> ')
        num_guess += 1
        if check_guess(guess_number):
            for i in str(guess_number):
                guess.append(int(i))
            break
    return guess, num_guess

#############################################################################################
# counting the bulls and cows
def count_bulls_cows(guesed_number, guess):
    bulls, cows = 0, 0
    for i in range(len(guesed_number)):
        if guesed_number[i] == guess[i]:
            bulls += 1
        elif guess[i] in guesed_number:
            cows += 1
    return bulls, cows

#############################################################################################
# time to guess the number - hours, minutes and seconds
def count_time(start, end):
    time = round(end - start)
    hours, min_sec = divmod(time, 3600)
    minutes, seconds = divmod(min_sec, 60)
    time = '{:02}:{:02}:{:02}'.format(hours, minutes, seconds)
    return time

#############################################################################################
# save username and statistics to file
def save_to_file(name, num_guess, elapsed_time):
    with open('bulls_and_covs_statistics.txt', 'a') as file:
        text = '{}\t{}\t{}\n'.format(name, num_guess, elapsed_time)
        file.write(text)
#############################################################################################
# MAIN function
#############################################################################################
def main():
    print_intro()
    username = get_username()
    guesed_number = generate_number()
    #print('secret number is:', guesed_number)
    num_guess = 0
    start = time.time()
    while True:
        guess, num_guess = read_gues(num_guess)
        if guess == guesed_number:
            print('Correct, you\'ve guessed the right number in %d guesses!' % num_guess)
            end = time.time()
            elapsed_time = count_time(start, end)
            print('Your guessing time is %s' % elapsed_time)
            break
        else:
            print( '{} bulls, {} cows'.format(*count_bulls_cows(guesed_number, guess)))
    save_to_file(username, num_guess, elapsed_time)


main()
