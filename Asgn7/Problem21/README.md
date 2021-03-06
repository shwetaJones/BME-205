**Implement the Viterbi Algorithm**

**Problem:**
	
	Given: A string x, followed by the alphabet Σ from which x was constructed, followed by the states States, transition matrix Transition, and emission matrix Emission of an HMM (Σ, States, Transition, Emission).
	
	Return: A path that maximizes the (unconditional) probability Pr(x, π) over all possible paths π.
	
**Sample DataSet:**
	
	xyxzzxyxyy
	--------
	x   y   z
	--------
	A   B
	--------
		A   B
	A   0.641   0.359
	B   0.729   0.271
	--------
		x   y   z
	A   0.117   0.691   0.192   
	B   0.097   0.42    0.483

**Sample Output:**
	
	AAABBAAAAA
