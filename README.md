# go-go-web

Command-line tool that converts input .txt files into .html files.

## Features

- `v0.0.1` converts TIL post (.txt file) into .html file, specify output location, specify stylesheet url, view app version, view app help message

## Installation

1. Download and install the latest version of [python](https://www.python.org/downloads/). Open a terminal and check that it is installed.

   `python --version`
   
2. Open a terminal and navigate to where you want go-go-web to be stored. Clone this repository locally.
    
   `git clone https://github.com/kliu57/go-go-web.git`

   `cd go-go-web`
   
3. Check that you have the latest version of the app.

   `python convert.py --version`

## Usage

### View App Version

`python convert.py --version` or `python convert.py --v`
</br></br>

### View Usage Message

`python convert.py --help` or `python convert.py --h`
</br></br>

### Convert .txt to .html

`python convert.py -i <file or folder path>`

#### Example 1 (Convert one file)
`python convert.py -i ./examples/examples.txt`

#### Example 2 (Convert a folder of files)
`python convert.py -i ./examples`

Output(s) can be found in til folder.
</br></br>

### Specify Output Location

`python convert.py -i <file or folder path> -o <folder path>`

#### Example
`python convert.py -i ./examples/examples.txt -o ./examples`
</br></br>

### Specify Stylesheet

`python convert.py -i <file or folder path> -s <stylesheet url>`

#### Example
`python convert.py -i ./examples/examples.txt -s https://cdnjs.cloudflare.com/ajax/libs/tufte-css/1.8.0/tufte.min.css`
</br></br>

## License

[License (MIT)](LICENSE.md)