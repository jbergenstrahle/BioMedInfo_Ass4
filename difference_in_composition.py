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
                test_input(seqs)
    return ids, seqs

def composition(fastaList):
    """Calculates the composition vectors to a dictionary,
    with the corresponding ID (organism)"""
    compList = {}
    compVector = []
    for fasta in fastaList:
        id, seq = readFastq(fasta)
        test_input(seq)
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

print(composition(fastaList))

def test_input(seqs):
    if seqs not in 'ACGT':
        raise Exception('There are non-bases characters in the fasta')
    elif len(seqs)=0:
        raise Exception('Fasta file is empty')
    else:
        continue

def test_id(id):
    if len(id)=0:
        raise Exception('Fasta file is empty')
    elif id.startswith(">"):
         raise Exception('Fasta file without >, add a proper fasta file')
    else:
        continue

if __name__ == "__main__":
    # execute only if run as a script
    main()
