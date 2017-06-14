import unittest
import argparse
import difference_in_composition as dic

#Input list of fasta files
#Output dictionary with {id ; composition}
#dic.composition()

#Input fasta files with id and sequence
#dic.readFastq()

#Assertion testing outside of functions

#read in test fasta(s)

badList ={"testCorrupt.fa","testCorrupt2.fa", "testCorrupt3,fa"}

for entry in badList:
    dic.readFastq(entry)

