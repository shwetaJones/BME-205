**Construct the De Bruijn Graph of a String**

**Problem:**
	
	Given: An integer k and a string Text.
	
	Return: DeBruijnk(Text), in the form of an adjacency list.

**Sample DataSet:**
	
	4
	AAGATTCTCTAC

**Sample Output:**
	
	AAG -> AGA
	AGA -> GAT
	ATT -> TTC
	CTA -> TAC
	CTC -> TCT
	GAT -> ATT
	TCT -> CTA,CTC
	TTC -> TCT
