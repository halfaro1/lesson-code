#this defines a function with one parameter, 'theList'
def printList( theList ):
    # this for loop iterates through each item in the list, except the last item
    for i in range( len(theList)-1 ): #can you remember what this line does?
        #this will add a comma after each list item
        print( str(theList[i]) + ',', end=' ')
        
    #the last list item doesn't need to be followed by a comma
    print( 'and ' + str(theList[ len(theList)-1 ]) )

#this is the end of what was asked in the question, the following lines are just to test the function we wrote

spam = ['apples', 'bananas', 'tofu', 'cats']
printList( spam )