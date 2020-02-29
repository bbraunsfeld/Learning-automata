import os
import logging
from shutil import rmtree
import opt

__all__ = ["setup_run"]


def setup_run(args):
    argparse_dict = vars(args)
    jsonpath = os.path.join(args.path, "args.json")
    if args.mode == "single":

        # build dir
        if args.overwrite and os.path.exists(args.path):
            logging.info("existing file will be overwritten...")
            rmtree(args.path)
        if not os.path.exists(args.path):
            os.makedirs(args.path)

        # store single arguments
        opt.utils.opt_utils.to_json(jsonpath, argparse_dict)

        single_args = args
    else:
        # check if path is valid
        if not os.path.exists(args.path):
            raise opt.utils.ScriptError(
                "The selected dir does not exist " "at {}!".format(args.path)
            )

        # load  arguments
        single_args = opt.utils.opt_utils.read_from_json(jsonpath)
        
    if args.mode == "multi":

        # build dir
        if args.overwrite and os.path.exists(args.path):
            logging.info("existing file will be overwritten...")
            rmtree(args.path)
        if not os.path.exists(args.path):
            os.makedirs(args.path)

        # store multi arguments
        opt.utils.opt_utils.to_json(jsonpath, argparse_dict)

        multi_args = args
    else:
        # check if path is valid
        if not os.path.exists(args.path):
            raise opt.utils.ScriptError(
                "The selected dir does not exist " "at {}!".format(args.path)
            )

        # load arguments
        multi_args = opt.utils.opt_utils.read_from_json(jsonpath)
        
    if (getsizeof(single_args)==0):
        mode_args = multi_args
    else:
        mode_args = single_args

    return mode_args
