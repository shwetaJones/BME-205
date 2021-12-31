**Variables and Some Arithmetic**

**Problem:**
	
	Given: A collection of k-mers Patterns.
	
	Return: The de Bruijn graph DeBruijn(Patterns), in the form of an adjacency list.

**Sample DataSet:**
	
	GAGG
	CAGG
	GGGG
	GGGA
	CAGG
	AGGG
	GGAG

**Sample Output:**
	
	AGG -> GGG
	CAG -> AGG,AGG
	GAG -> AGG
	GGA -> GAG
	GGG -> GGA,GGG
