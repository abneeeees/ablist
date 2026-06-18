from ablist.argument import parser
from ablist.engine import WordListModes
from ablist.file import FileHandler
from ablist.token import (
    DateTimeListType,
    NumberBasedListType,
    PatternBasedListType,
    TextBasedListType,
)


def create_tokens(words: list) -> dict:
    tokens = {
        "StringTokens": [],
        "IntegerTokens": [],
        "DateTimeTokens": [],
        "PatternBasedTokens": [],
    }

    text_based = TextBasedListType()
    number_based = NumberBasedListType()
    pattern_based = PatternBasedListType()
    date_time_based = DateTimeListType()

    for word in words:
        # Text-based tokens
        if text_based.lowercase_tokens(word):
            tokens["StringTokens"].append(word)

        if text_based.uppercase_tokens(word):
            tokens["StringTokens"].append(word)

        if text_based.alphanumeric_tokens(word):
            tokens["StringTokens"].append(word)

        if text_based.capitalized_tokens(word):
            tokens["StringTokens"].append(word)

        if text_based.special_char_only_tokens(word):
            tokens["StringTokens"].append(word)

        # Number-based tokens
        if number_based.int_tokens(word):
            tokens["IntegerTokens"].append(word)

        if number_based.float_tokens(word):
            tokens["IntegerTokens"].append(word)

        if number_based.short_number_tokens(word):
            tokens["IntegerTokens"].append(word)

        if number_based.long_number_tokens(word):
            tokens["IntegerTokens"].append(word)

        if number_based.padded_number_tokens(word):
            tokens["IntegerTokens"].append(word)

        # DateTime-based tokens
        if date_time_based.is_date_ddmmyyyy(word):
            tokens["DateTimeTokens"].append(word)

        if date_time_based.is_date_yyyymmdd(word):
            tokens["DateTimeTokens"].append(word)

        if date_time_based.is_month_name(word):
            tokens["DateTimeTokens"].append(word)

        if date_time_based.is_weekday(word):
            tokens["DateTimeTokens"].append(word)

        if date_time_based.is_time(word):
            tokens["DateTimeTokens"].append(word)

        # Pattern-based tokens
        if pattern_based.is_email_like(word):
            tokens["PatternBasedTokens"].append(word)

        if pattern_based.is_camel_case(word):
            tokens["PatternBasedTokens"].append(word)

        if pattern_based.is_snake_case(word):
            tokens["PatternBasedTokens"].append(word)

        if pattern_based.is_kebab_case(word):
            tokens["PatternBasedTokens"].append(word)

    return tokens


def engine(tokens: dict, final_word_list: list) -> list:

    return final_word_list


def filehandling(filename_and_filetype: list, final_word_list: list) -> None:
    if len(filename_and_filetype) == 1:
        filename_and_filetype.append("output.txt")

    if len(filename_and_filetype) > 2:
        print("Invalid number of arguments for output option.")
        exit(1)

    if len(filename_and_filetype) == 0:
        print("No output option provided. Defaulting to terminal output.")
        filename_and_filetype = ["D", None]

    if filename_and_filetype[0] not in ["B", "D", "T"]:
        print("Invalid output type. Please choose 'B', 'D', or 'T'.")
        exit(1)

    if filename_and_filetype[0] in ["B", "T"] and filename_and_filetype[1] is None:
        print("Please provide a filename for the output.")
        exit(1)

    if filename_and_filetype[0] == "D" and filename_and_filetype[1] is not None:
        print("Filename is not required for terminal output. Ignoring the filename.")
        filename_and_filetype[1] = None

    mode = filename_and_filetype[0]
    filename = filename_and_filetype[1]

    obj = FileHandler(filename, final_word_list)
    if mode == "T":
        obj.save_as_txt()
    elif mode == "D":
        for word in final_word_list:
            print(word)
    elif mode == "B":
        obj.save_as_txt()
        for word in final_word_list:
            print(word)
    else:
        print("Invalid output type. Please choose 'T', 'D', or 'B'.")


def main():
    args = parser.parse_args()
    FinalWordList: list = []

    tokens = create_tokens(args.words)
    final_output = engine(tokens, FinalWordList)
    filehandling(args.output, final_output)


if __name__ == "__main__":
    main()
