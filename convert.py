import sys
import re
import os

# prints the app version
def print_version():
    print("go-go-web " + open("_version.py", "r").read())

# prints the app help message
def print_help(missing_arg=None):
    print("Usage: convert.py -i <txt_filename> or <folder_containing_txt_files>  [-s <css-link>]\n")
    print("Options:")
    print("  -i, --input\t\tInput .txt file(s)\t\t" + "[string] [required]".rjust(24))
    print("  -s, --stylesheet\tOptional CSS Link \t\t" + "[string] [default: \"\"]".rjust(24))
    print("  -h, --help\t\tPrint this help message\t\t" + "[boolean]".rjust(24))
    print("  -v, --version\t\tPrint version number\t\t" + "[boolean]".rjust(24))

    if missing_arg:
        print("\nMissing required argument: " + missing_arg)

# only triggered when we call this .py file and not during imports
if __name__ == '__main__':

    # gets list of all arguments user typed in command line after calling this .py file with "python convert.py"
    # Ex: python convert.py argument1 argument2
    # gets: ['argument1', 'argument2']
    args = sys.argv[1:]

    # check if user specified any arguments
    if args:
        option_name = args[0]

        if option_name == "-v" or option_name == "--version":
            print_version()
        elif option_name == "-h" or option_name == "--help":
            print_help()
        elif option_name == "-i" or option_name == "--input":
            
            file_names = args[1:]

            if file_names:
                
                # loop through each file given by user
                for path in file_names:

                    # check if the path given is for existing file, existing folder, or non-existent
                    if os.path.isfile(path):
                        # split the root and file ext
                        path_tup = os.path.splitext(path)

                        # extract the file name and extension
                        file_name = path_tup[0]
                        file_ext = path_tup[1]
                        
                        if file_ext == ".txt":
                            print("not ready")
                        else:
                            print("Error: file extension should be .txt")

                    elif os.path.isdir(path): 
                        print("It is a folder")  
                    else:  
                        print("Error: file cannot be found")


            else:
                print_help("<txt_filename> or <folder_containing_txt_files>")
                


        elif option_name == "-s" or option_name == "--stylesheet":
            print("this functionality is not ready")
        else:
            print_help()

    
    else:
        print_help()

        


    
    
