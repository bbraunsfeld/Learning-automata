def get_parameter(args, logging=None):
    """
    Get parameter from arguments.
    Args:
        args (argparse.Namespace): parsed arguments
        logging: logger
    Returns:
        function
    """
    if args.model == "min" or args.model == "max":
        if logging:
            logging.info("Parameter will be loaded...")
        a,b=args.interval
        r = args.subint
        eps = args.error
        delt = args.delta
        lamb = args.lambda
        
        return a,b,r,eps,delt,lamb