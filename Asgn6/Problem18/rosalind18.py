class problemEighteen:
    """ The class tries to find every amino acid string Peptide such that Cyclospectrum(Peptide) """
    aaWeight = {'G':57, 'A':71, 'S':87, 'P':97, 'V':99, 'T':101, 'C':103, 'I':113, 'L':113, 'N':114, 'D':115, 'K':128, 'Q':128, 'E':129, 'M':131, 'H':137, 'F':147, 'R':156, 'Y':163, 'W':186}
    weights = [57, 71, 87, 97, 99, 101, 103, 113, 114, 115, 128, 129, 131, 137, 147, 156, 163, 186]
    def __init__(self, aaSeq):
        """ Description: The method saves values as self """
        """ Input: The input is the amino acid seq """
        """ Output: There is no output """
        self.aaSeq = aaSeq

    def differentSegments(self, peptide):
        """ Description: The method creates all the possible segments """
        """ Input: The input for this method is the peptide sequence """
        """ Output: The output is the sorted list of segments """
        spec = [0, sum(peptide)]
        temp = peptide + peptide
        for k in range(1, len(peptide)):
            for i in range(len(peptide)):
                subpeptide = temp[i:i + k]
                spec.append(sum(subpeptide))
        spec.sort()
        return spec

    def valid(self, peptide):
        """ Description: This method checks to see if chosen peptide is consistent """
        """ Input: The input is peptide sequence """
        """ Output: The output returns either a true or false """
        prefixMass = [0]; linearSpectrum = [0]
        for i in range(len(peptide)):
            temp = prefixMass[i] + peptide[i]
            prefixMass.append(temp) #adds the masses into a pist
        for i in range(len(peptide)):
            for j in range(i+1, len(peptide)+1):
                linearSpectrum.append(prefixMass[j] - prefixMass[i]) #appends the differentce between the two to determine the final value
        linearSpectrum.sort()

        if sum(peptide) > self.aaSeq[-1] - self.weights[0]: #checks to see if the mass is in the list of masses
            return False
        for mass in linearSpectrum:
            if mass not in self.aaSeq:
                return False
        return True #if it is valid, true is returned

    def cyclopeptideSequencing(self):
        """ Description: This method does cyclopeptide sequencing """
        """ Input: There is no input, however, """
        """ Output: The output is every amino acid string Peptide such that Cyclospectrum(Peptide)"""
        result = set() #ensures there are no repitions
        peptides = [[]]
        while peptides:
            newPep = []
            for pep in peptides: #determines the mass
                for mass in self.weights:
                    newPep.append(pep + [mass])
            peptides = newPep
            for peptide in peptides:
                if sum(peptide) == self.aaSeq[-1]: #checks to see if the calculated sum meets the given amino acid spectrum
                    if self.differentSegments(peptide) == self.aaSeq:
                        result.add("-".join(map(str, peptide))) #formats and adds the valid string to the results list
                    peptides = [pep for pep in peptides if pep != peptide]
                elif not self.valid(peptide): #checks to see if the peptide is valid
                    peptides = [pep for pep in peptides if pep != peptide]
        return result #returns the final list of amino acid string peptide masses

def main(inFile):
    """ Description: The main reads in an input file and outputs all the possible peptide sequence masses"""
    """ Input: The input file contains the spectrum"""
    """ Output: The output is every amino acid string Peptide such that Cyclospectrum(Peptide)"""
    inFile = open(inFile, "r")
    spectrum = [int(x) for x in inFile.readline().strip().split()]
    processed = problemEighteen(spectrum)
    sequenced = processed.cyclopeptideSequencing()
    print(" ".join(sequenced))

if __name__== "__main__":
    # main("test18.txt")
    main("rosalind_ba4e.txt")
