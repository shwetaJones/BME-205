**Find the Longest Path in a DAG**

**Problem:**
	
	Given: An integer representing the source node of a graph, followed by an integer representing the sink node of the graph, followed by an edge-weighted graph. The graph is represented by a modified adjacency list in which the notation "0->1:7" indicates that an edge connects node 0 to node 1 with weight 7.
	
	Return: The length of a longest path in the graph, followed by a longest path. (If multiple longest paths exist, you may return any one.)

**Sample DataSet:**
	
	0
	4
	0->1:7
	0->2:4
	2->3:2
	1->4:1
	3->4:3

**Sample Output:**
	
	9
	0->2->3->4
