from ablist.argument import *
from datetime import datetime
import re

# Tokens are nothing but a fancy word given to the arguments given in the command line.

#  Key difference is here they will be seperated based on charactersics
# Each token will stored in their respective list type
# A list type is a list of specific types such as dates, string, integer, float, uppercase, etc ....

## Initially every argument taken is a string there it is need to be converted into their list type hence store there 

# TextBased Tokens are stored in this class 
class TextBasedListType:

    # examples: admin, password, user
    def lowercase_tokens(word:str) -> list:
        lowercase:list = None
        if word.isalpha() and word.islower():
            lowercase.append(word)

        return lowercase

        # examples: ADMIN, ROOT, USER
    def uppercase_tokens(word:str) -> list:
        uppercase:list = None
        if word.isalpha() and word.isupper():
            uppercase.append(word)

        return uppercase

        # examples: admin123, user2024, pass01
    def alphanumeric_tokens(word:str) -> list:
        alphanumeric:list = None

        if word.isalnum() and word.isalpha()==False and word.isdigit()==False:
            alphanumeric.append(word)

        return alphanumeric
    
        # examples: Admin, Password, User
    def capitalized_tokens(word:str) -> list:
        capitalize:list = None
        capitalize_regex = r'^[A-Z][a-z]+$'
        
        if re.match(capitalize_regex, word):
            capitalize.append(word)

        return capitalize

        # examples: aDmIn, pAsSwOrD
    def mixedcase_tokens(word:str) -> list:
        pass


        # examples: @@@, ###, !!!, $$
    def special_char_only_tokens(word:str) -> list:
        special_char_only:list = None
        special_char_only_regex = r'^[^a-zA-Z0-9\t\n ]+$'

        if re.match(special_char_only_regex, word):
            special_char_only.append(word)

        return special_char_only

# Number Tokens are stored in this class 
class NumberBasedListType:
        # examples: 3.14, 0.99
    def int_tokens(word:str) -> list:
        integer:list = None
        integer_regex = r'^[+-]*[\d]+$'

        if re.match(integer_regex, word):
                integer.append(word)

        return integer

        # examples: 3.14, 0.99
    def float_tokens(word:str) -> list:
        floater:list = None
        floater_regex = r'^[+-]*[\d.]+$'

        if re.match(floater_regex, word):
            floater.append(word) 

        return floater

        # examples: 1, 7, 9
    def short_number_tokens(word:str) -> list:
        short_number:list = None
        short_number_regex = r'^[+-]*[\d.]{1,5}+$'

        if re.match(short_number_regex, word):
            short_number.append(word) 

        return short_number

        # examples: 123456, 987654321
    def long_number_tokens(word:str) -> list:
        long_number:list = None
        long_number_regex = r'^[+-]*[\d.]{6,}+$'

        if re.match(long_number_regex, word):
            long_number.append(word) 

        return long_number

        # examples: 001, 007, 0001
    def padded_number_tokens(word:str) -> list:
        padded_number:list = None
        padded_number_regex = r'0+[0-9]$'

        if re.match(padded_number_regex, word):
            padded_number.append(word)

        return padded_number

# DateTime Tokens are stored in this class 
class DateTimeListType:
    def __init__(self):
        self.weeks = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        self.months = ["january", "february", "march", "april", "may", "june", "july", "august", "september", " october", "november", "december"]

        # examples: 12-08-2004, 01-01-2020
    def date_ddmmyyyy_tokens(word:str) -> list:
        date_ddmmyyyy:list = None

        formats = ['%d-%m-%Y', '%d/%m/%Y', '%d\%m\%Y']
        for format in formats:
            try:
                datetime.strptime(word, format)
                date_ddmmyyyy.append(word)
            except:
                pass

        return date_ddmmyyyy

        # examples: 2004-08-12, 2020-01-01
    def date_yyyymmdd_tokens(word:str) -> list:
        date_yyyymmdd:list = None

        formats = ['%Y-%m-%d', '%Y/%m/%d', '%Y\%m\%d']
        for format in formats:
            try:
                if datetime.strptime(word, format):
                    date_yyyymmdd.append(word)
            except:
                pass

        return date_yyyymmdd

        # examples: jan, january, feb
    def month_name_tokens(self, word:str) -> list:
        month_name:list = None

        for month in self.months:
            if month == word.lower() or month[:3] == word.lower():
                month_name.append(word)
            
        return month_name

        # examples: mon, monday, fri
    def weekday_tokens(self, word:str) -> list:
        weekday:list = None

        for week in self.weeks:
            if week == word.lower() or week[:3] == word.lower():
                weekday.append(word)

            return weekday
        
        # examples: 0930, 23:59, 0815
    def time_tokens(word:str) -> list:
        time_tokens:list = None

        formats = ['%H:%M:%S', '%H:%M']
        for format in formats:
            try:
                if datetime.strptime(word, format):
                    time_tokens.append(word)
            except:
                pass
        
        return time_tokens

        # examples: 1998, 2020, 2025
    def year_tokens(word:str) -> list:
        pass

# Pattern Tokens are stored in this class 
class PatternBasedListType:
        # examples: user@gmail.com, admin@domain.in
    def email_like_tokens(word:str) -> list:
        email_like:list = None
        email_regex = r'[A-Za-z0-9!@#$%^&*()_+]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,7}'

        if re.fullmatch(email_regex, word):
            email_like.append(word)

        return email_like

        # examples: MyPassword, UserName
    def camel_case_tokens(word:str) -> list:
        camel_case:list = None
        camel_case_regex = r'^[a-zA-Z]+([A-Z][a-z]+)+$'

        if re.match(camel_case_regex, word):
            camel_case.append(word)

        return camel_case

        # examples: my_password, user_name_1
    def snake_case_tokens(word:str) -> list:
        snake_case:list = None
        snake_case_regex = r'^[a-z]+(_[0-9a-z]+)+$'

        if re.match(snake_case_regex, word):
            snake_case.append(word)

        return word

        # examples: my-password, user-name
    def kebab_case_tokens(word:str) -> list:
        kebab_case:list = None
        kebab_case_regex = r'^[a-z]+(-[0-9a-z]+)+$'

        if re.match(kebab_case_regex, word):
            kebab_case.append(word)

        return kebab_case

args = parser.parse_args()
arguments:str = args.words

text_based = TextBasedListType()
number_based = NumberBasedListType()
date_time_based = DateTimeListType()
pattern_based = PatternBasedListType()

for word in arguments:
    # text based
    print(text_based.lowercase_tokens(word))
    print(text_based.uppercase_tokens(word))
    print(text_based.capitalized_tokens(word))
    print(text_based.mixedcase_tokens(word))
    print(text_based.alphanumeric_tokens(word))
    print(text_based.special_char_only_tokens(word))

    # number based
    print(number_based.float_tokens(word))
    print(number_based.short_number_tokens(word))
    print(number_based.long_number_tokens(word))
    print(number_based.padded_number_tokens(word))

    # date based
    print(date_time_based.date_ddmmyyyy_tokens(word))
    print(date_time_based.date_yyyymmdd_tokens(word))
    print(date_time_based.month_name_tokens(word))
    print(date_time_based.weekday_tokens(word))
    print(date_time_based.time_tokens(word))
    print(date_time_based.year_tokens(word))

    # pattern based
    print(pattern_based.email_like_tokens(word))
    print(pattern_based.camel_case_tokens(word))
    print(pattern_based.snake_case_tokens(word))
    print(pattern_based.kebab_case_tokens(word))