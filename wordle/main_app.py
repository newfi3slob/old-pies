# Assignment 2 - TASK 3
# Creates and implements the functionalities required of the Wordle game.
# Nathan Juguilon

from Wordle175 import ScrabbleDict
import random

def chooseTargetWord(file):
    '''
    Randomly chooses a word from a given file.
    Input: file
    Returns: a random target word (targetWord)
    '''
    wordList = list(file.dictionary.keys())
    targetWord = random.choice(wordList)  # chooses random target word
    return targetWord

def getUserGuess(attempt):
    '''
    Prompts the user for their input/guess.
    Input: attempt
    Returns: user guess
    '''
    attempt_str = '\nAttempt ' + str(attempt) + ': '
    guess = input(attempt_str + 'Please enter a 5 five-letter word: ').lower()
    return guess 

def processGuess(targetWord, file):
    '''
    Processes and validates guess attempts.
    Inputs: targetWord, file
    Returns: N/A
    '''
    attempt = 1
    guessedWords = []
    correctGuess = False
    
    while attempt <= 6 and correctGuess == False:
        guess = getUserGuess(attempt)
        
        # VALIDATION of guess input
        if len(guess) > 5:
            print(guess.upper(), 'is too long')
        elif len(guess) < 5:
            print(guess.upper(), 'is too short')
        elif file.check(guess) == False:
            print(guess.upper(), 'is not a recognized word') 
        elif guess in guessedWords:
            print(guess.upper(), 'was already entered')
            
        # with a validated guess - begin PROCESSING
        else:
            guessedWords.append(guess)  # records all valid guessed words
            
            # for each recorded guess - process them and print their feedbacks
            for guess in guessedWords:
                lists = processLetterLists(guess, targetWord)
                printLetterLists(guess, lists)
            if guess != targetWord:
                attempt += 1
            else:
                correctGuess = True
                
    printResults(attempt, targetWord, correctGuess)
            
def processLetterLists(guess, targetWord):
    '''
    Processes a guesses letter lists (i.e. the feedback for a guess)
    Inputs: guess, targetWord
    Returns: the lists (gList, oList, rList)
    '''
    dupLetters = '' 
    gList = []
    oList = []
    rList = []
    for i in range(len(guess)):
        letter = guess[i]
        letterCount = dupLetters.count(letter) + 1
        
        # if letter is a duplicate - label as appropriate
        if guess.count(letter) > 1:
            dupLetters = dupLetters + letter
            letter = letter + str(letterCount)
        
        # if letter is in the right position - add to green list
        if letter[0] == targetWord[i]: 
            gList.append(letter.upper())
        
       # elif letter not in word or letter count is disallowed - add to red list
        elif letter[0] not in targetWord or letterCount > targetWord.count(letter[0]):
            rList.append(letter.upper())
         
        # else - add to orange list   
        else: 
            oList.append(letter.upper())  
            
    return(gList, oList, rList)
            
def printLetterLists(guess, lists):
    '''
    Prints the letter lists of a given guess attempt (i.e. a guesses feedback)
    Inputs: guess and letter lists (lists)
    Returns: N/A
    '''
    gList = sorted(lists[0])
    oList = sorted(lists[1])
    rList = sorted(lists[2])
   
    print(guess.upper(), ' Green={', ', '.join(gList), sep = '', end = '} - ')
    print('Orange={', ', '.join(oList), sep = '', end = '} - ')
    print('Red={', ', '.join(rList), sep = '', end = '}\n')
    
def printResults(attempt, targetWord, correctGuess):
    '''
    Prints the appropriate output given a users attempts/guesses.
    Inputs: attempt, targetWord, correctGuess
    Returns: N/A
    '''
    word = targetWord.upper()
    if correctGuess == True:
        print('Found in ' + str(attempt) + ' attempts. Well done. The word is ' + word)
    else:
        print('Sorry you lose. The word is ' + word)    
    
def main():
    '''
    Main methods/functionalities of the designed Wordle175 program.
    '''
    file = ScrabbleDict(5, 'scrabble5.txt')    
    targetWord = chooseTargetWord(file)
    processGuess(targetWord, file)
main()