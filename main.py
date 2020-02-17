import board
import node
import pathfinding


start = node.Node(0, 0)
end = node.Node(4,5)
start.g_cost = 0
start.h_cost = start.dist_from_node(end)
start.f_cost = start.g_cost + start.h_cost
arena = board.Board(width=10,height=10,start=start,end=end)

def test_path_found_no_obstacles():
    return pathfinding.a_star(arena, start, end)

def test_path_not_found():
    for i in range(arena.height):
        arena.board[i][1].val = node.Node.obstacle_val
    return pathfinding.a_star(arena, start, end)

# print(arena)
# print(arena.start.dist_from_node(arena.end))
# adjacent = node.Node(1,1)
# print(arena.start.dist_from_node(adjacent))

# shortest_path = test_path_not_found()
shortest_path = test_path_found_no_obstacles()
print("shortest path: ", end='')
if shortest_path:
    print(shortest_path)
else:
    print("not found")
