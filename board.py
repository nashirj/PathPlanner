import node

class Board:
    def __init__(self, width, height, start, end):
        self.width = width
        self.height = height
        self.board = [[node.Node(i,j) for j in range(self.width)] for i in range(self.height)]
        self.start = start
        self.end = end
        # start and end points
        self.board[start.x][start.y] = start
        self.board[end.x][end.y] = end

    def __str__(self):
        ret = ''
        for i in range(self.height):
            for j in range(self.width):
                ret += self.board[i][j].val
            ret += '\n'

        return ret[:-1] # remove last trailing newline
