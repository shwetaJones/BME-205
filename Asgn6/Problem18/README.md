**Find a Cyclic Peptide with Theoretical Spectrum Matching an Ideal Spectrum**

**Problem:**
	
	Given: A collection of (possibly repeated) integers Spectrum corresponding to an ideal experimental spectrum.
	
	Return: Every amino acid string Peptide such that Cyclospectrum(Peptide) = Spectrum (if such a string exists).
	
**Sample DataSet:**
	
	0 113 128 186 241 299 314 427

**Sample Output:**
	
	186-128-113 186-113-128 128-186-113 128-113-186 113-186-128 113-128-186
