# graphs
# - orieontovany, ohodnoceny, 
# souvislost - silna (=odkudkoliv kamkoliv), slaba (=muzu se dostat do kazdyho bodu, ale ne pri kazdem pocatku)
# 
# ----- matice sousednosti (=matice vsech s vsemi)   
#     v1 v2 v3 v4 v5
# v1  0  1  0  1  1
# v2  1  1  0  0  1
# v3  0  1  0  0  0
# v4  1  1  0  0  0
# v5  1  0  0  1  0
#
# ----- adjacency list (=seznam spojeni)
# v1 | v2, v4, v5
# v2 | v1, v2, v5
# v3 | v2
# v4 | v1, v2
# v5 | v1, v4
#
# ----- edge list
# v1 - v2,
# v2 - v1,
# v5 - v1,
# v2 - v2,
# v4 - v1,
# v2 - v5,
# v5 - v4,
# v1 - v4,
# v4 - v2,
# v3 - v2,
# v1 - v5
# 