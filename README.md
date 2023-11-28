# go-go-web

Command-line tool that converts .txt or .md files into .html files.

## Features

- `v1.0.3` project package uploaded to [PyPI](https://pypi.org/project/gogoweb/)
- `v0.0.5` additionally parses front matter from .md files for metadata
- `v0.0.4` additionally accepts TOML config file
- `v0.0.3` additionally parses code blocks and horizontal rules for .md files
- `v0.0.2` additionally converts .md files into .html and parses italic and bold for .md files
- `v0.0.1` converts TIL post (.txt file) into .html file, specify output location, specify stylesheet url, view app version, view app help message

## Installation

1. Download and install the latest version of [python](https://www.python.org/downloads/). Open a terminal and check that it is installed.

   Windows
   ```
   py --version
   ```

   Linux/MAC OS
   ```
   python3 --version
   ```

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

4. Check that the package was installed

   ```
   pip show gogoweb
   ```

5. Check that you have the latest version of the app.

   Windows
   ```
   py -m gogoweb.convert -v
   ```

   Linux/MAC OS
   ```
   python3 -m gogoweb.convert -v
   ```
   
   If you get `ModuleNotFoundError: No module named 'gogoweb'`:

   - Check the Location result from Step 4 to see which Python folder it installed to (Ex: Python311 is 3.11 and Python 312 is 3.12)
   - Specify the Python version it was installed to when running the Python commands:
  
   Windows
   ```
   py -3.12 -m gogoweb.convert -v
   ```

   Linux/MAC OS
   ```
   python3 -3.12 -m gogoweb.convert -v
   ```

   If this works, you probably have multiple versions of Python on your machine. Specify the Python version when running commands.

## Usage

### View App Version

   Windows
   ```
   py -m gogoweb.convert --version
   py -m gogoweb.convert -v
   ```

   Linux/MAC OS
   ```
   python3 -m gogoweb.convert -version
   python3 -m gogoweb.convert -v
   ```

### View Usage Message

   Windows
   ```
   py -m gogoweb.convert --help
   py -m gogoweb.convert -h
   ```

   Linux/MAC OS
   ```
   python3 -m gogoweb.convert -help
   python3 -m gogoweb.convert -h
   ```

### Convert .txt to .html

   Windows
   ```
   py -m gogoweb.convert <file or folder path>
   ```

   Linux/MAC OS
   ```
   python3 -m gogoweb.convert <file or folder path>
   ```

#### Example 1 (Convert one file)
`py -m gogoweb.convert ./examples/til_post1.txt`

#### Example 2 (Convert a folder of files)
`py -m gogoweb.convert ./examples`

Output(s) can be found in current workding directory's `til` folder.
</br></br>

### Specify Output Location

   Windows
   ```
   py -m gogoweb.convert <file or folder path> -o <folder path>
   ```

   Linux/MAC OS
   ```
   python3 -m gogoweb.convert <file or folder path> -o <folder path>
   ```

#### Example
`py -m gogoweb.convert ./examples/examples.txt -o ./examples`
</br></br>

### Specify Stylesheet

   Windows
   ```
   py -m gogoweb.convert <file or folder path> -s <stylesheet url>
   ```

   Linux/MAC OS
   ```
   python3 -m gogoweb.convert <file or folder path> -s <stylesheet url>
   ```

#### Example
`py -m gogoweb.convert ./examples/til_post2.txt -s https://cdnjs.cloudflare.com/ajax/libs/tufte-css/1.8.0/tufte.min.css`
</br></br>

### Specify Config File

   Windows
   ```
   py -m gogoweb.convert <file or folder path> -c <config toml file path>
   ```

   Linux/MAC OS
   ```
   python3 -m gogoweb.convert <file or folder path> -c <config toml file path>
   ```

#### Example
`py -m gogoweb.convert ./examples -c src/gogoweb/config.toml`
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
