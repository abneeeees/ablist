from ablist.token import  TextBasedListType, NumberBasedListType, DateTimeListType, PatternBasedListType
from itertools import permutations, combinations_with_replacement

class Transformer:
    def __init__(self):
        pass

    def Uppercase(self, word:str) -> str:
        return word.upper()
    
    def Lowercase(self, word:str) -> str:
        return word.lower()
    
    def AddSuffix(self, word:str, suffix:str) -> str:
        return word + suffix
    
    def AddPrefix(self, word:str, prefix:str) -> str:
        return prefix + word
    
    def Capitalize(self, word:str) -> str:
        return word.capitalize()

    def Title(self, word:str) -> str:
        return word.title()

    def SwapCase(self, word:str) -> str:
        return word.swapcase()
    
    def JoinWords(self, word1:str, word2:str) -> str:
        return word1 + word2
    
    def JoinWith(self, word1:str, word2:str, separator:str) -> str:
        return word1 + separator + word2
    
class Generator:
    def __init__(self):
        pass

    # aVneEsh101 -> AvNeEsH101
    def ToggleCase(self, word:str) -> str:
        for x in range(len(word)):
            if x % 2 == 0:
                word = word[:x] + word[x].upper() + word[x+1:]
            else:
                word = word[:x] + word[x].lower() + word[x+1:]
        return word

    def permutations(self, words:list, limit:int) -> list:
        perm = permutations(words, limit)
        return [''.join(p) for p in perm]
    
    def combinations(self, words:list, limit:int) -> list:
        comb = combinations_with_replacement(words, limit)
        return [''.join(c) for c in comb]
    
    def LeetSpeak(self, word:str) -> str:
        LeetDict = {
            'a': '@',        'A': '@',
            'e': '3',        'E': '3',
            'i': '1',        'I': '1',
            'o': '0',        'O': '0',
            'l': '1',        'L': '1',
            's': '$',        'S': '$',
            't': '7',        'T': '7',
            'b': '8',        'B': '8',
        }

        return ''.join(LeetDict[x] if x in LeetDict else x for x in word)


class WordListModes:
    def __init__(self, final_word_list:list):
        self.final_word_list = final_word_list
        self.TextBasedListType = TextBasedListType()
        self.NumberBasedListType = NumberBasedListType()
        self.DateTimeListType = DateTimeListType()
        self.PatternBasedListType = PatternBasedListType()

    def Mode1(self):
        
        return self.final_word_list
    
    def Mode2(self):
        pass

    def Mode3(self):
        pass    

    def Mode4(self):
        pass

# Mode 1 = combinations only
# Mode 2 = combinations + permutations
# Mode 3 = combinations + case transforms
# Mode 4 = permutations + case transforms + separators + numbers + leet + prefixes/suffixes
