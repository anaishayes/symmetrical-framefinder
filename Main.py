#!/usr/bin/python

import sys
import glob

from multiprocessing.dummy import Pool as ThreadPool
from Directory_Setup import Directory_Setup
from Run_Transdecoder import Run_Transdecoder

"""
To execute, run in bash `./Main.py *.[FILE EXTENSION]

For example, to run on all .fasta files, do `./Main.py *.fasta`
"""

def run_commands(file):
        #print file
        ds = Directory_Setup(file)
        rt = Run_Transdecoder(ds.get_new_path())

def globbing(ext):
        """
        Locate all files ending with a file extension provided to the constructor
        and pipes each of them to the Transdecoder Program.

        """
        files = glob.glob(ext)

        pool = ThreadPool(4)

        pool.map(run_commands, files)

        pool.close()
        pool.join()

        print "Done with globbing"


if __name__ == "__main__":
        print "Running TransDecoder on all %s files in current working directory" % sys.argv[1]
        print ""
        globbing(sys.argv[1])