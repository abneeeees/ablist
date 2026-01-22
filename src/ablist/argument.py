import argparse

# All the flags documented and explained in https://github.com/abneeeees/ablist/blob/main/docs/docs.md
# This file contains the declaration of all the flags to be used in the command line

# Argument parser configuration
# This parser defines all supported command-line flags and their behavior.
parser = argparse.ArgumentParser(
    prog='ablist',
#   usage=None,            #confued between wether to show this in use or not
    usage=argparse.SUPPRESS,
    prefix_chars='-',
    description="""
    ablist is a command-line bruteforcing tool used to generate custom wordlists from a given set of words.
    ------------------------------------------------------------------------------------------------------
        Key Features:
        * Generate custom wordlists from a given set of words
        * Save output to a file format of your choice
        * Control the number of words generated in the output (1-30)
        * Choose between four different generation modes
        * Simple and lightweight CLI usage""",
    formatter_class=argparse.RawTextHelpFormatter,
    epilog="Created by : https://github.com/abneeeees"
)

# handles -w and --words flag
parser.add_argument(
    '-w', '--words',
    nargs='+',
    type=str,
    required=True,
    metavar='<word1> <word2> <word3> ...',
    help='Write words to be used in generating the wordlist'
)

# handles -l and --limits flag
parser.add_argument(
    '-l', '--limits',
    type=int,
    choices=range(1,30),
    default=10,
    required=False,
    metavar='<1-30>',
    help='Set a limit to number of words to generated in the output wordlist'
)

# handles -o and --output flag
parser.add_argument(
    '-o', '--output',
    choices=['A', 'D', 'P', 'X', 'T'],
    type=str,
    default='-oD',
    required=False,
    metavar='<filetype> <filename>',
    help=('''Get an output file of the wordlist
        -o -oA <filename> : for output in all format
        -o -oD <filename> : for output directlty on the terminal screen
        -o -oP <filename> : for output in .pdf format
        -o -oX <filename> : for output in .xml format
        -o -oT <filename> : for output in .txt format Default'''
    )
)

# handles -m and --mode flag
parser.add_argument(
    '-m', '--mode',
    choices=range(1,5),
    type=int,
    required=False,
    metavar='<1-4>',
    help=('''To tell ablist what mode to use while generating the wordlist
        -m 1 - Basic Combinations: Generates simple combinations using the given words in their original order.
        -m 2 - Permutation Mode: Generates all possible permutations of the given words up to the specified limit.
        -m 3 - Case Variations: Generates combinations with lowercase, uppercase, and mixed-case variations.
        -m 4 - God Mode: Generates combinations using case variations, word order changes, and numeric suffixes.'''
    )
)