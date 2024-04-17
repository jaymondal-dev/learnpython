my_graph = {
    'A': [('B', 5), ('C', 3), ('E', 11)],
    'B': [('A', 5), ('C', 1), ('F', 2)],
    'C': [('A', 3), ('B', 1), ('D', 1), ('E', 5)],
    'D': [('C',1 ), ('E', 9), ('F', 3)],
    'E': [('A', 11), ('C', 5), ('D', 9)],
    'F': [('B', 2), ('D', 3)]
}

def shortest_path(graph, start, target = ''):
    # the list function creates a list from an iterable.
    unvisited = list(graph) #this lists all the available lists
    print("printing unvisitedlists\n",unvisited)
    distances = {node: 0 if node == start else float('inf') for node in graph}
    print("printing distances",distances)
    paths = {node: [] for node in graph}
    print("printing paths ",paths)
    paths[start].append(start)
    
    print("\nstarting loop\n")
    while unvisited:
        current = min(unvisited, key=distances.get)
        print("printing current in the loop",current)
        
        print("printing graph of the current in the loop",graph[current])
        
        for node, distance in graph[current]:
            print("==============")
            print(node,distance)
            print("==============")
            if distance + distances[current] < distances[node]:
                distances[node] = distance + distances[current]
                if paths[node] and paths[node][-1] == node:
                    paths[node] = paths[current][:]
                else:
                    paths[node].extend(paths[current])
                paths[node].append(node)
        unvisited.remove(current)


    print("\nending loop\n")
    print("printing paths after loop \n",paths)
    print("printing unvisited after loop \n",unvisited)
    print("printing distances after loop \n",distances)
    
    targets_to_print = [target] if target else graph
    for node in targets_to_print:
        if node == start:
            continue
        print(f'\n{start}-{node} distance: {distances[node]}\nPath: {" -> ".join(paths[node])}')
    
    return distances, paths
    
shortest_path(my_graph, 'A',)