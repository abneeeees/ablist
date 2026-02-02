from ablist.token import *

testcase = [
    # ======================
    # basic text
    # ======================
    'Admin', 'admin', 'ADMIN',
    'User', 'user',

    # ======================
    # mixed / case variants
    # ======================
    'Admin123', 'admin123', 'AdMiN',
    'UsEr', 'uSeR',

    # ======================
    # numeric only
    # ======================
    '1', '42', '1111',
    '0001.01', '2024', '0101.11',
    '0011', '0000',
    '2121021021', '142411',
    '0000000.0000000',
    '11111111111',
    '-1', '+42',
    '0000000001',
    '0000002',
    '0000000200000',
    '2000000001',
    '121212-121212-1212',
    '3.14159', '1e10',

    # ======================
    # alphanumeric patterns
    # ======================
    '123admin', 'admin123', 'user2024',
    'a1b2c3', 'abc007',
    '007bond', 'bond007',

    # ======================
    # special characters only
    # ======================
    '@@@', '!!!', '###', '$$',
    '%^&*', '(){}[]',

    # ======================
    # contains special characters
    # ======================
    'admin@@@', 'Admin@@@',
    'pass@123', 'root!',
    'hello.world', 'foo#bar',
    'name$', 'test%',

    # ======================
    # separators / styles
    # ======================
    'admin_user',        # snake_case
    'admin-user',        # kebab-case
    'AdminUser',         # camelCase
    'admin.user',        # dot.case
    'admin__user',       # double underscore
    'admin--user',       # double dash

    # ======================
    # leetspeak
    # ======================
    'p@ssw0rd', '4dm1n.0',
    'l33t', 'h4x0r',
    '1337', 'n00b',

    # ======================
    # repeated characters
    # ======================
    'aaa', '!!!!', '1111',
    'aaaaaa', 'zzzzzz',
    '_____', '-----',

    # ======================
    # dates / time
    # ======================
    '01-01-2020', '01/01/2020', '2020-01-01',
    '12-08-2004',
    '0930', '23:59:01', '23:59:10','2003','2023'
    '00:00', '23:59',
    '2020/13/01',  # invalid date but common input

    # ======================
    # words related to time
    # ======================
    'jan', 'JANUARY', 'march',
    'mon', 'monday',
    'fri', 'sunday',
    'december',

    # ======================
    # email / username like
    # ======================
    'admin@gmail.com',
    'abneeeees@proton.me',
    'apple@mail.com',
    'user_123',
    'user.name+tag@gmail.com',
    'USER@EXAMPLE.COM',

    # ======================
    # keyboard patterns
    # ======================
    'qwerty', 'asdf', 'zxcv',
    'qazwsx', '1q2w3e',
    'wasd',

    # ======================
    # palindrome
    # ======================
    'abba', '1221', 'level',
    'racecar', 'madam',
    'neveroddoreven',

    # ======================
    # whitespace & invisible
    # ======================
    '',                # empty
    ' ',               # space
    '   ',             # multiple spaces
    '\t',              # tab
    '\n',              # newline
    ' admin ',         # padded
    'user\n',

    # ======================
    # unicode / non-ascii
    # ======================
    'café', 'naïve',
    'résumé',
    'mañana',
    'こんにちは',
    '用户',
    'админ',

    # ======================
    # tricky edge cases
    # ======================
    'a'*100,            # very long word
    '1'*100,            # very long number
    'admin\0user',      # null byte
    '../admin',
    '<script>alert(1)</script>',
    "' OR 1=1 --",
]

text_based = TextBasedListType()
number_based = NumberBasedListType()
date_time_based = DateTimeListType()
pattern_based = PatternBasedListType()

for word in testcase:
    # text based
    lowercase = text_based.lowercase_tokens(word)
    uppercase = text_based.uppercase_tokens(word)
    capitalized = text_based.capitalized_tokens(word)
    alphanumeric = text_based.alphanumeric_tokens(word)
    special_char_only = text_based.special_char_only_tokens(word)

    # number based
    float = number_based.float_tokens(word)
    short_number = number_based.short_number_tokens(word)
    long_number = number_based.long_number_tokens(word)
    padded_number = number_based.padded_number_tokens(word)

    # date based
    date_ddmmyyyy = date_time_based.date_ddmmyyyy_tokens(word)
    date_yyyymmdd = date_time_based.date_yyyymmdd_tokens(word)
    month_name = date_time_based.month_name_tokens(word)
    weekday = date_time_based.weekday_tokens(word)
    time = date_time_based.time_tokens(word)

    # pattern based
    email_like = pattern_based.email_like_tokens(word)
    camel_case = pattern_based.camel_case_tokens(word)
    snake_case = pattern_based.snake_case_tokens(word)
    kebab_case = pattern_based.kebab_case_tokens(word)

print("\nlowercase\t : ", lowercase)
print("\nuppercase\t : ", uppercase)
print("\ncapitalized\t : ", capitalized)
print("\nalphanumeric\t : ", alphanumeric)
print("\nspecial_char_only\t : ", special_char_only)
print("\nfloat\t : ", float)
print("\nshort_number\t : ", short_number)
print("\nlong_number\t : ", long_number)
print("\npadded_number\t : ", padded_number)
print("\ndate_ddmmyyyy\t : ", date_ddmmyyyy)
print("\ndate_yyyymmdd\t : ", date_yyyymmdd)
print("\nmonth_name\t : ", month_name)
print("\nweekday\t : ", weekday)
print("\ntime\t : ", time)
print("\nemail_like\t : ", email_like)
print("\ncamel_case\t : ", camel_case)
print("\nsnake_case\t : ", snake_case)
print("\nkebab_case\t : ", kebab_case)