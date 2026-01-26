from ablist.argument import *
from datetime import datetime
import re

# Tokens are nothing but a fancy word given to the arguments given in the command line.

#  Key difference is here they will be seperated based on charactersics
# Each token will stored in their respective list type
# A list type is a list of specific types such as dates, string, integer, float, uppercase, etc ....


## Initially every argument taken is a string there it is need to be converted into their list type hence store there 
class TextBasedListType:
    def __init__(self):
        pass
    
    # examples: admin, password, user
    def lowercase_tokens(word:str) -> list:                                                             #done
        lowercase:list = None
        if word.isalpha() and word.islower():
            lowercase.append(word)

        return lowercase

        # examples: ADMIN, ROOT, USER
    def uppercase_tokens(word:str) -> list:                                                             #done
        uppercase:list = None
        if word.isalpha() and word.isupper():
            uppercase.append(word)

        return uppercase

        # examples: admin123, user2024, pass01
    def alphanumeric_tokens(word:str) -> list:                                                          #done
        alphanumeric:list = None

        if word.isalnum() and word.isalpha()==False and word.isdigit()==False:
            alphanumeric.append(word)

        return alphanumeric
    
        # examples: Admin, Password, User
    def capitalized_tokens(word:str) -> list:
        capitalize:list = None
        return capitalize

        # examples: aDmIn, pAsSwOrD
    def mixedcase_tokens(word:str) -> list:
        pass


        # examples: @@@, ###, !!!, $$
    def special_char_only_tokens(word:str) -> list:
        special_char_only:list = None
        return special_char_only


        # examples: pass@123, admin!, root#
    def contains_special_tokens(word:str) -> list:
        contains_special_tokens:list = None
        return contains_special_tokens


class NumberBasedListType:
    def __init__(self):
        pass

        # examples: 3.14, 0.99
    def int_tokens(word:str) -> list:
        integer:list = None

        try:
            word = int(word)
            if isinstance(word, int) != False:
                integer.append(word)
        except:
            exit

        return integer

        # examples: 3.14, 0.99
    def float_tokens(word:str) -> list:
        floater:list = None
        floater_regex = r'\d{1,}+\.+\d{1,}'

        if re.match(floater_regex, word):
            floater.append(word) 

        return floater

        # examples: 1, 7, 9
    def short_number_tokens(word:str) -> list:
        pass

        # examples: 123456, 987654321
    def long_number_tokens(word:str) -> list:
        long_number_tokens:list = None

        # examples: 001, 007, 0001
    def padded_number_tokens(word:str) -> list:                                                          #done
        padded_number:list = None
        padded_number_regex = r'0+[0-9]$'

        if re.match(padded_number_regex, word):
            padded_number.append(word)

        return padded_number


class DateTimeListType:
    def __init__(self):
        pass

        # examples: 12-08-2004, 01-01-2020
    def date_ddmmyyyy_tokens(word:str) -> list:                                                          #done
        date_ddmmyyyy:list = None

        formats = ['%d-%m-%Y', '%d:%m:%Y', '%d/%m/%Y', '%d\%m\%Y']
        for format in formats:
            try:
                datetime.strptime(word, format)
                date_ddmmyyyy.append(word)
            except:
                pass

        return date_ddmmyyyy

        # examples: 2004-08-12, 2020-01-01
    def date_yyyymmdd_tokens(word:str) -> list:                                                          #done
        date_yyyymmdd:list = None

        formats = ['%Y-%m-%d', '%Y:%m:%d', '%Y/%m/%d', '%Y\%m\%d']
        for format in formats:
            try:
                datetime.strptime(word, format)
                date_yyyymmdd.append(word)
            except:
                pass

        return date_yyyymmdd

        # examples: jan, january, feb
    def month_name_tokens(word:str) -> list:
        pass

        # examples: mon, monday, fri
    def weekday_tokens(word:str) -> list:
        pass

        # examples: 0930, 23:59, 0815
    def time_tokens(word:str) -> list:
        pass

        # examples: 1998, 2020, 2025
    def year_tokens(word:str) -> list:
        pass

class PatternBasedListType:
    def __init__(self):
        pass

        # examples: user@gmail.com, admin@domain.in
    def email_like_tokens(word:str) -> list:
        email_like:list = None
        email_criteria = r'[A-Za-z0-9!@#$%^&*()_+]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,7}'

        if re.fullmatch(email_criteria, word):
            email_like.append(word)

        return email_criteria

        # examples: user_123, admin99, root_user
    def username_like_tokens(word:str) -> list:
        pass

        # examples: MyPassword, UserName
    def camelCase_tokens(word:str) -> list:
        camelCase:list = None
        camelCaseCritera = r'^[a-z]+(?:[A-Z][a-z]+)*$'

        if re.match(camelCaseCritera, word):
            camelCase.append(word)

        return camelCase

        # examples: my_password, user_name_1
    def snake_case_tokens(word:str) -> list:
        snake_case:list = None
        snake_case_criteria = r'[a-z]' 

    def kebab_case_tokens(word:str) -> list:
        # examples: my-password, user-name
        pass

    # def leetspeak_tokens(word:str) -> list:
    #     # examples: p@ssw0rd, 1337, h4x0r
    #     pass

args = parser.parse_args()
arguments:str = args.words

text_based = TextBasedListType()
number_based = NumberBasedListType()
date_time_based = DateTimeListType()
pattern_based = PatternBasedListType()

for word in arguments:
    # text based
    text_based.lowercase_tokens(word)
    text_based.uppercase_tokens(word)
    text_based.capitalized_tokens(word)
    text_based.mixedcase_tokens(word)
    text_based.alphanumeric_tokens(word)
    text_based.special_char_only_tokens(word)
    text_based.contains_special_tokens(word)

    # number based
    number_based.float_tokens(word)
    number_based.short_number_tokens(word)
    number_based.long_number_tokens(word)
    number_based.padded_number_tokens(word)

    # date based
    date_time_based.date_ddmmyyyy_tokens(word)
    date_time_based.date_yyyymmdd_tokens(word)
    date_time_based.month_name_tokens(word)
    date_time_based.weekday_tokens(word)
    date_time_based.time_tokens(word)
    date_time_based.year_tokens(word)

    # pattern based
    pattern_based.email_like_tokens(word)
    pattern_based.username_like_tokens(word)
    pattern_based.camelcase_tokens(word)
    pattern_based.snake_case_tokens(word)
    pattern_based.kebab_case_tokens(word)
    pattern_based.leetspeak_tokens(word)