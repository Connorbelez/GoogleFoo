# graph = {
#   'A' : ['B','C'],
#   'B' : ['D', 'E'],
#   'C' : ['F'],
#   'D' : [],
#   'E' : ['F'],
#   'F' : []
# }


graph = [[0, 0, 0, 0, 0, 0],
          [1, 1, 1, 1, 1, 0],
          [0, 0, 0, 0, 0, 0],
          [0, 1, 1, 1, 1, 1],
          [0, 1, 1, 1, 1, 1],
          [0, 0, 0, 0, 0, 0]]

graph4 = [[0, 0, 1, 1, 1, 1],
          [0, 0, 0, 0, 0, 0],
          [0, 1, 1, 1, 1, 0],
          [0, 1, 0, 0, 0, 0],
          [0, 1, 0, 1, 1, 1],
          [0, 1, 0, 0, 0, 0]]

graph3 = [[0,0],
          [0,0]]

graph5 = [[0,0,0],
          [0,0,0]]
graph2 = [[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]

graph6 = [[0,1,1,0,1,0,0,1,0,0,0,1,1,0,1,0,0,1,1,1],
            [1,1,1,1,1,0,0,1,1,1,0,1,1,1,1,1,0,0,0,0],
            [0,0,0,0,0,1,0,0,0,0,1,1,0,1,1,0,1,0,0,0],
            [1,0,0,1,0,0,0,0,0,0,1,1,1,1,1,0,1,1,1,1],
            [1,1,1,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1],
            [1,0,1,0,0,1,0,1,1,1,0,0,0,0,0,1,1,0,0,0],
            [1,1,1,1,1,1,0,0,0,1,0,1,0,0,1,1,0,1,1,0],
            [1,0,0,0,0,1,1,0,0,1,1,1,0,1,0,1,1,1,0,1],
            [0,1,1,0,1,1,1,0,0,1,1,1,0,1,0,0,1,0,0,1],
            [0,0,0,0,0,0,1,1,0,0,0,1,0,0,0,1,0,0,1,1],
            [0,1,1,0,0,0,0,0,1,1,0,0,0,0,0,0,0,1,0,0],
            [0,1,0,0,1,0,0,0,1,1,1,0,0,0,0,1,0,1,1,1],
            [0,1,1,0,0,1,1,1,0,0,1,1,1,0,0,1,0,1,1,1],
            [1,1,1,0,1,0,1,1,1,0,0,1,1,0,0,1,1,0,1,0],
            [0,0,1,0,1,0,1,1,0,0,1,0,1,0,0,0,0,0,1,1],
            [1,1,0,0,1,0,1,0,0,0,1,0,1,0,0,0,0,0,0,1],
            [1,0,1,1,0,0,1,1,1,1,0,1,1,0,1,0,1,0,1,1],
            [0,1,0,0,0,1,0,1,0,0,0,0,1,1,0,0,0,0,1,0],
            [0,0,0,1,0,0,1,0,1,1,0,0,1,0,0,1,1,0,0,1],
            [1,0,0,0,0,0,1,0,1,1,1,0,1,1,1,1,1,0,0,0]]

def getANodes(graph,point):
    validPaths = []
    width = len(graph[0]) - 1
    height = len(graph) - 1
    pointRow = point[0]
    pointColoumn = point[1]
    if pointColoumn > 0:
        if graph[pointRow][pointColoumn-1] == 0:
            validPaths.append((pointRow, pointColoumn-1))
    if pointColoumn < width:
        if graph[pointRow][pointColoumn+1] == 0:
            validPaths.append((pointRow, pointColoumn+1))
    if pointRow > 0:
        if graph[pointRow-1][pointColoumn]==0:
            validPaths.append((pointRow-1, pointColoumn))
    if pointRow < height:
        if graph[pointRow+1][pointColoumn]==0:
            validPaths.append((pointRow+1, pointColoumn))

    return validPaths

def bfs(graph,start,end):
    visited = [start]
    pred = {}
    queue = []
    previous = []
    #start = (row,coloumn)
    queue.append(start)
    while queue:
        s = queue.pop(0)
        if s == end:
            val = str(end)
            counter = 0
            while val != str(start):
                val = pred.get(val)
                # print(val)
                counter += 1
            return counter + 1
        neighbhours = getANodes(graph,s)

        for neighbhour in neighbhours:
            if neighbhour not in visited:
                pred[str(neighbhour)] = str(s)
                visited.append(neighbhour)
                queue.append(neighbhour)
        previous.append(s)
    # print(pred)

    return 1000

def solution(graph):
    end = (len(graph)-1,len(graph[0])-1)
    start = (0,0)
    bestRoute = 1000
    wallFound = False
    if(len(graph)) == 2 and len(graph[0])==2:
        return 2
    for row in range(len(graph)):
        for column in range(len(graph[row])):
            if graph[row][column] == 1:
                wallFound = True
                # tempGraph = graph
                graph[row][column] = 0
                tempBestRoute = bfs(graph,start,end)
                if tempBestRoute < bestRoute:
                    bestRoute = tempBestRoute
                graph[row][column] = 1
    if not wallFound:
        bestRoute = bfs(graph, start, end)
    return bestRoute

print(solution(graph))
print(solution(graph2))
print(solution(graph3))
print(solution(graph4))
print(solution(graph5))

print(solution(graph6))