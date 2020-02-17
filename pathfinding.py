def a_star(arena, start, end):
    '''Implementation of algorithm from this video: https://www.youtube.com/watch?v=-L-WgKMFuhE
    '''
    open_nodes = {}
    closed_nodes = {}
    open_nodes[start] = start.f_cost
    while open_nodes:
        # https://stackoverflow.com/questions/3282823/get-the-key-corresponding-to-the-minimum-value-within-a-dictionary/3282904#3282904
        current = min(open_nodes, key=open_nodes.get)
        del open_nodes[current]
        closed_nodes[current] = current.f_cost

        # print_nodes_for_debugging(open_nodes, "open_nodes")
        # print_nodes_for_debugging(closed_nodes, "closed_nodes")
        
        if current.x == end.x and current.y == end.y:
            # TODO: return the path itself, find a way to reconstruct and visualize
            return current.f_cost
        
        # TODO: change this to a class method in node?
        neighbors = find_neighbors(arena, current, closed_nodes)
        for neighbor in neighbors:
            if neighbor.dist_from_node(current) < neighbor.g_cost or neighbor not in open_nodes:
                neighbor.g_cost = neighbor.dist_from_node(start)
                neighbor.h_cost = neighbor.dist_from_node(end)
                neighbor.f_cost = neighbor.g_cost + neighbor.h_cost
                neighbor.parent = current
                if neighbor not in open_nodes:
                    open_nodes[neighbor] = neighbor.f_cost
    return None

def find_neighbors(arena, current, closed_nodes):
    directions = [[1,0], [0,1], [-1,0], [0,-1]] # allow for movement in the up, down, left, right directions, no diagonals
    neighbors = []
    for direction in directions:
        if 0 <= current.x+direction[0] < arena.height and 0 <= current.y+direction[1] < arena.width:
            node = arena.board[current.x+direction[0]][current.y+direction[1]]
            if node.is_traversable() and node not in closed_nodes:
                neighbors.append(node)
    return neighbors

def print_nodes_for_debugging(nodes, name):
    print("nodes in {}:".format(name))
    for node in nodes:
        print('\t{}'.format(node))
    print()
    