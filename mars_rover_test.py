import unittest
from mars_rover import MarsRover

class TestMarsRover(unittest.TestCase):
    def test_single_rover_no_movement_stays_in_place(self):
        mars_rover = MarsRover()
        mars_rover.generate_grid(2, 2)
        mars_rover.place_rover(0, 1, 'N')

        expected_grid = [
            [None, None],
            ['N', None]
        ]
        
        self.assertEqual(mars_rover.view_grid(), expected_grid)

    def test_another_single_rover(self):
        mars_rover = MarsRover()
        mars_rover.generate_grid(2, 2)
        mars_rover.place_rover(0, 0, 'N')

        expected_grid = [
            ['N', None],
            [None, None]
        ]

        self.assertEqual(mars_rover.view_grid(), expected_grid)

    def test_generate_grid_creates_empty_grid(self):
        mars_rover = MarsRover()
        mars_rover.generate_grid(1, 1)

        self.assertEqual(mars_rover.view_grid(), [[None]])
        
    def test_generate_two_by_two_grid_creates_empty_grid(self):
        mars_rover = MarsRover()
        mars_rover.generate_grid(2, 2)

        self.assertEqual(mars_rover.view_grid(), [[None, None], [None, None]])

    def test_generate_non_square_grid(self):
        mars_rover = MarsRover()
        mars_rover.generate_grid(2, 3)
        expected_grid = [
          [None, None, None],
          [None, None, None]
        ]
        self.assertEqual(mars_rover.view_grid(), expected_grid)

if __name__ == '__main__':
    unittest.main()