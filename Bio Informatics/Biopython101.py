#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 14:31:01 2024

@author: nmfuphicsir.co.za

Python with Bioinformatics

"""
dna_sequence ="ATGGTCTACATAGCTGACAAAGTGACCTTGAGCCCTGCAacgt"
##Prints the DNA sequence.
print(dna_sequence)
###Prints the length of the DNA sequence.
print(len(dna_sequence)) 
##: Counts the occurrences of the nucleotide "A" in the DNA sequence and prints the result.
print(dna_sequence.count("A")) 

##Prints the first three nucleotides of the DNA sequence
print(dna_sequence[0:3]) 

##Converts the DNA sequence to uppercase and prints it
print(dna_sequence.upper()) 
DNA_SEQUENCE= dna_sequence.upper()
print(DNA_SEQUENCE)

##Converts the DNA sequence to lowercase and prints it.
print(dna_sequence.lower()) 


##If you are simulating mutations in a DNA sequence, you might want to replace one nucleotide with another to model a mutation
mutated_dna_sequence=dna_sequence.replace("A", "T")
print(mutated_dna_sequence)


#Checking index of each nucleaotide.
for index, letter in enumerate(mutated_dna_sequence):
    print(index, letter)

##Arithmetic Operations on Seq such as addition and multiplication
###Creates 2 DNA sequence object.
dna1 = "AGCT"
dna2 = "TCGA"


##Concatenation
dna3 = dna1 + dna2 

##Prints the concatenated DNA sequence.
print(dna3)

##Repetition 
dna4 = dna1 * 3 
print(dna4) 

#-------------------------------------------------------------------------------------------------------------
"""
Installation 
pip install biopython
The official Biopython website (https://biopython.org/) 
Biopython Documentation: https://biopython.org/docs/1.75/api/Bio.Seq.html
"""


####Sequencing Handling
from Bio.Seq import Seq
###Basic Sequence Manipulations
coding_dna=Seq("ATCGAGCTACCGTCA")
print(coding_dna)


###Get a complement strand sequence
complement_dna_sequence= coding_dna.complement()
print(complement_dna_sequence)


## Generates the reverse complement of the DNA sequence
template_dna= coding_dna.reverse_complement()
print(template_dna)


##Transcription, showing transcribed rna
messenger_rna= coding_dna.transcribe()
print(messenger_rna)

##Translation: 
##Converts the DNA sequence to a string and prints it
protein_sequence = coding_dna.translate()


#------------------------------------------------------------------
###File Format
###Reading a FASTA file:
#pip install wget

import wget  
from Bio import SeqIO
# Specify the path to the FASTA file


##Get data!
url = "https://www.ncbi.nlm.nih.gov/WebSub/html/help/sample_files/nucleotide-sample.txt"
fasta_file= wget.download(url)


# Parse the FASTA file and iterate over the sequences
for record in SeqIO.parse(fasta_file, "fasta"):
    print(f"ID: {record.id}")
    print(f"Description: {record.description}")
    print(f"Sequence: {record.seq}")
    print("Length:", len(record))
    print("\n" + "=" * 30 + "\n")  # Separating records for better readability



"""
#Reading a GenBank file:
from Bio import SeqIO
# Specify the path to the GenBank file
genbank_file_path = "example.gb"

# Parse the GenBank file and iterate over the sequences
for record in SeqIO.parse(genbank_file_path, "genbank"):
    print(f"ID: {record.id}")
    print(f"Description: {record.description}")
    print(f"Sequence: {record.seq}")
    
  """
  
  
  
##Writing a sequence to a FASTA file:
from Bio.SeqRecord import SeqRecord

# Create a SeqRecord object with a sequence and metadata
sequence = Seq("ATGCGAATACAGAGTAG")
record = SeqRecord(sequence, id="example_id", description="Example sequence")

# Specify the output file path
output_fasta_path = "output.fasta"

# Write the SeqRecord to a FASTA file
SeqIO.write(record, output_fasta_path, "fasta")

##Writing multiple sequences to a FASTA file:
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

# Create multiple SeqRecord objects with sequences and metadata
sequences = [
    SeqRecord(Seq("ATGCGAATACAGAGTAG"), id="seq1", description="Sequence 1"),
    SeqRecord(Seq("TTAGCTGAACCTATCGG"), id="seq2", description="Sequence 2"),
]

# Specify the output file path
output_fasta_path = "output.fasta"

# Write the SeqRecord objects to a FASTA file
SeqIO.write(sequences, output_fasta_path, "fasta")

#--------------------------------------------------------------------------

##Online Database
## Searching PubMed for a specific term and retrieving the list of matching IDs
from Bio import Entrez
# Set your email address (required by NCBI), Provide your email address to identify yourself to NCBI
Entrez.email = "nmfuphi@csir.co.za"

# Define the search term
search_term = "biopython"
# This gives you the list of available databases 
handle = Entrez.einfo() 
rec = Entrez.read(handle)
handle.close()
print(rec.keys())
 
 
 ##Show all the available NCBI DBs 
rec['DbList']

# Search PubMed for articles related to a specific query
# Perform the PubMed search
handle = Entrez.esearch(db="pubmed", term="Covid19 in South Africa")
record = Entrez.read(handle)
handle.close()

# Print the list of PubMed IDs (PMIDs) matching the search term
print("List of PMIDs:", record["IdList"])



##Similarly, you can use the Entrez.efetch() function to retrieve detailed information about specific records using their IDs. 
##Below is an example of how to retrieve information for a specific PubMed ID:


from Bio import Entrez # Provide your email address to identify yourself to NCBI Entrez.email = "your@email.com" 
# Specify the PubMed ID
pubmed_id = "12345678"
 # Fetch information for the specified PubMed ID 
handle = Entrez.efetch(db="pubmed", id=pubmed_id, rettype="xml") 
record = Entrez.read(handle)
 # Print the title and abstract of the article
article = record["PubmedArticle"][0]["MedlineCitation"]["Article"]
title = article["ArticleTitle"]
abstract = article["Abstract"]["AbstractText"][0] if "Abstract" in article else "No abstract available"
print("Title:", title) 
print("Abstract:", abstract) 
# Close the handle

handle.close()

"""
### Search and retrieve information from the NCBI nucleotide database (db = "nucleotide"):
from Bio import Entrez

# Set your email address (required by NCBI)
Entrez.email = "nmfuphi@csir.co.za"


# Define the search term
search_term = "biopython"

# Perform the nucleotide database search
handle = Entrez.esearch(db="nucleotide", term=search_term)
record = Entrez.read(handle)

# Print the list of matching accession numbers
print("List of Accession Numbers:", record["IdList"])

# Fetch details of the first record using its accession number
if record["IdList"]:
    accession_number = record["IdList"][0]
    handle = Entrez.efetch(db="nucleotide", id=accession_number, rettype="gb", retmode="text")
    sequence_record = handle.read()

    # Print the sequence record in GenBank format
    print("\nGenBank Record:")
    print(sequence_record)
    
   

#--------------------------------------------------------------------------------
##3D structure analysis
from Bio.PDB import PDBParser
parser = PDBParser()
structure = parser.get_structure("example", "example.pdb")

##Phylogenetics
from Bio import Phylo
tree = Phylo.read("tree.nwk", "newick")

##Population Studies

from Bio.PopGen import HardyWeinberg
loci_data = [[25, 37, 42], [30, 35, 40]]
results = HardyWeinberg(loci_data) 

 """



