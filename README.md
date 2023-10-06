# go-go-web

Command-line tool that converts input .txt files into .html files.

## Features

- `v0.0.4` additionally accept TOML config file
- `v0.0.3` parses code blocks and horizontal rules for .md files
- `v0.0.2` additionally converts .md files into .html and parses italic and bold for .md files
- `v0.0.1` converts TIL post (.txt file) into .html file, specify output location, specify stylesheet url, view app version, view app help message

## Installation

1. Download and install the latest version of [python](https://www.python.org/downloads/). Open a terminal and check that it is installed.

   `python --version`
   
2. Open a terminal and navigate to where you want go-go-web to be stored. Clone this repository locally.
    
   `git clone https://github.com/kliu57/go-go-web.git`

   `cd go-go-web`

3. Install the tomlkit package
   `pip install tomlkit`
   
4. Check that you have the latest version of the app.

   `python convert.py --version`

## Usage

### View App Version

`python convert.py --version` or `python convert.py -v`
</br></br>

### View Usage Message

`python convert.py --help` or `python convert.py -h`
</br></br>

### Convert .txt to .html

`python convert.py <file or folder path>`

#### Example 1 (Convert one file)
`python convert.py ./examples/til_post1.txt`

#### Example 2 (Convert a folder of files)
`python convert.py ./examples`

Output(s) can be found in til folder.
</br>

### Specify Output Location

`python convert.py <file or folder path> -o <folder path>`

### Specify config file
`python convert.py ./examples -c config.toml`

#### Example
`python convert.py ./examples/examples.txt -o ./examples`
</br></br>

### Specify Stylesheet

`python convert.py <file or folder path> -s <stylesheet url>`

#### Example
`python convert.py ./examples/til_post2.txt -s https://cdnjs.cloudflare.com/ajax/libs/tufte-css/1.8.0/tufte.min.css`
</br></br>

## License

[License (MIT)](LICENSE.md)

## See Examples Outputs

[go-go-web examples](https://kliu57.github.io/gogoweb/)
