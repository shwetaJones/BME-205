**Compute the Probability of an Outcome Given a Hidden Path**

**Problem:**
	
	Given: A string x, followed by the alphabet Σ from which x was constructed, followed by a hidden path π, followed by the states States and emission matrix Emission of an HMM (Σ, States, Transition, Emission).
	
	Return: The conditional probability Pr(x|π) that string x will be emitted by the HMM given the hidden path π.
	
**Sample DataSet:**
	
	xxyzyxzzxzxyxyyzxxzzxxyyxxyxyzzxxyzyzxzxxyxyyzxxzx
	--------
	x   y   z
	--------
	BBBAAABABABBBBBBAAAAAABAAAABABABBBBBABAABABABABBBB
	--------
	A   B
	--------
		x   y   z
	A   0.612   0.314   0.074 
	B   0.346   0.317   0.336

**Sample Output:**
	
	1.93157070893e-28
