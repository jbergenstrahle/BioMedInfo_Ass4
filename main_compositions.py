import unittest
import argparse
import functions_for_composition as dic
import numpy as np
import itertools
import math
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument("inFasta", nargs="+") #multiple input files will be stored in a list
args = parser.parse_args()
#fastaList is a list of all fasta files
fastaList = args.inFasta

compList = dic.composition(fastaList)
phylip_matix=dic.phylip_matix(compList)


#Input list of fasta files
#Output dictionary with {id ; composition}
#dic.composition()

#Input fasta files with id and sequence
#dic.readFastq()

#Assertion testing outside of functions

#read in test fasta(s)


#print(composition(fastaList))
