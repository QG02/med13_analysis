# Imports
from Bio import SeqIO

# Function to produce the transcribed RNA strand from the DNA sequence
def dnaTranscription(dnaStrand):

    result = {}

    for seqID, seq in dnaStrand.items():

        seq = seq.upper()
        rnaStrand = ""

        for base in seq:
            if base == 'A':
                rnaStrand += 'U'
            else:
                rnaStrand += base
        result[seqID] = rnaStrand
    return result


