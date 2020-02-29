import argparse

class StoreDictKeyPair(argparse.Action):
    """
    From https://stackoverflow.com/a/42355279
    """

    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        self._nargs = nargs
        super(StoreDictKeyPair, self).__init__(
            option_strings, dest, nargs=nargs, **kwargs
        )

    def __call__(self, parser, namespace, values, option_string=None):
        my_dict = {}
        for kv in values:
            k, v = kv.split("=")
            my_dict[k] = v
        setattr(namespace, self.dest, my_dict)

def get_mode_parsers():
    mode_parser = argparse.ArgumentParser(add_help=False)

    # mode parsers

    # json parser
    json_parser = argparse.ArgumentParser(add_help=False, parents=[mode_parser])
    json_parser.add_argument(
        "json_path",
        type=str,
        help="Path to argument file. (default: %(default)s)",
        default=None,
    )
    
    
    single_parser = argparse.ArgumentParser(add_help=False, parents=[mode_parser])
    single_parser.add_argument("path", help="Path to directory")
    single_parser.add_argument(
        "--overwrite", 
        help="Remove previous saving directory.",
        action="store_true"
    )
    
    
    multi_parser = argparse.ArgumentParser(add_help=False, parents=[mode_parser])
    multi_parser.add_argument("path", help="Path to directory")
    multi_parser.add_argument(
        "--overwrite", 
        help="Remove previous saving directory.",
        action="store_true"
    )
        
    return mode_parser, json_parser, single_parser, multi_parser
    
def get_model_parsers():
    # model parsers
    model_parser = argparse.ArgumentParser(add_help=False)
    min_parser = argparse.ArgumentParser(add_help=False, parents=[model_parser])    
    min_parser.add_argument(
        "--interval",
        help="Range that is examined",
        type=int,
        nargs=2,
        default=[None, None],
    )
    
    min_parser.add_argument(
        "--subint",
        help="Number of sub-intervals divided (default: %(default)s)",
        type=int,
        default=5,
    )
    
    min_parser.add_argument(
        "--error",
        help="Giving the error band (default: %(default)s) according to the required precision or the required computation cost",
        type=float,
        default=0.05,
    )
    
    min_parser.add_argument(
        "--delta",
        help="Threshold of action probabilities (0 < D < 1/r) (default: %(default)s)",
        type=float,
        default=0.01,
    )
    
    min_parser.add_argument(
        "--lambda",
        help="Speed of convergence (0 < k < 1) (default: %(default)s)",
        type=float,
        default=0.4,
    )
    
    max_parser = argparse.ArgumentParser(add_help=False, parents=[model_parser])    
    max_parser.add_argument(
        "--interval",
        help="Range that is examined",
        type=int,
        nargs=2,
        default=[None, None],
    )
    
    max_parser.add_argument(
        "--subint",
        help="Number of sub-intervals divided (default: %(default)s)",
        type=int,
        default=5,
    )
    
    max_parser.add_argument(
        "--error",
        help="Giving the error band (default: %(default)s) according to the required precision or the required computation cost",
        type=float,
        default=0.05,
    )
    
    max_parser.add_argument(
        "--delta",
        help="Threshold of action probabilities (0 < D < 1/r) (default: %(default)s)",
        type=float,
        default=0.01,
    )
    
    max_parser.add_argument(
        "--lamda",
        help="Speed of convergence (0 < k < 1) (default: %(default)s)",
        type=float,
        default=0.4,
    )
    
    
    return model_parser, min_parser, max_parser 

def get_function_parsers():
    # functions parsers
    function_parser = argparse.ArgumentParser(add_help=False)
    function_parser.add_argument(
        "--func",
        help="Function that is used (example:  /'np.sin(x) + np.cos(0.5*x)/')",
        type=str,
        default=None,
    )
    
    return function_parser
        
        
            
def build_parser():
    #get parser
    mode_parser, json_parser, single_parser, multi_parser = get_mode_parsers()
    model_parser, min_parser, max_parser = get_model_parsers()
    function_parser = get_function_parsers()
    
    #subparser
    #mode
    mode_subparsers = mode_parser.add_subparsers(dest="mode", help="Main arguments")
    single_subparser = mode_subparsers.add_parser("single", help="Single help")
    multi_subparser = mode_subparsers.add_parser("multi", help="Multi help")
    
    json_subparser = mode_subparsers.add_parser(
        "from_json", help="load from json help", parents=[json_parser]
    )
    
    # single mode
    single_subparsers = single_subparser.add_subparsers(
        dest="model", help="Model-specific arguments"
    )
    # model
    min_subparser = single_subparsers.add_parser("min", help="Min help")
    max_subparser = single_subparsers.add_parser("max", help="Max help")
    
    # min
    min_subparsers = min_subparser.add_subparsers(
        dest="function", help="function specific arguments"
    )
    min_subparsers.add_parser(
        "custom",
        help="Function help",
        parents=[single_parser, min_parser, function_parser],
    )
    
    # max
    max_subparsers = max_subparser.add_subparsers(
        dest="function", help="function specific arguments"
    )
    max_subparsers.add_parser(
        "custom",
        help="Function help",
        parents=[single_parser, max_parser, function_parser],
    )
    
    return mode_parser


if __name__ == "__main__":
    parser = build_parser()
    args = parser.parse_args() 
