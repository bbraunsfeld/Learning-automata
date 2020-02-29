#!/usr/bin/env python
import os
import logging
from opt.utils import (get_function,get_parameter,ScriptError,setup_run)
from opt.utils.script_utils.parsing import build_parser
from opt.algorithms.maximum import *

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))

def main(args):
    # setup
    mode_args = setup_run(args)
    
    #get function
    func=get_function(mode_args)
    
    #get parameter 
    a, b, r, eps, delt, lamb = get_parameter(args)
    
    #single or multi
    if args.mode == "single":
        if args.model == "max":
            logging.info("searching...")
            maximum=find_maximum(func,a,b,r,eps,delt,lamb)
            logging.info("maximum found...")
            
            xs=np.arange(a,b,0.1)
            plt.figure(figsize=(15,3))
            plt.plot(xs,list(map(func,xs)))
            plt.plot(xs, np.zeros(xs.shape),color='black',linewidth=1)
            plt.plot(maximum,0,'.',marker="*",color='red')
            np.cos(x/4)*(np.cos(3*x)+np.sin(6*x))
            plt.savefig(args.path)
            
        elif args.model == "min":
            logging.info("searching...")
            minimum=find_minimum(func,a,b,r,eps,delt,lamb)
            logging.info("minimum found...")
            
            xs=np.arange(a,b,0.1)
            plt.figure(figsize=(15,3))
            plt.plot(xs,list(map(func,xs)))
            plt.plot(xs, np.zeros(xs.shape),color='black',linewidth=1)
            plt.plot(maximum,0,'.',marker="*",color='red')
            np.cos(x/4)*(np.cos(3*x)+np.sin(6*x))
            plt.savefig(args.path)
            
        else:
            raise ScriptError("Unknown mode: {}".format(args.model))
    
    
    
    
    
if __name__ == "__main__":
    parser = build_parser()
    args = parser.parse_args()

    if args.mode == "from_json":
        args = opt.utils.read_from_json(args.json_path)

    import argparse

    main(args)
