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

def runFileTransdecoder(file):
        """
        Pipe file to Transdecoder program and sets up output and input directory 
        before processing it. 
        """
        ds = Directory_Setup(file)
        rt = Run_Transdecoder(ds.get_new_path())

def parallelizeFileProcessing(ext):
        """
        Locate all files ending with a file extension provided to the constructor
        and pipes each of them to the Transdecoder Program in parallel.

        """
        files = glob.glob(ext)

        pool = ThreadPool(16)

        pool.map(runFileTransdecoder, files)

        pool.close()
        pool.join()

        print "Completed parallel processing of files"


if __name__ == "__main__":
        print "Running TransDecoder on all %s files in current working directory" % sys.argv[1]
        print ""
        parallelizeFileProcessing(sys.argv[1])
