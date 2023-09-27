#----------------------------------------------------
# Lab 4: Web browser simulator
# Purpose of program: Simulates the utilities of a webpage browsers search bar.
#
# Collaborators/references: None
#----------------------------------------------------

def getAction():
    '''
    Requests a users action and validates it through a list of approved actions.
    Inputs: N/A
    Returns: a validated user input
    '''
    
    validCharacters = ('=', '<', '>', 'q')  # actionable characters
    userInput = None 
    
    # while the users input is NOT actionable - request for input
    while userInput not in validCharacters:
        userInput = input(
        'Enter = to enter a URL, < to go back, > to go forward, q to quit: ')
        
        # if the users input is invalid - print an error message
        if userInput not in validCharacters:
            print('Invalid entry.')
            
    return userInput

def goToNewSite(current, pages):
    '''
    Requests for a new page URL from the user and updates the appropriate page
    lists and indexes. If the pages index does not exist then add it. Otherwise,
    replace it and remove any page indexes greater than current.
    Inputs: current website index (current), websites list (pages)
    Returns: the new pages index
    '''   
    
    newPage = input('URL: ')
    newIndex = current + 1 
    
    # if the new pages index does not exist - append it to the pages list
    if newIndex not in range(len(pages)):
        pages.append(newPage)  # adds page to the recorded list of pages
        
    # else if it does exist - replace the old page with the new one
    else:
        pages[newIndex] = newPage
        
        # for each pages index in the pages list
        for pageIndex in range(len(pages)):
            
            # if its index is greater than the new one - remove it from the list
            if pageIndex > newIndex:
                page = pages[pageIndex]
                pages.remove(page)
    
    return newIndex
  
def goBack(current, pages):
    '''
    Validates whether the BACK (<) function is actionable, if not then an error
    message is returned with the current index; otherwise the page index is 
    updated as appropriate.
    Inputs: current website index (current), websites list (pages)
    Returns: the previous pages index OR the current page index
    '''    
    
    # if 'previous' index is not in range of pages - print error and return index
    if current - 1 not in range(len(pages)):
        print('Cannot go back.')
        return current
    
    # else - return the 'previous' pages index
    else: 
        previousIndex = current - 1
        return previousIndex

def goForward(current, pages):
    '''
    Validates whether the FORWARD (>) function is actionable, if not then an 
    error message is returned with the current index; otherwise the page index 
    is updated as appropriate.
    Inputs: current website index (current), websites list (pages)
    Returns: the next pages index OR the current page index
    '''    
    
    # if 'next' index is not in range of pages - print error and return index
    if current + 1 not in range(len(pages)):
        print('Cannot go forward.')
        return current
    
    # else - return the 'next' pages index
    else:
        nextIndex = current + 1
        return nextIndex

def main():
    '''
    Controls main flow of web browser simulator
    Inputs: N/A
    Returns: None
    '''    
    HOME = 'www.cs.ualberta.ca'
    websites = [HOME]
    currentIndex = 0
    quit = False
    
    while not quit:
        print('\nCurrently viewing', websites[currentIndex])
        action = getAction()
        
        if action == '=':
            currentIndex = goToNewSite(currentIndex, websites)
        elif action == '<':
            currentIndex = goBack(currentIndex, websites)
        elif action == '>':
            currentIndex = goForward(currentIndex, websites)
        elif action == 'q':
            quit = True
    
    print('Browser closing...goodbye.')    

        
if __name__ == "__main__":
    main()