## Contributing - Raising an Issue

1. Issues > New issue

2. Give lots of details in the description and include screenshots wherever possible. If you would like to work on the issue, please mention this.

3. Please wait to be assigned to the issue before starting work on it.

## Contributing - Fixing an Existing Issue

1. Comment in the issue to ask to be assigned.

2. Download and install the latest version of [python](https://www.python.org/downloads/). Open a terminal and check that it is installed.

   `python --version`

3. Once you have been assigned, follow [these steps](https://docs.github.com/en/get-started/quickstart/contributing-to-projects) for forking and cloning the repo and creating a branch.

4. Install packages

   `pip install tomlkit`
   `pip install python-frontmatter`
   `pip install pycodestyle`
   `pip install --upgrade autopep8`
   `pip install pylint`

5. Make your code additions or changes.

6. Prior to committing your changes to your branch, run autopep8 to format the code.

   `python -m autopep8 --in-place --recursive --exclude="*.md,_version.py,_output_dir.py" .`

   Alternatively, install the autopep8 VS Code extension, and then run it on a file by:

   `Right Click File Contents > Format Document With... > autopep8`

7. Run Pylint to evaluate the code. Please ensure the evaluation rating is at or above 9.0/10.

   `python -m pylint ./*.py --ignore-patterns="_version.py,_output_dir.py"`

   If you use VS Code, you can install the Pylint VSCode extension, and linting will automatically run when a Python file is opened. Read [here](https://code.visualstudio.com/docs/python/linting#_run-linting) for more details. This can help with identifying and locating issues, but you must run the above command line code to reveal the evaluation score.

8. Commit your changes to your branch and submit a pull request. See [steps in this guide](https://docs.github.com/en/get-started/quickstart/contributing-to-projects). In the pull request description, please link it to the issue by writing Closes #11, where 11 is replaced with your issue number. Please also include screenshots to show results of testing.