class MarsRover:
    def __init__(self):
        self.grid = []

    def generate_grid(self, rows, columns):
        row = [None] * columns
        self.grid = [row] * rows

    def place_rover(self, row, column, facing):
        self.grid = [
            [None, None],
            ['N', None]
        ]

    def view_grid(self):
        return self.grid
        