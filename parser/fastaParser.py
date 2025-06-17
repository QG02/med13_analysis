# Imports
from Bio import SeqIO
import json
import os

# Parsing function
def parseFastaInput():
    # Ask user for inputs
    fastaPath = input("Enter the path to your FASTA file: ").strip()
    metadataPath = input("Enter the path to your metadata JSON file: ").strip()
    typeMap = fileType(metadataPath)
    sequences = parseFasta(fastaPath, typeMap)
    return fastaPath, sequences

# Function to extract data from JSON file
def fileType(jsonPath):
    with open(jsonPath, "r") as f:
        data = json.load(f)    
        # Creates a dictionary of file types using the metadata
        typeMap = {
        file["filePath"]: file["fileType"]
        for file in data["genes"]["files"]
    }
    return typeMap

# Function to match the inputed file to its type
def parseFasta(filePath, typeMap):
    fileName = os.path.basename(filePath)
    fileType = typeMap.get(fileName)

    if not fileType:
        print("Could not identify file type from metadata.")
        return {}

    print(f"Detected file type from metadata: {fileType}")

    # Print out the sequences
    sequences = {}
    for record in SeqIO.parse(filePath, "fasta"):
        sequences[record.id] = record.seq
    return sequences

def fileIdentifier(filePath):
    desc = []
    # open and read the file 
    with open(filePath, "r") as f:
        for record in SeqIO.parse(f,"fasta"):
            header = record.description
            label = classifySeq(header)
            desc.append((header,label))
    return desc
    # extract header from records
    # run a conditional to see what kind of information it is

def classifySeq(header):
    if "mRNA" in header or header.startswith("NM_") or header.startswith("XM_"):
        if header.startswith("NM_"):
            return "experimentally curated mRNA"
        else:
            return "computationally modeled mRNA"
    elif "protein" in header or header.startswith("NP_") or header.startswith("XP_"):
         if header.startswith("NP_"):
            return "protein from experimentally curated mRNA"
         else:
            return "protein from computationally curated mRNA"
    elif "chromosome=" in header:
        if ":c" in header:
            return "genomic DNA - complement strand"
        else:
            return "genomic DNA - original strand"
    else:
        return "unclassified"
