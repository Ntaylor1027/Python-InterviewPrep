# Dijkstra's Algorithm
"""
Goal: Finds the shortest path from 1 vertex to anther
Returns: Matrix of vertex, shortest distance, previous vertex

2 list
Visted = []
Unvisted = [Unvisited]

(A)--6--(B)
|      / |   \ 5
1    2   2    (C)
|   /    |   / 5
(D)--1--(E)


Set up
1. Start at vertex A
2. Add A to result table with distance = 0
3. Add all other vertexes to infinite paths

Processing
4. Examine neigbors of current vertex
5. Calculate distance of neigbor to current
6. If neigbor distance < tracked distance
        Update shortest distance
        Update previous node
7. Push current vertex onto Visited
8. Visit unvisited vertex with smallest known distance from start/current vertex
    use shortest distance tracked in results table 
"""
