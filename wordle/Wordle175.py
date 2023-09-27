# Assignment 2 - TASK 2 + TASK 4
# Creates and tests the ScrabbleDict class and all of its methods.
# Nathan Juguilon

# TASK 2 - Class Creation
class ScrabbleDict:
    '''
    The ScrabbleDict class and its attributes/methods
    '''
    def __init__(self, size, filename):
        '''
        Initializes the ScrabbleDict classes main attributes.
        Input: Size attribute (size) and words file (filename)
        Returns: N/A
        '''
        self.size = size
        
        # getting filenames contents
        file = open(filename, 'r')
        contents = file.readlines()
        
        # dictionary initialization
        self.dictionary = {}
        
        # for each line in contents - separate the word and its definition
        for line in contents:
            lineContents = line.strip().split()  # ASSUMING WHITESPACE IS SEPARATOR
            
            # if the words length is right size - add it to dictionary
            if len(lineContents[0]) == size:
                key = lineContents[0]
                self.dictionary[key] = line.strip()
            
            # else - don't add it (i.e. do nothing)
            else:
                None  
                
    def check(self, word):
        '''
        Checks if word is in dictionary.
        Input: A word (word)
        Returns: True or False
        '''
        # if the word is in the dictionary - return True, else return False
        if str(word) in self.dictionary.keys():
            return True
        return False
    
    def getSize(self):
        '''
        Returns number of words in dictionary.
        Input: N/A
        Returns: Number of words (self.dictionary length)
        '''
        return len(self.dictionary)
    
    def getWords(self, letter):
        '''
        Returns a sorted list of words from dictionary starting with the
        character letter.
        Input: Character letter (letter)
        Returns: Sorted word list
        '''
        wordList = []
        
        # for each word in the dictionary
        for word in self.dictionary.keys():
            
            # if the words first letter matches - append the word to wordList
            if word[0] == letter:
                wordList.append(word)
                
            # else do nothing
            else:
                None  
                
        return sorted(wordList)
    
    def getWordSize(self):
        '''
        Returns the length of the words stored in the dictionary.
        Input: N/A
        Returns: The word length (self.size)
        '''
        return self.size
    
    # TASK 4 - ADDITIONAL METHODS
    def getMaskedWords(self, template):
        '''
        Gets a list of words that fit within a given template.
        Inputs: template
        Returns: a sorted list of words (wordList)
        '''
        wordList = []
        
        # for every word in the dictionary - validate a character match
        for word in self.dictionary.keys():
            match = True
            for i in range(len(word)):
                
                # if the templates character isnt a star and doesn't match
                if template[i].lower() != '*' and template[i].lower() != word[i]:
                    match = False  # then a match is INVALID
                    
            # if a character match is found - add the word to the wordList
            if match == True:
                wordList.append(word)
                
        return sorted(wordList)
        
    def getConstrainedWords(self, template, letters):
        '''
        Gets a list of words constrained to a given template and letters.
        Input: template and a set of wildcards (letters)
        Returns: a sorted list of words (wordList)
        '''
        wordList = []    
        maskedWords = self.getMaskedWords(template)
        
        for word in maskedWords:
            
            # if wildcard inputs are empty - return templates possible words
            if letters == {''}:
                match = True
            
            # else - validate a match between wildcards and letters
            else:
                match = False
                for i in range(len(word)):
                    
                    # if a words letter fits a wildcard - validate the match
                    if template[i].lower() == '*' and word[i] in letters:
                        match = True
             
            # if a character match is found - add the word to the wordList
            if match == True:
                wordList.append(word)
                
        return sorted(wordList)
                 
# ScrabbleDict class testing
if __name__ == '__main__':
    '''
    Area for testing class methods/functions.
    Input: N/A
    Returns: N/A
    '''
    test = ScrabbleDict(5, 'scrabble5.txt')
    testSep = '\n----------------------------------'
    
    # TASK 2 METHOD TESTS
    # check that dictionary size is correct - should be 8913
    print('Does getSize() == 8913?', test.getSize() == 8913, testSep)
    
    # ensure only VALID words are allowed in the dictionary check method
    words = ('agony', 'aGOny')
    
    for word in words:
        print('Is ' + word + ' valid?', test.check(word), testSep)
    
    # test if getWords method works 
    lowerLetter = 'x'
    upperLetter = 'X'  # ASK ABOUT UPPER AND LOWER INPUTS

    print(test.getWords(lowerLetter), testSep)
    
    # ensure getWordSize method works
    print('Does getWordSize == 5?', test.getWordSize() == 5)