import argparse

# All the flags documented and explained in https://github.com/abneeeees/ablist/blob/main/docs/docs.md
# This file contains the declaration of all the flags to be used in the command line

# Argument parser configuration
# This parser defines all supported command-line flags and their behavior.
parser = argparse.ArgumentParser(
    prog="ablist",
    #   usage=None,            #confued between wether to show this in use or not
    usage=argparse.SUPPRESS,
    prefix_chars="-",
    description="""

                                            ▄▄
                                       █▄    ██          █▄
                                       ██    ██ ▀▀      ▄██▄
                                 ▄▀▀█▄ ████▄ ██ ██ ▄██▀█ ██
                                 ▄█▀██ ██ ██ ██ ██ ▀███▄ ██
                                ▄▀█▄██▄████▀▄██▄███▄▄██▀▄██

    ablist is a command-line bruteforcing tool used to generate custom wordlists from a given set of words.
    ------------------------------------------------------------------------------------------------------
        Key Features:
        * Generate custom wordlists from a given set of words
        * Save output to a file format of your choice
        * Control the number of words generated in the output (1-30)
        * Choose between four different generation modes
        * Simple and lightweight CLI usage""",
    formatter_class=argparse.RawTextHelpFormatter,
    epilog="Created by : https://github.com/abneeeees",
)

# handles -w and --words flag
parser.add_argument(
    "-w",
    "--words",
    nargs="+",
    type=str,
    required=True,
    metavar="<word1> <word2> <word3> ...",
    help="Write words to be used in generating the wordlist",
)

# handles -l and --limits flag
parser.add_argument(
    "-l",
    "--limits",
    type=int,
    choices=range(1, 31),
    default=30,
    required=False,
    metavar="<1-30>",
    help="Set a limit to number of words to generated in the output wordlist",
)

# handles -o and --output flag
parser.add_argument(
    "-o",
    "--output",
    nargs="*",
    metavar=("TYPE", "FILENAME"),
    default=["D", None],
    help="""
        Output options:
          -o B filename    Output to both terminal and file
          -o D             Output only to terminal (default)
          -o T filename    Output only to a text file
""",
)

# handles -m and --mode flag
parser.add_argument(
    "-m",
    "--mode",
    choices=range(1, 5),
    type=int,
    required=False,
    metavar="<1-4>",
    help=(
        """To tell ablist what mode to use while generating the wordlist
        -m 1 - Fast Mode: Original words and basic combinations.
        -m 2 - Smart Mode: Adds permutations and common word order changes.
        -m 3 - Aggressive Mode: Adds case variations, capitalization patterns, and text mutations.
        -m 4 - God Mode: Applies all permutations, case mutations, leetspeak, dates, numbers, prefixes, suffixes, separators, and pattern-based transformations."""
    ),
)
