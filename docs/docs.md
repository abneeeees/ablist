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
    - `ablist -o -oA <filename>` : for output in all format
    - `ablist -o -oP <filename>` : for output in .pdf format
    - `ablist -o -oX <filename>` : for output in .xml format
    - `ablist -o -oT <filename>` : for output in .txt format **Default**


### -m --mode
- to tell ablist what mode to use while generating the wordlist
- example `ablist -m <1-4>` or `ablist --mode <1-4>`
- Types:
    - `ablist -m 1` – **Basic Combinations**: Generates simple combinations using the given words in their original order.
    - `ablist -m 2` – **Permutation Mode**: Generates all possible permutations of the given words up to the specified limit.
    - `ablist -m 3` – **Case Variations**: Generates combinations with lowercase, uppercase, and mixed-case variations.
    - `ablist -m 4` – **God Mode**: Generates combinations using case variations, word order changes, and numeric suffixes.

---

Thanks for visiting, Contributions are welcome <3 