import numpy as np
import logging


def get_function(args, logging=logging):
    """
    Get function from arguments.
    Args:
        args (argparse.Namespace): parsed arguments
        logging: logger
    Returns:
        function
    """
    if args.function == "custom":
        if logging:
            logging.info("Custom function will be loaded ...")
            
        func = lambda x: np.cos(x/4)*(np.cos(3*x)+np.sin(6*x))
        
        return func
