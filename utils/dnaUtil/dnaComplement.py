# Imports
from Bio import SeqIO

def complement(dnaSeq):
    
    complementSeq = {}

    for seqID, seq in dnaSeq.items():

        dnaComp = ""
        seq = seq.upper()

        # Constructing the complement bases 
        for base in seq:

            if base == 'A':
                dnaComp += 'T'
            elif base == 'T':
                dnaComp += 'A'
            elif base == 'C':
                dnaComp += 'G'
            elif base == 'G':
                dnaComp += 'C'
            else:
                dnaComp += '?'
        
        # Reversing the sequence
        reverseDNA = ''.join(reversed(dnaComp))
        complementSeq[seqID] = reverseDNA
    
    return complementSeq 
