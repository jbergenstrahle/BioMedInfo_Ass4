import argparse

parser = argparse.ArgumentParser()
parser.add_argument("inFasta", nargs="+") #multiple input files will be stored in a list
args = parser.parse_args()
#fastaList is a list of all fasta files
fastaList = args.inFasta

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
                seqs[-1] += line.upper()
    return ids, seqs

def composition(fastaList):
    """Calculates the composition vectors to a dictionary,
    with the corresponding ID (organism)"""
    compList = {}
    compVector = []
    for fasta in fastaList:
        id, seq = readFastq(fasta)
        id = id[0]
        seq = seq[0]
        nrA = seq.count("A")
        nrC = seq.count("C")
        nrG = seq.count("G")
        nrT = seq.count("T")
        nTot = nrA+nrC+nrG+nrT
        compVector = [nrA/nTot, nrC/nTot, nrG/nTot, nrT/nTot]
        compList[id] = compVector
    return compList


print(composition(fastaList))