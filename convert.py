import pathlib
import re
import sys
import os
import argparse
import shutil
from tomlkit.toml_file import TOMLFile

DEFAULT_OUTPUT = "til"

def print_version():
    """Function printing app version."""
    with open("_version.py", "r", encoding="utf-8") as file:
        print("go-go-web " + file.read())

def remake_til_folder(out=DEFAULT_OUTPUT):
    """Function removes existing default output folder and recreates it."""
    # delete default output folder
    if os.path.exists(out):
        try:
            shutil.rmtree(out)
            print(out + " folder deleted")
        except OSError as e:
            print(e)
            sys.exit()

    # create default output folder
    os.makedirs(out)
    print(out + " folder created")

def load_config_file(config_file):
    """Load and parse the TOML configuration file."""
    try:
        toml = TOMLFile(config_file)
        config_data= toml.read()
        return config_data
    except Exception as e:
        print("Error loading or parsing the config file:", e)
        sys.exit(1)

def convert_to_html(path, output_folder, css_url):
    # at slash at end of folder path if it is not there
    if output_folder[-1] != "/":
        output_folder += "/"

    # check if output folder is an existing folder
    if not os.path.isdir(output_folder):
        print("Error: output folder " + output_folder + " is not an existing folder")
        return

    # split the root and file ext
    path_tup = os.path.splitext(path)

    # extract the file name and ext
    file_name = path_tup[0]
    file_ext = path_tup[1]
    if file_ext == ".md":
        markdown_to_html(path,file_name, output_folder, css_url)
    elif file_ext == ".txt":
        text_to_html(path,file_name, output_folder, css_url)
    else:
        print("Error: " + path.replace(os.sep, '/') + " was not converted. File extension should be .md or .txt")



def markdown_to_html(path,file_name, output_folder, css_url):
    title = os.path.basename(file_name)
    output_fname = title + ".html"

    # use the input file name as the output file name
    output_fpath = output_folder + output_fname

    # flag which signifies if text is inside a code block
    in_code_block = False

    # open input and output files
    with open(path, mode='r', encoding="utf-8") as input_file, open(output_fpath, mode='w', encoding="utf-8") as output_file:

        # write html head
        output_file.write('<!doctype html>\n')
        output_file.write('<html lang="en">\n')
        output_file.write('<head>\n')
        output_file.write('\t<meta charset="utf-8">\n')
        output_file.write(f'\t<title>{title}</title>\n')
        output_file.write('\t<meta name="viewport" content="width=device-width, initial-scale=1">\n')
        if css_url:
            output_file.write(f'\t<link rel="stylesheet" href="{css_url}">\n')
        output_file.write('</head>\n')

        # write html body
        output_file.write('<body>\n')

        # read each line in input file
        for line in input_file:

            # trim the line of whitespace and newline character
            line = line.strip()

            
                # If text is not inside a code block, must parse styled text
            if not in_code_block:
                # Look for beginning of code block (```)
                result_tup = re.subn(r'^[ ]*```.*$', r'<pre>', line)
                line = result_tup[0]
                num_found = result_tup[1]

                if num_found > 0:
                    in_code_block = True
                else:
                    # Replace *italic* and _italic_ with <em>italic</em>
                    line = re.sub(r'([^*])\*([^*]+)\*', r'\1<em>\2</em>', line)
                    line = re.sub(r'[^_]_([^_]+)_', r'<em>\1</em>', line)

                    # Replace **bold** and __bold__ with <strong>bold</strong>
                    line = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', line)
                    line = re.sub(r'__([^_]+)__', r'<strong>\1</strong>', line)

                    # Replace --- with <hr />
                    line = re.sub(r'^[ ]*---[-]*[ ]*$', r'<hr />', line)

                    # Replace `text` with <code>text</code>
                    line = re.sub(r'`(.*)`', r'<code>\1</code>', line)

                    # Line is not in code block, so wrap line in paragraph tag
                    line = "<p>" + line + "</p>"
            else:
                # Look for end of code block (```)
                result_tup = re.subn(r'^[ ]*```[`]*[ ]*$', r'</pre>', line)
                line = result_tup[0]
                num_found = result_tup[1]

                if num_found > 0:
                    in_code_block = False
            if line:
                # write the line to the output file
                output_file.write(f'{line}\n')
            else:
                # write an empty line to the output file
                output_file.write(f'\n')

        # write closing tags
        output_file.write(f'</body>\n')
        output_file.write(f'</html>')
    
    print(path.replace(os.sep, '/') + " converted to " + output_fpath + " successfully!")


