import random
"""
"""

def main():
    # Set up two random numbers
    replay = 2
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    print("Enter 2 numbers between 1 and 100.")
    
    while replay != 0:
        # Loop to keep asking for numbers until the user gets it right
        game_result = get_numbers(num1, num2)
        
        # If they wish to play again, regenerate the random numbers
        if game_result == 1:
            replay = 1
            num1 = random.randint(1, 100)
            num2 = random.randint(1, 100)
            
        # End the game if they don't want to play again
        if game_result == 0:
            replay = 0

def get_numbers(num1, num2):
    # Get two numbers from the user to compare to the randomly generated numbers
    print("Enter two whole numbers between 1 and 100")
    number1 = input("Enter your first number: ")
    number2 = input("Enter your second number: ")
    
    #make the numbers integers if possible
    try:
        number1 = int(number1)
    except ValueError:
        pass
    try:
        number2 = int(number2)
    except ValueError:
        pass
    # check to see if it is setting them correctly
    # print(type(number1))
    # since this program calls the print error more I just made the text a variable
    errorresp = "Please enter a valid whole number between 1 and 100"
    if (type(number1) == int):
        if (type(number2) == int):
        # Process integer input
        # Check if the user's numbers are out of bounds
            if number1 < 1 or number1 > 100 or number2 < 1 or number2 > 100:
                print(errorresp)
            else:
                # error check to see if it catches if the first and second number are valid data types but are out of bounds
                # print("first else, Out of Bounds")
                # Call the check function to see if any of the numbers from the user match the random numbers
                result = check(number1, number2, num1, num2)
                # Check to see if values produced desired "result"
                # print(result)
                return result
        else:
            # error check to see if it catches if the first number is a valid data type and the second is not
            # print("second else, invalid number2")
            print(errorresp)
    else:
        # Process float input
        # error check to see if it catches if the first number is a invalid data type and the second is not
        # print("final else, invalid number1")
        print(errorresp)
   


def check(number1, number2, num1, num2):
       
    # If both numbers are wrong, check if they are high or low
    if number1 != num1 or number2 != num2:
        # If a number is high, check if just one is or if both are
        if number1 > num1 or number2 > num2:
            if number1 <= num1 or number2 <= num2:
                print("One is more")
            else:
                print("Both are high")
        
        # If a number is low, check if just one is or if both are
        if number1 < num1 or number2 < num2:
            if number1 >= num1 or number2 >= num2:
                print("One is less")
            else:
                print("Both are low")
        
    # If both numbers are correct, ask if they want to play again
    else:
        print("You are correct!")
        replay = int(input("Would you like to play again? (Enter 1 for yes or 0 for no): "))
        
        # Exit the program if they don't want to play again
        if replay == 0:
            return replay
        
        # If they want to play again, return 1 to main
        if replay == 1:
            return replay
    
    # If all else fails, loop through again with the same two numbers
    return 2

# Start the game
main()