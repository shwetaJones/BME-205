**Compute the Probability of a Hidden Path**

**Problem:**
	
	Given: A hidden path π followed by the states States and transition matrix Transition of an HMM (Σ, States, Transition, Emission).
	
	Return: The probability of this path, Pr(π). You may assume that initial probabilities are equal.
	
**Sample DataSet:**
	
	AABBBAABABAAAABBBBAABBABABBBAABBAAAABABAABBABABBAB
	--------
	A   B
	--------
		A   B
	A   0.194   0.806
	B   0.273   0.727

**Sample Output:**
	
	5.01732865318e-19
