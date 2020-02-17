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

    def set_start(self, start):
        self.board[self.start.x][self.start.y].val = node.Node.default_val
        self.board[start.x][start.y].val = node.Node.start_val

    def set_end(self, end):
        self.board[self.end.x][self.end.y].val = node.Node.default_val
        self.board[end.x][end.y].val = node.Node.end_val
