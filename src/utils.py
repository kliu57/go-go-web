"""Module providing general utility functions."""
import os


def format_path_display(path):
    """Format path for display"""
    # Format path to relative path if in CWD or to absolute path if not
    path = os.path.relpath(path)
    if ".." in path:
        path = os.path.abspath(path)
    # returns the path formatted with forward slashes
    path = path.replace(os.sep, '/')
    return path


def get_root_dir():
    """Function returns the parent directory of this file"""
    return os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))


def get_par_dir(path):
    """"Function returns parent directory of given path"""
    return os.path.abspath(os.path.join(path, os.pardir))
