# Assignment 2 - TASK 1
# Gets and cleans a files contents and creates a 'clean' file given these contents
# Nathan Juguilon

def clean_corrupt_contents():
    '''
    Cleans/organizes the files contents accordingly.
    Inputs: N/A
    Returns: Cleaned file contents
    '''
    file = open('word5Dict.txt','r')
    contents = file.read().strip().split('#')
    
    for i in range(len(contents)):
        contents[i] = contents[i].strip()  # strips words individually 
    file.close()
    
    return contents

def create_clean_file(clean_contents):
    '''
    Creates a new 'clean' file, scrabble5.txt.
    Inputs: the cleaned contents (clean_contents)
    Returns: N/A
    '''
    clean_file = open('scrabble5.txt','w')
    clean_file.write('\n'.join(clean_contents))  # writing of lines
    clean_file.close()
    
def main():
    '''
    Main methods/functionalities of the designed program.
    '''
    clean_contents = clean_corrupt_contents()
    create_clean_file(clean_contents)  
main()