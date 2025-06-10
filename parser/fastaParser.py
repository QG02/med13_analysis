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
    return parseFasta(fastaPath, typeMap)

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
