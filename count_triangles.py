#From https://www.careercup.com/question?id=5988741646647296
# Given a undirected graph with corresponding edges. Find the number of possible triangles? 
# Example: 
# 0 1 
# 2 1 
# 0 2 
# 4 1 
# 
# Answer: 
# 1

def string_to_graph(string):
    graph=dict()
    def add_to_graph(a,b):
        if a in graph:graph[a].add(b)
        else:         graph[a]=   {b}
    for line in string.splitlines():
        x,y=line.split()
        add_to_graph(x,y)
        add_to_graph(y,x)
    return graph
def count_triangles(string):
    graph=string_to_graph(string)
    count=0
    for vertex,neighbors in graph.items():
        for neighbor in neighbors:
            count+=len(neighbors&graph[neighbor])
    return count//6

print(count_triangles('0 1\n2 1\n0 2\n4 1'))#prints 1