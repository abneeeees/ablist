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
    COMMON_NUMBERS = [
        "1", "12", "123", "1234", "007", "69", "420", "777", "0011", "67", "00",
    ]

    COMMON_SEPARATORS = [
        "_", "-", ".", "@", "$", "#", "&", "+", "!", "*", "~", "^", "=",
    ]

    def __init__(self):
        pass

    def ToggleCase(self, word: str) -> str:
        result = []
        for i, ch in enumerate(word):
            result.append(ch.upper() if i % 2 == 0 else ch.lower())
        return "".join(result)

    def permutations(self, words: list, limit: int) -> list:
        return ["".join(p) for p in permutations(words, limit)]

    def combinations(self, words: list, limit: int) -> list:
        return ["".join(c) for c in combinations_with_replacement(words, limit)]

    def LeetSpeak(self, word: str) -> str:
        leet_dict = {
            "a": "@", "A": "@",
            "e": "3", "E": "3",
            "i": "1", "I": "1",
            "o": "0", "O": "0",
            "l": "1", "L": "1",
            "s": "$", "S": "$",
            "t": "7", "T": "7",
            "b": "8", "B": "8",
        }
        return "".join(leet_dict.get(x, x) for x in word)

    def AddCommonNumbers(self, word: str) -> list:
        return [self.AddSuffix(word, num) for num in self.COMMON_NUMBERS]

    def AddCommonSymbols(self, word1: str, word2: str) -> list:
        return [self.JoinWith(word1, word2, s) for s in self.COMMON_SEPARATORS]


class WordListModes(Generator):
    def __init__(
        self,
        final_word_list: list,
        string_tokens: list,
        integer_tokens: list,
        date_time_tokens: list,
        pattern_based_tokens: list,
        limit: int = 30,
    ):
        super().__init__()
        self.final_word_list = final_word_list
        self.StringTokens = string_tokens
        self.IntegerTokens = integer_tokens
        self.DateTimeTokens = date_time_tokens
        self.PatternBasedTokens = pattern_based_tokens
        self.limit = limit
        self.all_words = list(set(
            string_tokens
            + integer_tokens
            + date_time_tokens
            + pattern_based_tokens
        ))

    def FastMode(self) -> list:
        result = set(self.all_words)
        for w1 in self.all_words:
            for w2 in self.all_words:
                result.add(self.JoinWords(w1, w2))
        return list(result)[:self.limit]

    def SmartMode(self) -> list:
        result = set(self.FastMode())
        if len(self.all_words) >= 2:
            for p in self.permutations(self.all_words, 2):
                result.add(p)
            for c in self.combinations(self.all_words, 2):
                result.add(c)
        return list(result)[:self.limit]

    def AggressiveMode(self) -> list:
        result = set(self.SmartMode())
        for w in self.all_words:
            result.add(self.Uppercase(w))
            result.add(self.Lowercase(w))
            result.add(self.Capitalize(w))
            result.add(self.Title(w))
            result.add(self.SwapCase(w))
            result.add(self.ToggleCase(w))
            result.add(self.LeetSpeak(w))
            result.update(self.AddCommonNumbers(w))
        for w1 in self.all_words:
            for w2 in self.all_words:
                if w1 != w2:
                    result.update(self.AddCommonSymbols(w1, w2))
        return list(result)[:self.limit]

    def GodMode(self) -> list:
        result = set(self.AggressiveMode())
        for w in self.all_words:
            for num in self.COMMON_NUMBERS:
                result.add(self.AddSuffix(w, num))
                result.add(self.AddPrefix(w, num))
            leet = self.LeetSpeak(w)
            result.add(self.Uppercase(leet))
            result.add(self.Lowercase(leet))
            result.add(self.ToggleCase(leet))
            for nw in self.AddCommonNumbers(w):
                result.add(self.Uppercase(nw))
                result.add(self.Lowercase(nw))
                result.add(self.ToggleCase(nw))
                result.add(self.LeetSpeak(nw))
        if len(self.all_words) >= 2:
            for w1 in self.all_words:
                for w2 in self.all_words:
                    if w1 != w2:
                        for s in self.AddCommonSymbols(w1, w2):
                            result.add(self.Uppercase(s))
                            result.add(self.Lowercase(s))
                            result.add(self.ToggleCase(s))
                            result.add(self.LeetSpeak(s))
        if len(self.all_words) >= 3:
            for p in self.permutations(self.all_words, 3):
                result.add(p)
            for c in self.combinations(self.all_words, 3):
                result.add(c)
        return list(result)[:self.limit]
