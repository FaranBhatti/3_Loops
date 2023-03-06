"""
File name:                   3_twttr.py
Description:                 When texting or tweeting, it's not uncommon to shorten words to save time or space, as by omitting
                             vowels, much like Twitter was originally called twttr. In this file, we will implement a program that prompts the user for a str of text and outputs that same text but with all the vowels (A, E, I, O, and U) omitted, whether inputted in lowercase or uppercase.
Created:                     Faran Bhatti
Edited:                      2023-03-01 by Faran Bhatti (FB)
Last Edited:                 2023-03-08 by Faran Bhatti (FB)
"""

def main():
    input_string = input("Input: ")
    output_string = ""
    
    for letter in input_string:
        if (not check_for_vowel(letter)):
            output_string += letter
            
    print("Output: " + output_string)
    

def check_for_vowel(letter):
    match (letter):
        case 'a':
            return True
        case 'A':
            return True
        case 'e':
            return True
        case 'E':
            return True
        case 'i':
            return True
        case 'I':
            return True
        case 'o':
            return True
        case 'O':
            return True
        case 'u':
            return True
        case 'U':
            return True
        case _:
            return False
        
main()
