from itertools import combinations_with_replacement, permutations


class Transformer:
    def __init__(self):
        pass

    def Uppercase(self, word: str) -> str:
        return word.upper()

    def Lowercase(self, word: str) -> str:
        return word.lower()

    def AddSuffix(self, word: str, suffix: str | int) -> str:
        return word + str(suffix)

    def AddPrefix(self, word: str, prefix: str | int) -> str:
        return str(prefix) + word

    def Capitalize(self, word: str) -> str:
        return word.capitalize()

    def Title(self, word: str) -> str:
        return word.title()

    def SwapCase(self, word: str) -> str:
        return word.swapcase()

    def JoinWords(self, word1: str | int, word2: str | int) -> str:
        return str(word1) + str(word2)

    def JoinWith(self, word1: str | int, word2: str | int, separator: str | int) -> str:
        return str(word1) + str(separator) + str(word2)


class Generator(Transformer):
    def __init__(self):
        pass

    # aVneEsh101 -> AvNeEsH101
    def ToggleCase(self, word: str) -> str:
        for x in range(len(word)):
            if x % 2 == 0:
                word = word[:x] + word[x].upper() + word[x + 1 :]
            else:
                word = word[:x] + word[x].lower() + word[x + 1 :]
        return word

    def permutations(self, words: list, limit: int) -> list:
        perm = permutations(words, limit)
        return ["".join(p) for p in perm]

    def combinations(self, words: list, limit: int) -> list:
        comb = combinations_with_replacement(words, limit)
        return ["".join(c) for c in comb]

    def LeetSpeak(self, word: str) -> str:
        LeetDict = {
            "a": "@",
            "A": "@",
            "e": "3",
            "E": "3",
            "i": "1",
            "I": "1",
            "o": "0",
            "O": "0",
            "l": "1",
            "L": "1",
            "s": "$",
            "S": "$",
            "t": "7",
            "T": "7",
            "b": "8",
            "B": "8",
        }

        return "".join(LeetDict[x] if x in LeetDict else x for x in word)

    def AddCommonNumers(self, word: str) -> str:
        COMMON_NUMBERS: list = [
            "1",
            "12",
            "123",
            "1234",
            "007",
            "69",
            "420",
            "777",
            "0011",
            "67",
            "00",
        ]

        for num in COMMON_NUMBERS:
            word = self.AddSuffix(word, num)
        return word

    def AddCommonSymbols(self, word1: str, word2: str) -> list:
        COMMON_SEPARATORS = [
            "_", "-", ".", "@", "$", "#", "&", "+", "!", "*", "~", "^", "=",
        ]

        for symbol in COMMON_SEPARATORS:
            return [''.join(self.JoinWith(word1=word1, word2=word2, separator=symbol))]


class WordListModes(Generator):
    def __init__(
        self,
        final_word_list: list,
        string_tokens: list,
        integer_tokens: list,
        date_time_tokens: list,
        pattern_based_tokens: list,
    ):
        self.final_word_list = final_word_list
        self.StringTokens = string_tokens
        self.IntegerTokens = integer_tokens
        self.DateTimeTokens = date_time_tokens
        self.PatternBasedTokens = pattern_based_tokens

    def FastMode(self):
        pass
        
    def SmartMode(self):
        pass

    def AggressiveMode(self):
        pass

    def GodMode(self):
        pass


# Fast Mode: Original words and basic combinations.
# Smart Mode: Adds permutations and common word order changes.
# Aggressive Mode: Adds case variations, capitalization patterns, and text mutations.
# God Mode: Applies all permutations, case mutations, leetspeak, dates, numbers, prefixes, suffixes, separators,
