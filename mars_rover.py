class MarsRover:
    def __init__(self):
        self.grid = []

    def generate_grid(self, rows, columns):
        row = [None] * columns
        self.grid = [row] * rows

    def view_grid(self):
        return self.grid

    def place_rover(self, row, column, facing):
        if column == 0:
            self.grid[0][0] = 'N' # this fails (gives us two 'N's in the grid)

            # this version works
            # self.grid[0] = ['N', None]
            
            # this version works
            # self.grid = [
            #     ['N', None],
            #     [None, None]
            # ]
        else:
            self.grid = [
                [None, None],
                ['N', None]
            ]


        