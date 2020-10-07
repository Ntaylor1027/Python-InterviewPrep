
# Possible scores for a final football score
# Solution Explained:
#   A 9 point score can be achieved in the following ways
#       - score 7 points after 2 point play
#       - score 6 points followed by a 3 point play
#       - score 2 points followed by a 7 point play
#   Create a 2d array that holds the values such that
#           0       1       2       3       4       5       6       7       8       9       10      11      12
#   2       1       0       1       0       1       0       1       0       1       0       1       0       1
#   2,3     1       0       1       1       1       1       2       1       2       2       2       2       3
#   2,3,7   1       0       1       1       1       1       2       2       2       3       3       3       4
