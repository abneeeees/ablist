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
