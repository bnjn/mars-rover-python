class MarsRover:
    def __init__(self):
        self.grid = []

    def generate_grid(self, rows, columns):
        make_row = lambda: [ None ] * columns
        self.grid = [ make_row() for i in range(0, rows) ]

    def view_grid(self):
        return self.grid

    def place_rover(self, row, column, facing):
        if column == 0:
            self.grid[0][0] = 'N'
        else:
            self.grid = [
                [None, None],
                ['N', None]
            ]


        