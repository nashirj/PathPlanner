import board
import node
import pathfinding
import view

def test_path_found_no_obstacles(arena, start, end):
    return pathfinding.a_star(arena, start, end)

def test_path_not_found(arena, start, end):
    for i in range(arena.height):
        arena.board[i][1].val = node.Node.obstacle_val
    cost = pathfinding.a_star(arena, start, end)
    # reset arena
    for i in range(arena.height):
        arena.board[i][1].val = node.Node.default_val
    return cost


# create parameters for arena
arena_w = 10
arena_h = 10
start = node.Node(0, 0)
end = node.Node(4,5)

arena = board.Board(arena_w, arena_h, start, end)
# shortest_path = test_path_not_found(arena, arena.start, arena.end)
shortest_path = test_path_found_no_obstacles(arena, arena.start, arena.end)
print("shortest path: ", end='')
if shortest_path:
    print(shortest_path)
else:
    print("not found")

view.display_board(arena)