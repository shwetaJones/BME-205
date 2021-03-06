**Solve the Soft Decoding Problem**

**Problem:**
	
	Given: A string x, followed by the alphabet Σ from which x was constructed, followed by the states States, transition matrix Transition, and emission matrix Emission of an HMM (Σ, States, Transition, Emission).
	
	Return: The probability Pr(πi = k|x) that the HMM was in state k at step i (for each state k and each step i).
	
**Sample DataSet:**
	
	zyxxxxyxzz
	--------
	x   y   z
	--------
	A   B
	--------
		A   B
	A   0.911   0.089
	B   0.228   0.772
	--------
		x   y   z
	A   0.356   0.191   0.453 
	B   0.04    0.467   0.493

**Sample Output:**
	
	A   B 
	0.5438  0.4562 
	0.6492  0.3508 
	0.9647  0.0353 
	0.9936  0.0064 
	0.9957  0.0043 
	0.9891  0.0109 
	0.9154  0.0846 
	0.964   0.036 
	0.8737  0.1263 
	0.8167  0.1833
