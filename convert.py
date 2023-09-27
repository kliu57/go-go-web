import pathlib
import re
import sys
import os
import argparse
import shutil

DEFAULT_OUTPUT = "til"

def print_version():
    """Function printing app version."""
    with open("_version.py", "r", encoding="utf-8") as file:
        print("go-go-web " + file.read())

def remake_til_folder():
    """Function removes existing default output folder and recreates it."""
    # delete default output folder
    if os.path.exists(DEFAULT_OUTPUT):
        try:
            shutil.rmtree(DEFAULT_OUTPUT)
            print(DEFAULT_OUTPUT + " folder deleted")
        except OSError as e:
            print(e)
            sys.exit()

    # create default output folder
    os.makedirs(DEFAULT_OUTPUT)
    print(DEFAULT_OUTPUT + " folder created")

def convert_to_html(path, output_folder, css_url):
    """Function converting one .txt or .md TIL post to html"""

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
    
    # check if input file has a valid extension
    if file_ext in (".txt", ".md"):
        title = os.path.basename(file_name)
        output_fname = title + ".html"

        # use the input file name as the output file name
        output_fpath = output_folder + output_fname

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

                if file_ext == ".md" :
                    # Replace *italic* and _italic_ with <em>italic</em>
                    line = re.sub(r'([^*])\*([^*]+)\*', r'\1<em>\2</em>', line)
                    line = re.sub(r'[^_]_([^_]+)_', r'<em>\1</em>', line)

                    # Replace **bold** and __bold__ with <strong>bold</strong>
                    line = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', line)
                    line = re.sub(r'__([^_]+)__', r'<strong>\1</strong>', line)
    
                if line:
                    # check if line is empty string
                    # write the line to the output file wrapped in the paragraph tag
                    output_file.write(f'<p>{line}</p>\n')
                else:
                    # write an empty line to the output file
                    output_file.write(f'\n')

            # write closing tags
            output_file.write(f'</body>\n')
            output_file.write(f'</html>')
        
        print(path.replace(os.sep, '/') + " converted to " + output_fpath + " successfully!")
    else:
        print("Error: " + path.replace(os.sep, '/') + " was not converted. File extension should be .txt")

# only triggered when we call this .py file and not during imports
if __name__ == '__main__':

    formatter = lambda prog: argparse.HelpFormatter(prog, max_help_position=52)
    parser = argparse.ArgumentParser(formatter_class=formatter, description="convert txt or md file or folder of files to html")
    parser.add_argument("-v", "--version", action="store_true", help="display the app version")
    parser.add_argument("-o", "--output", type=pathlib.Path, help="specify output directory")
    parser.add_argument("-s", "--stylesheet", type=str, help="specify url for CSS stylesheet")
    parser.add_argument("fname", nargs='?', type=pathlib.Path, help="the input file or folder path")
    args = parser.parse_args()

    if args.version:
        print_version()
    else:
        if args.fname:
            # default output folder path and css url
            output_folder = DEFAULT_OUTPUT
            css_url = None

            # remove and recreate default output folder
            remake_til_folder()

            # get input file path from user input
            path = str(args.fname)

            if args.stylesheet:
                # get css url from user input
                css_url = args.stylesheet
                
            if args.output:
                # get output folder path from user input
                output_folder = str(args.output)

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