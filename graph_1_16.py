vertices=7
graph=[[[]] for i in range(vertices)]
graph[0]=[[0,1,3],[0,2,2]]
graph[1]=[[1,0,3],[1,3,10],[1,2,5]]
graph[3]=[[2,0,4],[2,3,10]]

graph[4]=[[4,5,3],[4,6,2]]
graph[5]=[[5,4,3],[5,6,10]]
graph[6]=[[6,4,2],[6,5,10]]
visited=[False for i in range(vertices)]
def has_path(graph,src,des,visited):
    if src==des:
        return True
    for neighbour in graph[src]:
        print(neighbour)
        if visited[src]==False:
            visited[src]=True
            res=has_path(graph,neighbour[1],des,visited)
            if res==True:
                return True
    return False
print(has_path(graph,0,2,visited))   