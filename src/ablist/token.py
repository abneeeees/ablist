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
        self.lowercase = []
        self.uppercase = []
        self.alphanumeric = []
        self.capitalize = []
        self.special_char_only = []

    # examples: admin, password, user
    def lowercase_tokens(self, word:str) -> list:
        if word.isalpha() and word.islower():
            self.lowercase.append(word)

        return self.lowercase

        # examples: ADMIN, ROOT, USER
    def uppercase_tokens(self, word:str) -> list:
        if word.isalpha() and word.isupper():
            self.uppercase.append(word)

        return self.uppercase

        # examples: admin123, user2024, pass01
    def alphanumeric_tokens(self, word:str) -> list:
        if word.isalnum() and word.isalpha()==False and word.isdigit()==False:
            self.alphanumeric.append(word)

        return self.alphanumeric
    
        # examples: Admin, Password, User
    def capitalized_tokens(self, word:str) -> list:
        capitalize_regex = r'^[A-Z][a-z]+$'
        
        if re.match(capitalize_regex, word):
            self.capitalize.append(word)

        return self.capitalize

        # examples: @@@, ###, !!!, $$
    def special_char_only_tokens(self, word:str) -> list:
        special_char_only_regex = r'^[^a-zA-Z0-9\t\n ]+$'

        if re.match(special_char_only_regex, word):
            self.special_char_only.append(word)

        return self.special_char_only

# ----------------------------------------
# Number Tokens are stored in this class
# ----------------------------------------

class NumberBasedListType:
    def __init__(self):
        self.integer = []
        self.floater = []
        self.short_number = []
        self.long_number = []
        self.padded_number = []

        # examples: 3.14, 0.99
    def int_tokens(self, word:str) -> list:
        integer_regex = r'^[+-]?\d+$'

        if re.match(integer_regex, word):
            self.integer.append(word)

        return self.integer

        # examples: 3.14, 0.99
    def float_tokens(self, word:str) -> list:
        floater_regex = r'^[+-]?\d+\.\d+$'

        if re.match(floater_regex, word):
            self.floater.append(word) 

        return self.floater

        # examples: 1, 7, 9
    def short_number_tokens(self, word:str) -> list:
        short_number_regex = r'^[+-]?\d{1,5}$'

        if re.match(short_number_regex, word):
            self.short_number.append(word) 

        return self.short_number

        # examples: 123456, 987654321
    def long_number_tokens(self, word:str) -> list:
        long_number_regex = r'^[+-]?\d{6,}$'

        if re.match(long_number_regex, word):
            self.long_number.append(word) 

        return self.long_number

        # examples: 001, 007, 0001
    def padded_number_tokens(self, word:str) -> list:
        padded_number_regex = r'^[0]{1,}+[0-9]{1}+$'

        if re.match(padded_number_regex, word):
            self.padded_number.append(word)

        return self.padded_number
    
# ----------------------------------------
# DateTime Tokens are stored in this class
# ----------------------------------------
 
class DateTimeListType:
    def __init__(self):
        self.date_ddmmyyyy = []
        self.date_yyyymmdd = []
        self.month_name = []
        self.weekday = []
        self.time_list = []
        self.weeks = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        self.months = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]

        # examples: 12-08-2004, 01-01-2020
    def date_ddmmyyyy_tokens(self, word:str) -> list:
        formats = [r'%d-%m-%Y', r'%d/%m/%Y', r'%d\%m\%Y']
        for format in formats:
            try:
                datetime.strptime(word, format)
                self.date_ddmmyyyy.append(word)
            except:
                pass

        return self.date_ddmmyyyy

        # examples: 2004-08-12, 2020-01-01
    def date_yyyymmdd_tokens(self, word:str) -> list:
        formats = [r'%Y-%m-%d', r'%Y/%m/%d', r'%Y\%m\%d']
        for format in formats:
            try:
                if datetime.strptime(word, format):
                    self.date_yyyymmdd.append(word)
            except:
                pass

        return self.date_yyyymmdd

        # examples: jan, january, feb
    def month_name_tokens(self, word:str) -> list:
        for month in self.months:
            if month == word.lower() or month[:3] == word.lower():
                self.month_name.append(word)
            
        return self.month_name

        # examples: mon, monday, fri
    def weekday_tokens(self, word:str) -> list:
        for week in self.weeks:
            if week == word.lower() or week[:3] == word.lower():
                self.weekday.append(word)

        return self.weekday
        
        # examples: 23:59, 0815
    def time_tokens(self, word:str) -> list:
        formats = [r'%H:%M:%S', r'%H:%M']
        for format in formats:
            try:
                if datetime.strptime(word, format):
                    self.time_list.append(word)
            except:
                pass
        
        return self.time_list

# ----------------------------------------
# Pattern Tokens are stored in this class
# ----------------------------------------

class PatternBasedListType:
    def __init__(self):
        self.email_like = []
        self.camel_case = []
        self.snake_case = []
        self.kebab_case = []    

        # examples: user@gmail.com, admin@domain.in
    def email_like_tokens(self, word:str) -> list:
        email_regex = r'[A-Za-z0-9!@#$%^&*()_+]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,7}'

        if re.fullmatch(email_regex, word):
            self.email_like.append(word)

        return self.email_like

        # examples: MyPassword, UserName
    def camel_case_tokens(self, word:str) -> list:
        camel_case_regex = r'^[A-Z][a-z]+(?:[A-Z][a-z]+)*$'

        if re.match(camel_case_regex, word):
            self.camel_case.append(word)

        return self.camel_case

        # examples: my_password, user_name_1
    def snake_case_tokens(self, word:str) -> list:
        snake_case_regex = r'(.*?)_([a-zA-Z0-9])'

        if re.match(snake_case_regex, word):
            self.snake_case.append(word)

        return self.snake_case

        # examples: my-password, user-name
    def kebab_case_tokens(self, word:str) -> list:
        kebab_case_regex = r'^[a-z]+(-[0-9a-z]+)+$'

        if re.match(kebab_case_regex, word):
            self.kebab_case.append(word)

        return self.kebab_case