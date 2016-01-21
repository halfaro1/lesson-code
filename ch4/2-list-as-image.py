#this is just the grid variable, given in the instructions
grid =[ ['.', '.', '.', '.', '.', '.'], 
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'], 
        ['.', 'O', 'O', 'O', 'O', 'O'], 
        ['O', 'O', 'O', 'O', 'O', '.'], 
        ['O', 'O', 'O', 'O', '.', '.'], 
        ['.', 'O', 'O', '.', '.', '.'], 
        ['.', '.', '.', '.', '.', '.']]
        
#this is the outer loop, it iterates through each column (vertical)
for column in range(6):
    #this is the inner loop, it iterates through each row (horizontal)
    for row in range(9):
        #each time we encounter an item horizontally print it out
        print( grid[row][column], end=' ' ) #the end=' ' statement just prints a space at the end of the print statement, instead of a new line
    #this adds a line break after each column is printed
    print()
