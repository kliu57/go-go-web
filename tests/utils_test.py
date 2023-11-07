"""Module contains unit tests for src/utils.py"""
import os
import pytest
from src import utils as ut


@pytest.mark.usefixtures('cleanup_cwd')
def test_format_path_display(tmp_path):
    """Tests format_path_display function"""

    # create sub directories and files
    sub_dir = tmp_path / "sub"
    sub_dir.mkdir()
    descendant = sub_dir / "desc"   # descendant of sub_dir
    file = descendant / "file.txt"  # descendant of sub_dir
    other_file = tmp_path / "other.txt"  # not descendant of sub_dir

    # Change CWD to sub_dir
    os.chdir(sub_dir)

    # Given an absolute path which is a child path of CWD,
    # should return relative path with forward slashes
    assert ut.format_path_display(file) == "desc/file.txt"

    # Given an relative path which is a child path of CWD,
    # should return relative path with forward slashes
    assert ut.format_path_display(os.path.relpath(file)) == "desc/file.txt"

    # Given an absolute path which is not a child path of CWD,
    # should return absolute path with forward slashes
    assert ut.format_path_display(other_file) == str(
        other_file).replace(os.sep, '/')

    # Given an relative path which is not a child path of CWD,
    # should return absolute path with forward slashes
    assert ut.format_path_display(os.path.relpath(
        other_file)) == str(other_file).replace(os.sep, '/')


def test_get_root_dir():
    """Tests get_root_dir function"""
    # Test that the root directory is the CWD, since tests should be executed while CWD is the root
    assert ut.get_root_dir() == os.path.abspath(os.getcwd())


def test_get_par_dir(tmp_path):
    """Tests get_par_dir function"""
    # Given sub directory, result from get_par_dir should be the parent directory
    assert ut.get_par_dir(tmp_path / "sub") == str(tmp_path)
