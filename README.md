# go-go-web

Command-line tool that converts input .txt files into .html files.

## Features

- `v0.0.1` converts TIL post (.txt file) into .html file

## Installation

1. Install the latest version of python [python downloads](https://www.python.org/downloads/).

   `python --version`
   
2. Clone this repository locally
    
   `git clone https://github.com/kliu57/go-go-web.git`

   `cd go-go-web`
   
3. Check that you have the latest version of the app

   `python convert.py --version`

## Usage

### View App Version

`python convert.py --version` or `python convert.py --v`

### View Usage Message

`python convert.py --help` or `python convert.py --h`

### Convert .txt to .html

`python convert.py -i <file or folder path>`

#### Example
`python convert.py -i input/examples.txt`

Output can be found in til folder.

### Specify Output Location

`python convert.py -i <file or folder path> -o <folder path>`

#### Example
`python convert.py -i input/examples.txt -o input`

### Specify Stylesheet

`python convert.py -i <file or folder path> -s <stylesheet url>`