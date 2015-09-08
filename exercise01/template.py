# Template file for CSCI 5481 Fall 2015 Exercise 1
# Usage:
# template.py -h
import sys, os
import argparse
from subprocess import Popen, PIPE

def make_arg_parser():
    parser = argparse.ArgumentParser(prog='template.py',
                          version="%prog 1.0",
                          formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-q","--query",
                      default=argparse.SUPPRESS,
                      required=True,
                      help="Path to query fasta [required]") 
    parser.add_argument("-r","--ref",
                      default=argparse.SUPPRESS,
                      required=True,
                      help="Path to reference fasta [required]")
    parser.add_argument("-c","--command",
                      default='embalm',
                      help="Path to EMBALMER command") 
    parser.add_argument("-V","--verbose",
                      action="store_true",
                      help="Verbose output")
    return parser

# Runs embalmer in --inline mode to obtain an alignment ID of two sequences
def run_embalmer(query, ref, embalmer_cmd='embalm', verbose=False):
    """thread worker function"""

    ### YOUR CODE HERE ###
    
    return run_command(cmd, verbose=verbose)

# runs the given command and returns return value and output
def run_command(cmd, verbose=False):
    if verbose:
        print cmd
    proc = Popen(cmd,shell=True,universal_newlines=True,stdout=PIPE,stderr=PIPE)
    stdout, stderr = proc.communicate()
    return_value = proc.returncode
    return return_value, stdout, stderr

    
if __name__ == '__main__':
    parser = make_arg_parser()
    args = parser.parse_args()

    
    ### YOUR CODE HERE ###


