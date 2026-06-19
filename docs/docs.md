## Welcome to **ablist** Usage

---

ablist is a command-line **bruteforcing tool** used to generate **custom wordlists** from a given set of words.  
It is designed to assist in tasks such as **bruteforcing**, **password cracking**, or simply **generating multiple password combinations** based on custom inputs.

---

## Key Features
- Generate custom wordlists from a given set of words
- Save output to a file format of your choice
- Control the number of words generated in the output *(1–30)*
- Choose between **four different generation modes**
- Simple and lightweight CLI usage

---

## Command-Line Options

### -h --help 
- to know about any flag and its usage 
- example `ablist -h` or `ablist --help`

### -w --words
- to write words to be used in generating the wordlist
- example `ablist -w <word1> <word2>` or `ablist --words <word1> <word2>`

### -l --limit
- to set a limit to number of words to generated in the output wordlist
- example `ablist -l <number>` or `ablist --limit <number>`
- default value: 10
- Max value: 30

### -o --output
- to get an output file of the wordlist
- example `ablist -o <filetype> <filename>` or `ablist --output <filetype> <filename>`
- Available filetypes: `.pdf` `.xml` `.txt`
- Types: 
    - `ablist -o D           ` : for output in all format
    - `ablist -o T <filename>` : for output in .txt format **Default**
    - `ablist -o B <filename>` : for both terminal and file output


### -m --mode
- to tell ablist what mode to use while generating the wordlist
- example `ablist -m <1-4>` or `ablist --mode <1-4>`
- Types:
    - `ablist -m 1` – **Fast Mode**: Fast Mode: Original words and basic combinations.
    - `ablist -m 2` – **Smart Mode**: Smart Mode: Adds permutations and common word order changes.
    - `ablist -m 3` – **Aggressive Mode**: Aggressive Mode: Adds case variations, capitalization patterns, and text mutations.
    - `ablist -m 4` – **God Mode**: God Mode: Applies all permutations, case mutations, leetspeak, dates, numbers, prefixes, suffixes, separators, and pattern-based transformations.

---

Thanks for visiting, Contributions are welcome <3 