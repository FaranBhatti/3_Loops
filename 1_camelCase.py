"""
File name:                   1_camelCase.py
Description:                 converting use inputted camelCase notation to - > snake_case notation
Created:                     Faran Bhatti
Edited:                      2023-02-17 by Faran Bhatti (FB)
Last Edited:                 2023-02-17 by Faran Bhatti (FB)
"""

def main():
    # Taking in user input for the camelCase
    camelCase = input("camelCase: ")

    # Converting the camelCase to snake_case and storing into snake_case variable
    snake_case = camel_to_snake(camelCase)

    # Print the result
    print("snake_case: " + snake_case)

def camel_to_snake(camelCase):
    snake_case = ""
    for letter in camelCase:
            # If it's upper replace it with an _ and lowercase version of itself
        if(letter.isupper()):
            snake_case += "_" + letter.lower()
        else:
            snake_case += letter
    return snake_case

main()