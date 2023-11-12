# create a program which takes random sequence of numbers and letters (example: 'dfssdfsdfsdf655sdf2654fs6d4646'). 
# The program should return (All stages requires separate functions, with logging all necessary data to file and error handling):
# 1) list of letters ordered
# 2) list of letters of reversed order
# 3) funtion which return list with only uniques letters (Can't repeat)
# 4) the same do with numbers (1-3 functions)
# 5)the sum of amount of letters and numbers are provided
# Rules:
# The program after text entered, should provide options list of actions:
# 1) Get list ordered
# 2) Get list ordered reversed etc...

# If there is special symbols,gaps - they should be added to special data structure , as we will have option :
# n) Show special symbols if provided.
# After any option is being used, terminal should ask if we want to use another option or to exit the program.
# If we choose to use another option, the option we already choose should be marked as `checked`:
# 1) Get list ordered[checked]
# sequence length should be nor less than 25 characters 

import logging
from typing import List
import sys

logging.basicConfig(
    level=logging.DEBUG,
    filename='data.log',
    filemode='a',
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%d/%m/%Y %H:%M:%S'
)

string_from_user = input("Please provide a random sequence of numbers and letters: ")

def get_ordered_letters(string_to_order: str) -> str:
    try:
        string_ordered = [char for char in ''.join(sorted(string_to_order))]
        return string_ordered
    except Exception as e:
        logging.exception(f"Error in get_ordered_letters: {e}")
        return ""

def get_reverse_ordered_letters(string_to_order: str) -> str:
    try:
        string_ordered_reversed = [char for char in ''.join(sorted(string_to_order, reverse=True))]
        return string_ordered_reversed
    except Exception as e:
        logging.exception(f"Error in get_reverse_ordered_letters: {e}")
        return ""

def get_unique_letters(string_to_check: str) -> List[str]:
    try:
        unique_letters = []
        for char in string_to_check:
            if char.isalpha() and char not in unique_letters:
                unique_letters.append(char)
        return unique_letters
    except Exception as e:
        logging.exception(f"Error in get_unique_letters: {e}")
        return []

def get_ordered_digits(string_to_order: str) -> str:
    try:
        digits_ordered = sorted(filter(str.isdigit, string_to_order))
        return digits_ordered
    except Exception as e:
        logging.exception(f"Error in get_ordered_digits: {e}")
        return ""

def get_reverse_ordered_digits(string_to_order: str) -> str:
    try:
        digits_ordered_reversed = sorted(filter(str.isdigit, string_to_order), reverse=True)
        return digits_ordered_reversed
    except Exception as e:
        logging.exception(f"Error in get_reverse_ordered_digits: {e}")
        return ""

def get_unique_digits(string_to_check: str) -> List[str]:
    try:
        unique_digits = []
        for char in string_to_check:
            if char.isdigit() and char not in unique_digits:
                unique_digits.append(char)
        return unique_digits
    except Exception as e:
        logging.exception(f"Error in get_unique_digits: {e}")
        return []

def get_special_symbols(string_to_check: str) -> List[str]:
    special_characters = '"!@#$%^&*()-+?_=,<>/"'
    try:
        special_chars = [char for char in string_to_check if char in special_characters or char == " "]
    except Exception as e:
        logging.exception(f"Error in get_special_symbols: {e}")
        return ""

dictionary_of_functions = {
    "To get the list of letters ordered press 1. ": [get_ordered_letters], 
    "To get the list of letters in reverse order press 2. ": [get_reverse_ordered_letters],
    "To get the list of unique letters press 3. ": [get_unique_letters],
    "To get the list of digits ordered press 4. ": [get_ordered_digits],
    "To get the list of digits in reverse order press 5. ": [get_reverse_ordered_digits],
    "To get the list of unique digits press 6. ": [get_unique_digits],
    "To get the list of special symbols press 7.": [get_special_symbols]
    }

def add_checked_flag(key, dictionary):
    if key in dictionary:
        values = dictionary[key]
        if "Checked" not in values:
            values.append("Checked")
    
def select_function_or_leave():
    while True:
        try:
            select_function = int(input("What would be your choice? Please select one of the 7 functions above! If you want to leave, press 0!"))
            if 1 <= select_function <= 7:
                break
            elif select function == 0:
                sys.exit()
            else:
                print("Please enter a number between 1 and 7. If you want to leave, press 0!")
        except Exception as e:
            print("Please enter a valid integer.")
            logging.exception(f"Error in selecting a function: {e}")

while True:    
    for key in dictionary_of_functions:
        print(key)