def text_to_html(path,file_name, output_folder, css_url):
    # check if input file has a valid extension
    title = os.path.basename(file_name)
    output_fname = title + ".html"

    # use the input file name as the output file name
    output_fpath = output_folder + output_fname

    # flag which signifies if text is inside a code block
    in_code_block = False

    # open input and output files
    with open(path, mode='r', encoding="utf-8") as input_file, open(output_fpath, mode='w', encoding="utf-8") as output_file:

        # write html head
        output_file.write('<!doctype html>\n')
        output_file.write('<html lang="en">\n')
        output_file.write('<head>\n')
        output_file.write('\t<meta charset="utf-8">\n')
        output_file.write(f'\t<title>{title}</title>\n')
        output_file.write('\t<meta name="viewport" content="width=device-width, initial-scale=1">\n')
        if css_url:
            output_file.write(f'\t<link rel="stylesheet" href="{css_url}">\n')
        output_file.write('</head>\n')

        # write html body
        output_file.write('<body>\n')

        # read each line in input file
        for line in input_file:

            # trim the line of whitespace and newline character
            line = line.strip()


            if line:
                # write the line to the output file
                output_file.write(f'{line}\n')
            else:
                # write an empty line to the output file
                output_file.write(f'\n')

        # write closing tags
        output_file.write(f'</body>\n')
        output_file.write(f'</html>')
    
    print(path.replace(os.sep, '/') + " converted to " + output_fpath + " successfully!")


# only triggered when we call this .py file and not during imports
if __name__ == '__main__':

    formatter = lambda prog: argparse.HelpFormatter(prog, max_help_position=52)
    parser = argparse.ArgumentParser(formatter_class=formatter, description="convert txt or md file or folder of files to html")
    parser.add_argument("-v", "--version", action="store_true", help="display the app version")
    parser.add_argument("-o", "--output", type=pathlib.Path, help="specify output directory")
    parser.add_argument("-s", "--stylesheet", type=str, help="specify url for CSS stylesheet")
    parser.add_argument("fname", nargs='?', type=pathlib.Path, help="the input file or folder path")
    parser.add_argument("-c", "--config", type=str, help="specify config file")
    args = parser.parse_args()

    if args.version:
        print_version()
    else:
            if args.fname:
                # default output folder path and css url
                output_folder = DEFAULT_OUTPUT
                css_url = None


                # get input file path from user input
                path = str(args.fname)

                if args.config:
                    # Load and parse the TOML configuration file
                    config_data = load_config_file(args.config)

                    # Extract configuration options from the parsed data
                    if "output" in config_data:
                        output_folder = str(config_data["output"])
                        remake_til_folder(output_folder)
                    if "stylesheet" in config_data:
                        css_url = str(config_data["stylesheet"])
                else:
                    if args.stylesheet:
                        # get css url from user input
                        css_url = args.stylesheet
                        
                    if args.output:
                        # get output folder path from user input
                        output_folder = str(args.output)
                        remake_til_folder(output_folder)
                    else:
                        # remove and recreate default output folder
                        remake_til_folder()

                # check if the input file or folder path EXISTS
                if os.path.isfile(path):
                    # convert file to html
                    convert_to_html(path, output_folder, css_url)
                elif os.path.isdir(path): 
                    # get each item in the folder
                    for item in os.listdir(path):
                        # get the file path
                        file_path = os.path.join(path, item)

                        # check if item is a file
                        if os.path.isfile(file_path):
                            # convert file to html
                            convert_to_html(file_path, output_folder, css_url)
                else:
                    print(f"Error: File {path} does not exist\n")
                    parser.print_help()
            else:
                print(f"Error: no file or folder name specified")
                parser.print_help()