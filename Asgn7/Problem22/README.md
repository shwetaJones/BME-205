**Compute the Probability of a String Emitted by an HMM**

**Problem:**
	
	Given: A string x, followed by the alphabet Σ from which x was constructed, followed by the states States, transition matrix Transition, and emission matrix Emission of an HMM (Σ, States, Transition, Emission).
	
	Return: The probability Pr(x) that the HMM emits x.
	
**Sample DataSet:**
	
	xzyyzzyzyy
	--------
	x   y   z
	--------
	A   B
	--------
		A   B
	A   0.303   0.697 
	B   0.831   0.169 
	--------
		x   y   z
	A   0.533   0.065   0.402 
	B   0.342   0.334   0.324

**Sample Output:**
	
	1.1005510319694847e-06
