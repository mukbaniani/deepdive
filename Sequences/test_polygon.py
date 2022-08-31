import unittest
from polygon import Polygon
import math


class TestPolygon(unittest.TestCase):
    def test_properties(self):
        n = 3
        R = 1
        p = Polygon(n, R)
        self.assertEqual(str(p), 'Polygon(n=3, R=1)')
        self.assertEqual(p.edges, n)
        self.assertEqual(p.vertices, n)
        self.assertEqual(p.circum_radius, R)
        self.assertEqual(p.interior_angle, 60)

        p.edges = 4
        p.circum_radius = 1
        n = 4
        assert (math.isclose(p.area, 2)), (f'actual: {p.area},'' expected: 2.0')
        assert (math.isclose(p.edge_length, math.sqrt(2))), (f'actual: {p.edge_length}, 'f' expected: {math.sqrt(2)}')
        assert (math.isclose(p.perimeter, n * math.sqrt(2))), (f'actual: {p.perimeter},' f' expected: {4 * math.sqrt(2)}')
        self.assertEqual(p.apothem, 0.7071067811865476)

if __name__ == '__main__':
    unittest.main()
