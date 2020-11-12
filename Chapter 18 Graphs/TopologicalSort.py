# Topological Sort
"""
Have a set of visited nodes
Have a Stack of visited nodes with all child visited

Pick a starting node
Add it to visited 
Go to child nodes
Add child nodes to visited
If child (visited) node has no dependencies that 
    haven't been visited add it to the stack

Once you have touched all nodes from parent and added everything to the stack
    Pick random node that you have not visited yet


Notes:
    Seems like a depth first search and once you 
        have seen items you add them to a stack

"""