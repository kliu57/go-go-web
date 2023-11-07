"""Module contains unit tests for src/convert.py"""
import os
import pytest
from src import convert as c


@pytest.mark.parametrize('cleanup_output', [['til/test.html']], indirect=True)
@pytest.mark.usefixtures('cleanup_output')
def test_main_default_output(tmpdir, helpers):
    """Tests convert.py main function with output to default location"""
    # Pass command line arguments to main() to mimic the following command line program call:
    # python src/convert <tmp_input_file>
    arguments = c.parse_args(
        [helpers.new_file(tmpdir, "test.txt", pytest.simple_txt_contents)])
    # Run main function
    c.main(arguments)
    # Compare actual output file contents to expected
    assert helpers.file_contents(
        'til/test.html') == pytest.simple_html_from_txt


def test_main_custom_output(tmpdir, helpers):
    """Tests convert.py main function specifying output location"""
    # Pass command line arguments to main() to mimic the following command line program call:
    # python src/convert -o <tmp_output_dir> <tmp_input_file>
    arguments = c.parse_args(
        ["-o", str(tmpdir), helpers.new_file(tmpdir, "test.txt", pytest.simple_txt_contents)])
    # Run main function
    c.main(arguments)
    # Compare actual output file contents to expected
    output_path = tmpdir.join('test.html')
    assert helpers.file_contents(output_path) == pytest.simple_html_from_txt


def test_main_folder_of_files(tmpdir, helpers):
    """Tests convert.py main function for folder of files, specifying output location"""
    # Create folder of files
    input_folder = tmpdir.mkdir("input")
    helpers.new_file(input_folder, "test.txt", pytest.simple_txt_contents)
    helpers.new_file(input_folder, "markdown.md", pytest.simple_md_contents)

    # Pass command line arguments to main() to mimic the following command line program call:
    # python src/convert -o <tmp_output_dir> <tmp_input_folder>
    arguments = c.parse_args(["-o", str(tmpdir), str(input_folder)])
    # Run main function
    c.main(arguments)
    # Compare actual output files contents to expected
    output_path = tmpdir.join('test.html')
    assert helpers.file_contents(output_path) == pytest.simple_html_from_txt
    output_path = tmpdir.join('markdown.html')
    assert helpers.file_contents(output_path) == pytest.simple_html_from_md


def test_main_stylesheet(tmpdir, helpers):
    """Tests convert.py main function specifying stylesheet, specifying output location"""
    # Pass command line arguments to main() to mimic the following command line program call:
    # python src/convert -o <tmp_output_dir> -s <stylesheet url> <tmp_input_file>
    arguments = c.parse_args(["-o", str(tmpdir), "-s", "https://cdnjs.cloudflare.com/ajax/libs/tufte-css/1.8.0/tufte.min.css",
                              helpers.new_file(tmpdir, "test.txt", pytest.simple_txt_contents)])
    # Run main function
    c.main(arguments)
    # Compare actual output file contents to expected
    output_path = tmpdir.join('test.html')
    assert helpers.file_contents(
        output_path) == pytest.simple_html_with_stylesheet


def test_main_config(tmpdir, helpers):
    """Tests convert.py main function specifying config file"""
    # Create config file
    contents = 'output = "' + str(tmpdir).replace(os.sep, '/') + '"\n' \
        'stylesheet = "https://cdnjs.cloudflare.com/ajax/libs/tufte-css/1.8.0/tufte.min.css"'
    config_file = helpers.new_file(tmpdir, "config.toml", contents)

    # Pass command line arguments to main() to mimic the following command line program call:
    # python src/convert -c <config toml file path> <tmp_input_file>
    arguments = c.parse_args(
        ["-c", config_file, helpers.new_file(tmpdir, "test.txt", pytest.simple_txt_contents)])
    # Run main function
    c.main(arguments)
    # Compare actual output file contents to expected
    output_path = tmpdir.join('test.html')
    assert helpers.file_contents(
        output_path) == pytest.simple_html_with_stylesheet
