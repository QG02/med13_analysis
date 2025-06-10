# Imports
from Bio import SeqIO

# Utility function to calculate base counts and CG contents
def cgContent(dnaSeq):
    
    # Empty dictionary to store count results
    result = {} 

    for seqID, seq in dnaSeq.items():
        seq = seq.upper()

        aBase = 0
        tBase = 0
        gBase = 0
        cBase = 0

        validBases = {'A', 'C', 'T', 'G'}
   
        aBase = seq.count('A')
        gBase = seq.count('G')
        tBase = seq.count('T')
        cBase = seq.count('C')

        totalBases = aBase + tBase + cBase + gBase

        # Handle empty sequences
        if totalBases == 0:
            cgPer = 0

        else:
            cgPer = ((cBase + gBase)/totalBases)*100

        # Store results into dictionary
        result[seqID] = {
            'A': aBase,
            'T': tBase,
            'C': cBase,
            'G': gBase,
            'Total': totalBases,
            'CG_Content': round(cgPer, 2)
        }

    return result
