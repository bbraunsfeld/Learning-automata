import json
import logging
from argparse import Namespace

__all__ = [
    "to_json",
    "read_from_json",
]

def to_json(jsonpath, argparse_dict):
    """
    This function creates a .json file as a copy of argparse_dict
    Args:
        jsonpath (str): path to the .json file
        argparse_dict (dict): dictionary containing arguments from argument parser
    """
    with open(jsonpath, "w") as fp:
        json.dump(argparse_dict, fp, sort_keys=True, indent=4)


def read_from_json(jsonpath):
    """
    This function reads args from a .json file and returns the content as a namespace dict
    Args:
        jsonpath (str): path to the .json file
    Returns:
        namespace_dict (Namespace): namespace object build from the dict stored into the given .json file.
    """
    with open(jsonpath) as handle:
        dict = json.loads(handle.read())
        namespace_dict = Namespace(**dict)
    return namespace_dict
