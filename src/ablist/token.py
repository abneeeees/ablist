from ablist.argument import *
from datetime import datetime
import re

# Tokens are nothing but a fancy word given to the arguments given in the command line.

#  Key difference is here they will be seperated based on charactersics
# Each token will stored in their respective list type
# A list type is a list of specific types such as dates, string, integer, float, uppercase, etc ....

## Initially every argument taken is a string there it is need to be converted into their list type hence store there 


# ----------------------------------------
# TextBased Tokens are stored in this class
# ----------------------------------------
 
class TextBasedListType:
    def __init__(self):
        self.capitalize_regex = r'^[A-Z][a-z]+$'
        self.special_char_only_regex = r'^[^a-zA-Z0-9\t\n ]+$'

    # examples: admin, password, user
    def lowercase_tokens(self, word:str) -> bool:
        return word.isalpha() and word.islower()

        # examples: ADMIN, ROOT, USER
    def uppercase_tokens(self, word:str) -> bool:
        return word.isalpha() and word.isupper()

        # examples: admin123, user2024, pass01
    def alphanumeric_tokens(self, word:str) -> bool:
        return word.isalnum() and not word.isalpha() and not word.isdigit()
    
        # examples: Admin, Password, User
    def capitalized_tokens(self, word:str) -> bool:
        return bool(re.match(self.capitalize_regex, word))

        # examples: @@@, ###, !!!, $$
    def special_char_only_tokens(self, word:str) -> bool:
        return bool(re.match(self.special_char_only_regex, word))

# ----------------------------------------
# Number Tokens are stored in this class
# ----------------------------------------

class NumberBasedListType:
    def __init__(self):
        self.integer_regex = r'^[+-]?\d+$'
        self.floater_regex = r'^[+-]?\d+\.\d+$'
        self.short_number_regex = r'^[+-]?\d{1,5}$'
        self.long_number_regex = r'^[+-]?\d{6,}$'
        self.padded_number_regex = r'^[0]{1,}+[0-9]{1}+$'

        # examples: 3.14, 0.99
    def int_tokens(self, word:str) -> bool:
        return bool(re.match(self.integer_regex, word))

        # examples: 3.14, 0.99
    def float_tokens(self, word:str) -> bool:
        return bool(re.match(self.floater_regex, word))

        # examples: 1, 7, 9
    def short_number_tokens(self, word:str) -> bool:
        return bool(re.match(self.short_number_regex, word))

        # examples: 123456, 987654321
    def long_number_tokens(self, word:str) -> bool:
        return bool(re.match(self.long_number_regex, word))

        # examples: 001, 007, 0001
    def padded_number_tokens(self, word:str) -> bool:
        return bool(re.match(self.padded_number_regex, word))
    
# ----------------------------------------
# DateTime Tokens are stored in this class
# ----------------------------------------
 
class DateTimeListType:
    def __init__(self):
        self.WEEKS = {
            'monday', 'tuesday', 'wednesday',
            'thursday', 'friday', 'saturday', 'sunday'
        }

        self.MONTHS = {
            'january', 'february', 'march',
            'april', 'may', 'june',
            'july', 'august', 'september',
            'october', 'november', 'december'
        }

        self.DDMMYYYY_FORMATS = (
            '%d-%m-%Y',
            '%d/%m/%Y',
            '%d\\%m\\%Y',
        )

        self.YYYYMMDD_FORMATS = (
            '%Y-%m-%d',
            '%Y/%m/%d',
            '%Y\\%m\\%d',
        )

        self.TIME_FORMATS = (
            '%H:%M',
            '%H:%M:%S',
        )

    def is_date_ddmmyyyy(self, word: str) -> bool:
        for fmt in self.DDMMYYYY_FORMATS:
            try:
                datetime.strptime(word, fmt)
                return True
            except ValueError:
                pass

        return False

    def is_date_yyyymmdd(self, word: str) -> bool:
        for fmt in self.YYYYMMDD_FORMATS:
            try:
                datetime.strptime(word, fmt)
                return True
            except ValueError:
                pass

        return False

    def is_month_name(self, word: str) -> bool:
        word = word.lower()

        return (
            word in self.MONTHS or
            any(month.startswith(word) and len(word) == 3
                for month in self.MONTHS)
        )

    def is_weekday(self, word: str) -> bool:
        word = word.lower()

        return (
            word in self.WEEKS or
            any(day.startswith(word) and len(word) == 3
                for day in self.WEEKS)
        )

    def is_time(self, word: str) -> bool:
        for fmt in self.TIME_FORMATS:
            try:
                datetime.strptime(word, fmt)
                return True
            except ValueError:
                pass

        return False
    

# ----------------------------------------
# Pattern Tokens are stored in this class
# ----------------------------------------

class PatternBasedListType:
    def __init__(self):
        self.EMAIL_REGEX = re.compile(
            r'^[A-Za-z0-9!@#$%^&*()_+]+@[A-Za-z0-9.-]+.[A-Za-z]{2,7}$'
        )

        self.CAMEL_CASE_REGEX = re.compile(
            r'^[A-Z][a-z]+(?:[A-Z][a-z]+)*$'
        )

        self.SNAKE_CASE_REGEX = re.compile(
            r'^[a-z0-9]+(?:_[a-z0-9]+)+$'
        )

        self.KEBAB_CASE_REGEX = re.compile(
            r'^[a-z0-9]+(?:-[a-z0-9]+)+$'
        )   

    def is_email_like(self, word: str) -> bool:
        return bool(self.EMAIL_REGEX.fullmatch(word))

    def is_camel_case(self, word: str) -> bool:
        return bool(self.CAMEL_CASE_REGEX.fullmatch(word))

    def is_snake_case(self, word: str) -> bool:
        return bool(self.SNAKE_CASE_REGEX.fullmatch(word))

    def is_kebab_case(self, word: str) -> bool:
        return bool(self.KEBAB_CASE_REGEX.fullmatch(word))
