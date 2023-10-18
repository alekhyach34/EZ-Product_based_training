vertices=7
graph=[[[]] for i in range(vertices)]
graph[0]=[[0,1,3],[0,4,2]]
graph[1]=[[1,0,3],[1,3,5],[1,7,10]]

visited=[False for i in range(vertices)]
def has_path(graph,src,dest,visited):
    if src==dest:
        return True
    for neighbour in graph[src]:
        print(neighbour)
        if visited[src]==False:
            visited[src]=True
            result=has_path(graph,neighbour[1],dest,visited)
            if result==True:
                return True
    return False
print(has_path(graph,0,1))