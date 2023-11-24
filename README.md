# go-go-web

Command-line tool that converts .txt or .md files into .html files.

## Features

- `v1.0.0` project package uploaded to [Test PyPI](https://test.pypi.org/project/gogoweb/1.0.0/)
- `v0.0.5` additionally parses front matter from .md files for metadata
- `v0.0.4` additionally accepts TOML config file
- `v0.0.3` additionally parses code blocks and horizontal rules for .md files
- `v0.0.2` additionally converts .md files into .html and parses italic and bold for .md files
- `v0.0.1` converts TIL post (.txt file) into .html file, specify output location, specify stylesheet url, view app version, view app help message

## Installation

1. Download and install the latest version of [python](https://www.python.org/downloads/). Open a terminal and check that it is installed.

   `python --version`
   
2. Open a terminal and navigate to where you want go-go-web to be stored. Clone this repository locally.
    
   `git clone https://github.com/kliu57/go-go-web.git`

   `cd go-go-web`

3. Install packages

   `pip install tomlkit`
   `pip install python-frontmatter`
   
4. Check that you have the latest version of the app.

   `py src/gogoweb/convert.py --version`

## Usage

### View App Version

`py src/gogoweb/convert.py --version` or `py src/gogoweb/convert.py -v`
</br></br>

### View Usage Message

`py src/gogoweb/convert.py --help` or `py src/gogoweb/convert.py -h`
</br></br>

### Convert .txt to .html

`py src/gogoweb/convert.py <file or folder path>`

#### Example 1 (Convert one file)
`py src/gogoweb/convert.py ./examples/til_post1.txt`

#### Example 2 (Convert a folder of files)
`py src/gogoweb/convert.py ./examples`

Output(s) can be found in til folder.
</br></br>

### Specify Output Location

`py src/gogoweb/convert.py <file or folder path> -o <folder path>`

#### Example
`py src/gogoweb/convert.py ./examples/examples.txt -o ./examples`
</br></br>

### Specify Stylesheet

`py src/gogoweb/convert.py <file or folder path> -s <stylesheet url>`

#### Example
`py src/gogoweb/convert.py ./examples/til_post2.txt -s https://cdnjs.cloudflare.com/ajax/libs/tufte-css/1.8.0/tufte.min.css`
</br></br>

### Specify Config File

`py src/gogoweb/convert.py <file or folder path> -c <config toml file path>`

#### Example
`py src/gogoweb/convert.py ./examples -c src/gogoweb/config.toml`
</br></br>

## Additional Features Available for Markdown

Input file must be a .md file that is written in proper Markdown syntax

### Front Matter Parsing

You may specify the following front matter in Markdown files and these will become the metadata of the resulting HTML file

| **Name**    | **Type** | **Default** | **Description**                                                                     |
|-------------|----------|-------------|-------------------------------------------------------------------------------------|
| description | string   | undefined   | The description of your document. Used for the page metadata and by search engines. |
| keywords    | string[] | undefined   | Keywords meta tag for the document page, for search engines.                        |
| lang        | string   | en          | The language of your document.                                                      |
| title       | string   | file name   | The text title of your document. Used for the page metadata.                        |

How to specify front matter in a Markdown file:

```
---
title: Katie's Homepage
keywords: website, coding
description: This is Katie's personal website.
---
```

## License

[License (MIT)](LICENSE.md)

## See Examples Outputs

[go-go-web examples](https://kliu57.github.io/gogoweb/)
