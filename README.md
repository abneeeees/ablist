# ablist
---

**ablist** is a `bruteforcing-tool` to generate custom wordlist out of given set of words. It has been created to help in tasks such as **Bruteforcing**,  **Password Cracking**, **or just creating a bunch of passwords out of something**

---

## Key Features
- Create a custom wordlist out of given set of words.
- Create the wordlist in a custom file of choice.
- Lets you choose Numbers of words to get in output(1-30).
- Lets you choose between 4 different modes to create the wordlist

---

## Installation

### PiP Installation
```sh
pip install ablist
```
### Updating ablist
```sh
pip install -U ablist
```

---

## Building

### Building ablist from the source.
```sh
git clone https://github.com/abneeeees/ablist.git
cd ablist
```

---

## Usage
Every uscase and flag is exlained in [Docs](https://github.com/abneeeees/ablist/blob/main/docs.md)

---

## Files Structure
- `main.py` runs the main function
- `token.py` takes command line inputs, create their tokens and store them sperately 
- `arguments.py` handles commmand line and flags
- `logic.py` contains logic of all the flags and functionality.
- `file.py` for file handling and stuff

---

## License
- This projects is licensed under [**GPLv3 license**](https://github.com/abneeeees/ablist/blob/main/LICENSE).
- Users are free to run, modify, and distribute software while ensuring that all modified versions remain free and open.