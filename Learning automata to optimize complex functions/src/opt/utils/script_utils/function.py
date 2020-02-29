def get_function(args, logging=None):
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
            logging.info("custom function will be loaded...")
        func = args.func
        func = "lambda x: " + func
        
        return func
