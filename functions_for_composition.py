#import argparse

#parser = argparse.ArgumentParser()
#parser.add_argument("inFasta", nargs="+") #multiple input files will be stored in a list
#args = parser.parse_args()
#fastaList is a list of all fasta files
#fastaList = args.inFasta
import numpy as np
import itertools
import math
import pandas as pd


def test_seq(seqs):
    if len(seqs)==0:
        raise Exception("Fasta list is empty")
    for seq in seqs:
        if len(seq)==0:
            raise Exception('Fasta entry is empty')
        for base in seq:
            if base not in 'ACGT':
                raise Exception('There are non-bases characters in the fasta')



def test_id(ids):
    if len(ids)==0:
        raise Exception("Id list is empty")


def readFastq(fasta):
    """Parse Fasta files"""
    ids = []
    seqs = []
    with open(fasta) as fa:
        while True: #loop until end of file
            line = fa.readline().rstrip() #rstrip to strip whitespace
            if len(line) == 0:
                break
            if line[0] == '>':
                ids.append(line[1:])
                seqs.append('')
            else:
                test_seq(line)
                seqs[-1] += line.upper()

        test_id(ids)
    return ids, seqs

def composition(fastaList):
    """Calculates the composition vectors to a dictionary,
    with the corresponding ID (organism)"""
    compList = {}
    compVector = []
    for fasta in fastaList:
        id, seq = readFastq(fasta)
        test_seq(seq)
        id = id[0]
        test_id(id)
        seq = seq[0]
        nrA = seq.count("A")
        nrC = seq.count("C")
        nrG = seq.count("G")
        nrT = seq.count("T")
        nTot = nrA+nrC+nrG+nrT
        compVector = [nrA/nTot, nrC/nTot, nrG/nTot, nrT/nTot]
        compList[id] = compVector
    return compList

def phylip_matix(compList):
    num=len(compList)
    phylip=np.zeros((num,num),int)
    print(phylip)
    keyList=list()
    i=0
    for key, value in compList.items():
        keyList.append(key)
    #names = [_ for _ in keyList]
    #phylip = pd.DataFrame(phylip, index=names, columns=names)
    #print(phylip)
    print(keyList)
    posVec = [(0,0),(0,1),(1,0),(1,1)]
    for keya,keyb in itertools.combinations(keyList,2):
        a=compList.get(keya)
        b=compList.get(keyb)
        comp_d=math.sqrt(a[0]*(a[0]-b[0])**2 + a[1]*(a[1]-b[1])**2 + a[2]*(a[2]-b[2])**2 + a[3]*(a[3]-b[3])**2)*100

        #print(comp_d)
        #phylip[a,b]=comp_d
        #phylip[b,a]=comp_d
        phylip[1][1]=comp_d

        i+=1
        print(i)
        print(phylip)




if __name__ == "__main__":
    tryList = ["testCorrect.fa", "testCorrupt.fa", "testCorrupt2.fa", "testCorrupt3,fa"]
    for entry in tryList:
        print("Test:", entry)
        readFastq(entry)
        print("Test sucessfull")
    # execute only if run as a script
    main()
