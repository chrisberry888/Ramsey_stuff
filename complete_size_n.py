#"graph" is a square matrix with 0 on the diagonal
#"colors" is a list of the colors
def complete_size_n(graph, n, colors):
    length = len(graph)
    result = {}
    for col in colors:
        result[col] = []
        
    for i in range(length-n+1):
        for j in range(i+1,n):
            result[graph[i,j]].append(j)