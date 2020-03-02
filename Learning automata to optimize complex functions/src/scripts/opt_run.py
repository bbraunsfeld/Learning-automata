#!/usr/bin/env python
import os
import logging
from opt.utils import (get_function,get_parameter,ScriptError,setup_run,picture_result,picture_results)
from opt.utils.script_utils.parsing import build_parser
from opt.algorithms.optimizer import *

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))

def main(args):
    # setup
    mode_args = setup_run(args)
    logging.info("Setup...")
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
            maximum=find_optimum(args.model, func,a,b,r,eps,delt,lamb)
            logging.info("Maximum found at x = %s" %(maximum))

            print ("Maximum at", maximum)
            picture_result(args.model,func,a,b,maximum,args)
            
  
        elif args.model == "min":
            logging.info("Searching for minimum...")
            minimum=find_optimum(args.model,func,a,b,r,eps,delt,lamb)
            logging.info("Minimum found at x = %s" %(minimum))
            
            print ("Minimum at x = ", minimum)
            picture_result(args.model,func,a,b,minimum,args)
            
        elif args.model == "minmax":
            logging.info("Searching for minimum...")
            optim = ["min","max"]
            minimum=find_optimum(optim[0],func,a,b,r,eps,delt,lamb)
            logging.info("Minimum found at x = %s" %(minimum))
            
            logging.info("Searching for maximum...")
            maximum=find_optimum(optim[1], func,a,b,r,eps,delt,lamb)
            logging.info("Maximum found at x = %s" %(maximum))

            print ("Minimum at x = ", minimum)
            print ("Maximum at x =", maximum)
            picture_result(optim[0],func,a,b,minimum,args)
            picture_result(optim[1],func,a,b,maximum,args)
            picture_results(func,a,b,minimum,maximum,args)
            
        else:
            raise ScriptError("Unknown mode: {}".format(args.model))
    
    
if __name__ == "__main__":
    parser = build_parser()
    args = parser.parse_args()

    if args.mode == "from_json":
        args = read_from_json(args.json_path)

    import argparse

    main(args)
