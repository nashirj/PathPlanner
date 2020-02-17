import board
import node
import pathfinding

def set_up_arena():
    start = node.Node(0, 0)
    end = node.Node(4,5)
    start.g_cost = 0
    start.h_cost = start.dist_from_node(end)
    start.f_cost = start.g_cost + start.h_cost
    return board.Board(width=10,height=10,start=start,end=end)


def test_path_found_no_obstacles(arena, start, end):
    return pathfinding.a_star(arena, start, end)

def test_path_not_found(arena, start, end):
    for i in range(arena.height):
        arena.board[i][1].val = node.Node.obstacle_val
    cost = pathfinding.a_star(arena, start, end)
    for i in range(arena.height):
        arena.board[i][1].val = node.Node.default_val
    return cost


arena = set_up_arena()
# shortest_path = test_path_not_found(arena, arena.start, arena.end)
shortest_path = test_path_found_no_obstacles(arena, arena.start, arena.end)
print("shortest path: ", end='')
if shortest_path:
    print(shortest_path)
else:
    print("not found")
