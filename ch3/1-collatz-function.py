# this is the collatz function, its parameter is number. 'number' and all other variables inside this function are in local scope
def collatz( number ):
    # inside the if statement, we check if number is divisible by 2, with the modulo operator
    if ( number % 2 == 0 ):
        print( number // 2 )
        return( number // 2 )
    # similarly, we check if the number leaves a reminder when devided by 2, meaning it is odd
    elif ( number % 2 == 1 ):
        print( 3 * number + 1 )
        return( 3 * number + 1 )
# this is the end of the collatz function