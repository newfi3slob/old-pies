# Mini Project 1 - Word Puzzle
# Has user guess letters of random word & outputs result based on user attempt

import random

# instruction func.
def print_instructions():   # prints instructions
    filename = "word-puzzle\wp_instructions.txt"
    filemode = "r"  
    file = open(filename, filemode)
    contents = file.read()
    file.close()    
    print(contents)
    
# initial puzzle disp func.
def init_puzzle_disp(scrt_wrd): # prints initial puzzle disp
    print('The answer so far is '+ '_ ' * len(scrt_wrd))
    
# updated puzzle disp func.
def upd_puzzle_state(new_disp): # prints updated puzzle display
    print('The answer so far is '+ new_disp)

# game win output
def good_end(scrt_wrd): # prints winning output
    print('Good job! You found the word '+ scrt_wrd +'!')
    
# game lose output
def bad_end(scrt_wrd):  # prints losing output
    print('Not quite, the correct word was '+scrt_wrd+'. Better luck next time')
     
# game result output
def print_result(new_disp, scrt_disp, scrt_wrd):    # prints output results
    if new_disp == scrt_disp:   
        output = good_end(scrt_wrd)     # defined different outputs
    else:
        output = bad_end(scrt_wrd)
    return output
    
# main func.
def main(): # main game functions
    guess_amt = 4
    guessed_letters = []
    new_disp = ''
    blanks = ' '
    scrt_wrd = random.choice(
        ['apple', 'banana', 'watermelon', 'kiwi', 'pineapple', 'mango'])
    scrt_wrd_list = list(scrt_wrd)
    scrt_disp = blanks.join(scrt_wrd_list)
    print_instructions()
    init_puzzle_disp(scrt_wrd)
    while guess_amt != 0 and new_disp != scrt_disp:
        new_disp_list = []
        guess = input('Guess a letter ('+str(guess_amt)+' guesses remaining): ')

        if len(guess) > 1:      # added validation aspect for guess (length check)
            print('Only guess a single letter')
            guess_amt += 1      # lazy implementation of relief for guess_amt deduction

        if guess in scrt_wrd_list:      # nested loops for tracking guesses
            if guess in guessed_letters:
                guess_amt -= 1
            for letter in scrt_wrd_list:
                if letter in guessed_letters:
                    new_disp_list += letter
                elif letter == guess:           
                    new_disp_list += guess
                    guessed_letters.append(guess)
                else:
                    new_disp_list += '_'

        else:
            for letter in scrt_wrd_list:
                if letter in guessed_letters:
                    new_disp_list += letter
                else:
                    new_disp_list += '_'
            guess_amt -= 1
        new_disp = blanks.join(new_disp_list)
        upd_puzzle_state(new_disp)   
    print_result(new_disp, scrt_disp, scrt_wrd)
    input('Press enter to end the game')
main()    