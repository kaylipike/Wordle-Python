
from colorama import Fore  # used to return colored version of user guess
import random  # used to randomly select the secret word
import re  # used to ensure user guess is a 5 letter word
from collections import Counter


def validate_word(guess, sw, count_guesses, list_guesses, lst):
    if re.match("^[A-Za-z]+$", guess):  # no other special characters/numbers
        if len(guess) != len(sw):  # if guess is too long or too short
            print("The word needs to be 5 letters. Try again please. ")
            print(f"You have {10 - count_guesses} guesses remaining. ")
            return False
        elif guess in list_guesses:
            print("You have already guessed this word. Please try again. ")
            print(f"You have {10 - count_guesses} guesses remaining. ")
            return False
        elif guess not in lst:
            print("That is not in the word list. Please try again. ")
            print(f"You have {10 - count_guesses} guesses remaining. ")
            return False
        else:
            return True
    else:
        print(f"Invalid input. Your input should contain only letters. "
              f"You still have {10 - count_guesses} guesse(s). ")
        return False


def create_word_lst(txt_file):
    with open(txt_file, 'r') as lst_of_words:
        lst = []
        for row in lst_of_words:
            word = row
            lst.append(word.strip())  # makes no accidental extra white spaces
    return lst


def wordle():
    guesses = 0
    word_lst = create_word_lst('sgb-words.txt')
    secret_word = random.choice(word_lst)
    print("Try to guess the secret word.")
    print("The secret word you need to guess will be randomly "
          "selected from a list. ")
    print("You will have 10 guesses. ")
    print("If you do not get it correct in 10 guesses you will be "
          "told what the secret word was. ")
    print("For each guess, the letters of your guess that are correct "
          "will turn green. ")
    print("Letters that are in the secret word but in the wrong "
          "place compared to the secret word will turn yellow. ")
    print("Letters of your guess that are not in the secret word "
          "will turn red. ")
    print("Note: Your guesses do not have to be real words to be checked, "
          "but if you want to make things harder for yourself then be sure "
          "that your guesses are actual words in the English language. ")
    guess_check = []
    while True:
        occur_positions = {}
        output = ['R', 'R', 'R', 'R', 'R']
        gw_counts = Counter()
        sw_counts = Counter()
        user_word = input(f'{Fore.RESET}' "Enter your 5-letter word "
                          "guess: ").lower()  # makes guesses all lowercase
        word = user_word
        gw_counts.update(word)
        sw_counts.update(secret_word)
        validation = validate_word(word, secret_word, guesses, \
                                   guess_check, word_lst)
        if validation:
            if word == secret_word:
                print(Fore.GREEN + user_word)
                print(Fore.RESET + f"You have correctly guessed the word! "
                      f"Congratulations! It took you {guesses} guesses. ")
                play_again = input("Do you want to play again? Y/N? ")
                break
            else:
                for i, letter in enumerate(word):
                    if letter == secret_word[i]:
                        output[i] = 'G'
                        occur_positions[letter] = i

                for i, letter in enumerate(word):
                    if letter in secret_word and output[i] != 'G':
                        if letter not in occur_positions:
                            output[i] = 'Y'
                            occur_positions[letter] = i
                            if sw_counts[letter] > 1:
                                sw_counts[letter] = sw_counts[letter] - 1
                                del occur_positions[letter]
                for i, label in enumerate(output):
                    if label == 'G':
                        print(Fore.GREEN + word[i], end='')
                    elif label == 'Y':
                        print(Fore.YELLOW + word[i], end='')
                    else:
                        print(Fore.RED + word[i], end='')
                guess_check.append(word)
                guesses = guesses + 1  # keeps track of number of guesses
                print('')
                print(Fore.BLACK + f"You have {10 - guesses} guesses "
                      "remaining. ")
        if guesses == 10:  # if user has run out of guesses
            print(Fore.RESET + f"You are out of guesses! The word was "
                  f"{secret_word}. ")
            break


if __name__ == '__main__':
    while True:
        game = wordle()
        play_again = input("Do you want to play again? Y/N ")
        if play_again.upper() != 'Y':
            break
