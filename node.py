class Node:
    default_val = '.' # valid square
    obstacle_val = 'x' # obstacle
    start_val = 's' # start
    end_val = 'e' # end
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.val = '.'
        self.g_cost = 0 # distance from start
        self.h_cost = 0 # distance from end (heuristic)
        self.f_cost = 0 # g_cost + h_cost
        self.parent = None
        

    def dist_from_node(self, other_node):
        '''Each square is 10 units, and distances are rounded to the nearest integer.
        '''
        return int((((self.x - other_node.x)**2 + (self.y - other_node.y)**2)**0.5)*10)

    def is_traversable(self):
        return self.val != 'x'


    def __str__(self):
        return "({},{}; f_cost={})".format(self.x, self.y, self.f_cost)
