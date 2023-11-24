# go-go-web

Command-line tool that converts .txt or .md files into .html files.

## Features

- `v1.0.0` project package uploaded to [Test PyPI](https://test.pypi.org/project/gogoweb/)
- `v0.0.5` additionally parses front matter from .md files for metadata
- `v0.0.4` additionally accepts TOML config file
- `v0.0.3` additionally parses code blocks and horizontal rules for .md files
- `v0.0.2` additionally converts .md files into .html and parses italic and bold for .md files
- `v0.0.1` converts TIL post (.txt file) into .html file, specify output location, specify stylesheet url, view app version, view app help message

## Installation

1. Download and install the latest version of [python](https://www.python.org/downloads/). Open a terminal and check that it is installed.

   `py --version`

2. Make sure you have upgraded version of pip.

   Windows
   ```
   py -m pip install --upgrade pip
   ```

   Linux/MAC OS
   ```
   python3 -m pip install --upgrade pip
   ```

3. Install gogoweb using pip.

   Windows
   ```
   pip install gogoweb
   ```

   Linux/MAC OS
   ```
   python3 -m pip install gogoweb
   ```

4. Check the location of the installed files.

   Windows
   ```
   pip show gogoweb
   ```

   Linux/MAC OS
   ```
   python3 -m pip show gogoweb
   ```

5. Append `\gogoweb` to the location path shown. Navigate to that location using `cd`, or simply go to that location in file explorer and open a terminal there.

   ```
   # this path will be different for each user depending on the result you get from Step 4
   cd C:\Users\<your user>\AppData\Local\Programs\Python\Python312\Lib\site-packages\gogoweb
   ```

6. Check that you have the latest version of the app.

   `py convert.py -v`

## Usage

### View App Version

`py convert.py --version` or `py convert.py -v`
</br></br>

### View Usage Message

`py convert.py --help` or `py convert.py -h`
</br></br>

### Convert .txt to .html

`py convert.py <file or folder path>`

#### Example 1 (Convert one file)
`py convert.py ./examples/til_post1.txt`

#### Example 2 (Convert a folder of files)
`py convert.py ./examples`

Output(s) can be found in til folder.
</br></br>

### Specify Output Location

`py convert.py <file or folder path> -o <folder path>`

#### Example
`py convert.py ./examples/examples.txt -o ./examples`
</br></br>

### Specify Stylesheet

`py convert.py <file or folder path> -s <stylesheet url>`

#### Example
`py convert.py ./examples/til_post2.txt -s https://cdnjs.cloudflare.com/ajax/libs/tufte-css/1.8.0/tufte.min.css`
</br></br>

### Specify Config File

`py convert.py <file or folder path> -c <config toml file path>`

#### Example
`py convert.py ./examples -c src/gogoweb/config.toml`
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
