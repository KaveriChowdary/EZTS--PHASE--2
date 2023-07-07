def krushkals(graph):
    edge_list=[]
    for source in graph:
        for edge in graph[source]:
            weight, dest = edge
            edge_list.append((weight,source,dest))
    edge_list.sort()
    parents={}
    for vertex in graph:
        parents[vertex] = vertex
    mst=[]
    
    def find_parent(vertex="a"):
        if parents[vertex]!=vertex:  
            parents[vertex]=find_parent(parents[vertex])
        return parents[vertex]
    
    for edge in edge_list:
        weight,source,dest=edge
        if find_parent(source)!=find_parent(dest):
            mst.append(edge)
            parents[find_parent(source)]=find_parent(dest)
    return mst
            
graph = {
    'a':[(10,'f'),(28,'b')],
    'b':[(28,'a'),(14,'g'),(16,'c')],
    'c':[(16,'b'),(12,'d')],
    'd':[(12,'c'),(18,'g'),(22,'e')],
    'e':[(22,'e'),(24,'g'),(25,'f')],
    'f':[(25,'e'),(10,'a')],
    'g':[(14,'b'),(18,'d'),(24,'e')],
    }
mst=krushkals(graph)
print(*mst,sep="\n") 