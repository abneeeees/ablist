# ablist

**ablist** is a command-line **bruteforcing tool** used to generate **custom wordlists** from a given set of words.  
It is designed to assist in tasks such as **bruteforcing**, **password cracking**, or simply **generating multiple password combinations** based on custom inputs.

---

## Key Features
- Generate custom wordlists from a given set of words
- Save output to a file format of your choice
- Control the number of words generated in the output *(1–30)*
- Choose between **four different generation modes**
- Simple and lightweight CLI usage

---

## File Structure
```sh
├── docs
│   └── docs.md             # User guide, usage instructions, and feature explanations for ablist.
├── LICENSE
├── pyproject.toml          # Project configuration file for packaging, dependencies, and build settings.
├── README.md
├── requirements.txt
├── src
│   ├── ablist
│   │   ├── argument.py             # Handles CLI argument parsing, validation, and flag processing.
│   │   ├── core
│   │   │   ├── engine.py           #Main controller that decides which generation mode and operations to run.
│   │   │   └── pipeline.py             # Executes word generation workflow (mutate → combine → decorate → return results).
│   │   ├── decorators
│   │   │   ├── prefix.py           #Adds prefixes.
│   │   │   ├── suffix.py           # Adds suffixes
│   │   │   └── wrapper.py          # Wraps words with surrounding characters or symbols (e.g., {word}, @word@).
│   │   ├── file.py             # Handles saving generated wordlists into different output formats (txt, pdf, xml, etc.).
│   │   ├── __init__.py
│   │   ├── __main__.py
│   │   ├── mutator.py          # Applies transformations to individual words (case changes, numeric variations, symbol mutations).
│   │   ├── structure
│   │   │   ├── combine.py          # Creates basic word combinations by joining words in order.
│   │   │   ├── pairwise.py             # Generates combinations between word pairs.
│   │   │   ├── permutation.py          # Generates all possible word order permutations.
│   │   │   └── subset.py           # Generates subsets of input words based on size or limit constraints.
│   │   └── token.py            # Classifies input words into categories (text types, numbers, patterns, dates, etc.).
├── tests
    └── test_tokens.py
```

---

## Installation

### uv Installation
- [uv](https://docs.astral.sh/uv/getting-started/installation/#__tabbed_1_2) is an extremely fast Python package and project manager, written in Rust. 

##### For macOS and Linux
```sh
curl -LsSf https://astral.sh/uv/install.sh | sh
```

##### Windows
```sh
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```
---

## Running

```sh
git clone https://github.com/abneeeees/ablist.git
cd ablist
uv sync
uv run ablist
```
---

## Building

```sh
git clone https://github.com/abneeeees/ablist.git
cd ablist
uv sync
uv build
pip install dist/ablist-0.1.0-py3-none-any.whl
```

---

## Developing
```sh
pip install -e .
```

## Usage
Every usecase and flag is exlained in [Docs](https://github.com/abneeeees/ablist/blob/main/docs/docs.md)

---

## Files Structure
- `main.py` runs the main function
- `token.py` takes command line inputs, create their tokens and store them sperately 
- `arguments.py` handles commmand line and flags
- `logic.py` contains logic of all the flags and functionality.
- `file.py` for file handling

---

## Contributing
- Contributions are welcome 💚

---

## License
- This projects is licensed under [**GPLv3 license**](https://github.com/abneeeees/ablist/blob/main/LICENSE).
- Users are free to run, modify, and distribute software while ensuring that all modified versions remain free and open.
