# def divide_two_nums(first_num:int, second_num:int) -> float:
#     try:
#         return first_num / second_num
#     except Exception as e:
#         print(f"Encountered exception: {e}.")
        

# def betkas(first_num:int, second_num:int) -> int:
#     answer = divide_two_nums(first_num, second_num)
#     if not answer:
#         return 0
#     else:
#         return answer ** 2

# print(betkas(5,0))

# Create a program which takes a sentence as your birth dau (YYYY:MM:DD)
# The program should return sum of all numbers, bigest and lowest number division 
# and days with power of month (dd ** mm)
# The code should be structured correctly: functions, error handling and logging.

import logging
import re
from typing import List

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def is_valid_date(inputed_birth_date):
    date_pattern = r'^\d{4}:\d{2}:\d{2}$'
    return bool(re.match(date_pattern, inputed_birth_date))

def input_to_variables() -> List[int]:
    try:
        user_date = input("Please provide your birth date in the format: YYYY:MM:DD :")
        if not is_valid_date(user_date):
            raise ValueError("Invalid input. Please provide a valid date in the format: YYYY:MM:DD")
        else:
            date_into_list = [int(number) for number in user_date.split(':')]
        if date_into_list[1] > 12:
            raise ValueError("Invalid input. Month should be between 1 and 12.")
        if date_into_list[2] > 31:
            raise ValueError("Invalid input. Day should be between 1 and 31.")
        if any(num < 1 for num in date_into_list):
            raise ValueError("Invalid input. All components (year, month, day) should be greater than or equal to 1.")
        logging.info(f"Input validated successfully: {date_into_list}")
        return date_into_list
    except ValueError as ve:
        logging.error(f"Error in input validation: {ve}")
        return []
    except Exception as e:
        logging.error(f"Encountered unexpected error: {e}")
        return []

def sum_of_all_nums(numbers_from_date: List[int]) -> int:
    if not numbers_from_date:
        raise ValueError("Cannot perform actions with the result from the previous function.")
    result = sum(numbers_from_date)
    logging.info(f"Sum of all numbers: {result}")
    return result

def find_min_max_division(numbers_from_date: List[int]) -> float:
    if not numbers_from_date:
        raise ValueError("Cannot perform actions with the result from the previous function.")
    try:
        min_num = min(numbers_from_date)
        max_num = max(numbers_from_date)
        result = max_num / min_num
        logging.info(f"Max/Min division: {result}")
        return result
    except Exception as e:
        logging.error(f"Encountered exception: {e}")
        return 0

def days_with_power_of_month(numbers_from_date: List[int]) -> int:
    if not numbers_from_date:
        raise ValueError("Cannot perform actions with the result from the previous function.")
    result = numbers_from_date[2] ** numbers_from_date[1]
    logging.info(f"Days with power of month: {result}")
    return result

numbers = input_to_variables()

if not numbers:
    logging.error("Error in obtaining input.")
else:
    try:
        sum_of_all_nums(numbers)
        find_min_max_division(numbers)
        days_with_power_of_month(numbers)
    except ValueError as ve:
        logging.error(f"Error in calculations: {ve}")
    except Exception as e:
        logging.error(f"Encountered unexpected error: {e}")







