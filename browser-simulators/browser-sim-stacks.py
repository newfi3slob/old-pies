#----------------------------------------------------
# Lab 5, Exercise 2: Web browser simulator
# Purpose of program: Simulate webpage browsing through the use of Stacks (ADTs)
#
# Collaborators/references: Lecture Notes
#----------------------------------------------------

from stack import Stack

def getAction():
    '''
    Requests a users action and validates it through a list of approved actions.
    Inputs: N/A
    Returns: a validated character input 
    '''
    validCharacters = ('=', '<', '>', 'q')  # actionable characters
    userInput = input(
        'Enter = to enter a URL, < to go back, > to go forward, q to quit: ')
    
    # if the users input is NOT actionable - raise an exception
    if userInput.lower() not in validCharacters:  # lower for inputs of 'Q'
        raise Exception('Invalid entry.')
    
    # else - return the users input
    else:
        return userInput.lower()
    
def goToNewSite(current, bck, fwd):
    '''
    Requests for a new page URL from the user and simultaneously INSERTS the old
    page into the BACK STACK whilst clearing the FORWARD STACK.
    Inputs: current page (current), back stack (bck), forward stack (fwd)
    Returns: the new page (str)
    '''   
    newPage = input('URL: ')
    bck.push(current)  # inserts old page into 'BACKWARD history'
    fwd.clear()  # clear 'FORWARD history'
    return str(newPage)
    
def goBack(current, bck, fwd):
    '''
    Validates whether the BACK (<) function is actionable, if not then an error
    is displayed and the current page returned; otherwise the FORWARD STACK is
    updated appropriately and back page returned.
    Inputs: current page (current), back stack (bck), forward stack (fwd)
    Returns: the current page OR the back page
    '''    
    # try retrieving the LAST element of the BACK STACK
    try:
        bckPage = bck.pop()
        
    # except, if there's nothing - print an error and return current page
    except Exception as bckException:
        print(bckException.args[0])
        return current
    
    # else - push old page into history and return the back page
    else:
        fwd.push(current)  # inserts old page into 'FORWARD history'
        return bckPage

def goForward(current, bck, fwd):
    '''
    Validates whether the FORWARD (>) function is actionable, if not then an 
    error is displayed and the current page returned; otherwise the BACK STACK
    is updated appropriately and forward page returned.
    Inputs: current page (current), back stack (bck), forward stack (fwd)
    Returns: the current page OR the forward page
    '''    
    # try validating that there is a LAST element in the FORWARD STACK
    try: 
        fwdPage = fwd.peek()
        
    # except, if there's none - print an error and return current page
    except Exception as fwdException:
        print(fwdException.args[0])
        return current
    
    # else - push old page into history and retrieve/return the forward page
    else:
        fwdPage = fwd.pop()
        bck.push(current)  # into 'BACK history'
        return fwdPage

def main():
    '''
    Controls main flow of web browser simulator
    Inputs: N/A
    Returns: None
    '''    
    HOME = 'www.cs.ualberta.ca'
    back = Stack()
    forward = Stack()
    
    current = HOME
    quit = False
    
    while not quit:
        print('\nCurrently viewing', current)
        try:
            action = getAction()
            
        except Exception as actionException:
            print(actionException.args[0])
            
        else:
            if action == '=':
                current = goToNewSite(current, back, forward)
            elif action == '<':
                current = goBack(current, back, forward)
            elif action == '>':
                current = goForward(current, back, forward)
            elif action == 'q':
                quit = True
            
            
    print('Browser closing...goodbye.')    

        
if __name__ == "__main__":
    main()  