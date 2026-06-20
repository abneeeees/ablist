import email

from ablist.token import (
    DateTimeListType,
    NumberBasedListType,
    PatternBasedListType,
    TextBasedListType,
)

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

lowercase:list = []
uppercase:list = []
capitalized:list = []
alphanumeric:list = []
special_char_only:list = []

for word in testcase:
    # text based
    if(text_based.lowercase_tokens(word)):
        lowercase.append(word)
    if(text_based.uppercase_tokens(word)):
        uppercase.append(word)
    if(text_based.capitalized_tokens(word)):
        capitalized.append(word)
    if(text_based.alphanumeric_tokens(word)):
        alphanumeric.append(word)
    if(text_based.special_char_only_tokens(word)):
        special_char_only.append(word)

float:list = []
short_number:list = []
long_number:list = []
padded_number:list = []

for word in testcase:
    # number based
    if(number_based.float_tokens(word)):
        float.append(word)
    if(number_based.short_number_tokens(word)):
        short_number.append(word)
    if(number_based.long_number_tokens(word)):
        long_number.append(word)
    if(number_based.padded_number_tokens(word)):
        padded_number.append(word)

date_ddmmyyyy:list = []
date_yyyymmdd:list = []
month_name:list = []
weekday:list = []
time:list = []

for word in testcase:
    # date based
    if(date_time_based.is_date_ddmmyyyy(word)):
        date_ddmmyyyy.append(word)
    if(date_time_based.is_date_yyyymmdd(word)):
        date_yyyymmdd.append(word)
    if(date_time_based.is_month_name(word)):
        month_name.append(word)
    if(date_time_based.is_weekday(word)):
        weekday.append(word)
    if(date_time_based.is_time(word)):
        time.append(word)

email_like:list = []
camel_case:list = []
snake_case:list = []
kebab_case:list = []

# pattern based
for word in testcase:
    if(pattern_based.is_email_like(word)):
        email_like.append(word)
    if(pattern_based.is_camel_case(word)):
        camel_case.append(word)
    if(pattern_based.is_snake_case(word)):
        snake_case.append(word)
    if(pattern_based.is_kebab_case(word)):
        kebab_case.append(word)

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