#!/usr/bin/env python
import os
import logging
from opt.utils import (get_function,get_parameter,ScriptError,setup_run,picture_results)
from opt.utils.script_utils.parsing import build_parser
from opt.algorithms.maximum import *

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))

def main(args):
    # setup
    mode_args = setup_run(args)
    logging.info("Steup...")
    #get function
    func=get_function(mode_args)
    print (func)
    
    #get parameter 
    a, b, r, eps, delt, lamb = get_parameter(mode_args)

    print (a, b, r, eps, delt, lamb)
    
    #single or multi
    if args.mode == "single":
        if args.model == "max":
            logging.info("Searching for maximum...")
            maximum=find_maximum(func,a,b,r,eps,delt,lamb)
            logging.info("Maximum found at x = %s" %(maximum))

            print ("Maximum at", maximum)
            picture_result(func,a,b,maximum,args)
            
  
        elif args.model == "min":
            logging.info("Searching for minimum...")
            minimum=find_minimum(func,a,b,r,eps,delt,lamb)
            logging.info("Minimum found at x = %s" %(minimum))
            
            print ("Minimum at x = ", maximum)
            picture_result(func,a,b,maximum,args)
            
        else:
            raise ScriptError("Unknown mode: {}".format(args.model))
    
    
    
    
    
if __name__ == "__main__":
    parser = build_parser()
    args = parser.parse_args()

    if args.mode == "from_json":
        args = read_from_json(args.json_path)

    import argparse

    main(args)
