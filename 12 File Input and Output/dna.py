#Ikbel El Amri
#CodeAcademy unit 12
#File Input and Output
#DNA Analysis Investigation

"""Solve a DNA mystery with the DNA Analysis Investigation Project!

The project has methods for each of the following:
    1. Given a file, read in the DNA for each suspect and save it as a string
    2. Take a DNA string and split it into a list of codons
    3. Iterate through a suspect's codon list to see how many of their codons\
    match the sample codons
    4. Pick the right suspect to continue the investigation on"""

def read_dna(dna_file):
    """read a suspect's DNA sample and save it as a string"""
    #This will be the string that will eventually contain a suspect's DNA
    dna_data = ""
    #open dna file in read only mode
    with open(dna_file, "r") as f:
        #iterate through each line in f
        for line in f:
            #add line to the dna data
            dna_data += line
    #return the updated dna data string
    return dna_data

def dna_codons(dna):
    """take a DNA string and split it into a list of codons"""
    #create empty list of codons
    codons = []
    #Codons are 3-letter-long units of genetic code.
    #iterate through a suspect's DNA string, chop it into 3 letter strings (codons)
    for i in range(0, len(dna), 3):
        #check that the iterator doesn't exceed the length of dna
        #(don't add a string to the codon list that isn't at least 3 letters long)
        if (i+3) < len(dna):
            #slice string of dna into smaller strings that are 3 letters long
            #and append them to the list of codons
            codons.append(dna[i:i+3])
    #return the codons
    return codons

def match_dna(dna, sample):
    """Iterate through a suspect's codon list to see how many of their codons\ match the sample codons"""
    #variable storing # times a codon from the sample matches a codon from a suspect's DNA
    matches = 0
    #iterate through the list to find matches
    for codon in dna:
        #check if the codon also exists in the sample
        if codon in sample:
            #increment matches var to reflect a match
            matches += 1
    #return the number of matches
    return matches

def is_criminal(dna_sample, retrieved_sample):
    """determine if a suspect is the criminal"""
    #read in DNA samples and create a string to hold them
    dna_data = read_dna(dna_sample)
    #chop the string into a list of codons
    codons = dna_codons(dna_data)
    #match the sample with the DNA
    num_matches = match_dna(codons, retrieved_sample)
    #check if the number of matches is significant
    if num_matches>=3:
        print "%s codon matches found. The number of matches is significant. \
The investigation should continue." % (num_matches)
    else: #otherwise
        print "No significant number of codon matches were found. \
The suspect can be set free"
        

    
def main():
    #print welcome message
    print "Welcome to the DNA Analysis Investigation!\n"
    #print scenario
    scenario = "A spy deleted important files from a computer. There were a few \
witnesses at the scene of the crime, but no one is sure who exactly the spy was. \
Three possible suspects were apprehended based on surveillance video. Each suspect \
had a sample of DNA taken from them. The computer's keyboard was also swabbed for \
DNA evidence and, luckily, one small DNA sample was successfully retrieved from \
the computer's keyboard."
    print scenario + "\n"
    #print task
    task = "Given the three suspects' DNA and the sample DNA retreived from the \
keyboard, let's figure out who the spy is!"
    print task + "\n"
  
    #list containing the three codons that were retrieved from the computer's keyboard
    sample = ['GTA','GGG','CAC']
    #print sample
    print "Below are the retrieved codons from the computer's keyboard:"
    print sample

    print "\nInvestigating the first suspect:"
    is_criminal("suspect1.txt", sample)

    print "\nInvestigating the second suspect:"
    is_criminal("suspect2.txt", sample)

    print "\nInvestigating the third suspect:"
    is_criminal("suspect2.txt", sample)

main()
    
