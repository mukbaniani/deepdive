import math

class Polygon:
    def __init__(self, edges, circum_radius):
        self._edges = edges
        self._circum_radius = circum_radius

    @property
    def edges(self):
        return self._edges

    @property
    def circum_radius(self):
        return self._circum_radius

    @property
    def vertices(self):
        return self._edges

    @property
    def interior_angle(self):
        return (self._edges - 2) * 180 / self._edges

    @property
    def edge_length(self):
        return 2 * self._circum_radius * math.sin(math.pi / self._edges)

    @property
    def apothem(self):
        return self._circum_radius * math.cos(math.pi / self._edges)

    @property
    def area(self):
        return 0.5 * self._edges * self.edge_length * self.apothem

    @property
    def perimeter(self):
        return self._edges * self.edge_length

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError(f'{other} must by Polygon')
        return self._edges == other._edges and self._circum_radius == other._circum_radius

    def __ge__(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError(f'{other} must by Polygon')
        return self._edges == other._edges

    def __repr__(self):
        return f'{self.__class__.__name__}(n={self._edges}, R={self._circum_radius})'


class Polygons:
    def __init__(self, m, R):
        if m < 3:
            raise ValueError('m must be greater than 3')
        self._m = m
        self._R = R
        self._polygons = [Polygon(i, R) for i in range(3, m + 1)]

    def __len__(self):
        return self._m - 2

    def __repr__(self):
        return f'{self.__class__.__name__}(m={self._m}, R={self._R})'

    def __getitem__(self, s):
        return self._polygons[s]

    @property
    def max_efficiency_polygon(self):
        sorted_polygons = sorted(self._polygons,
                                 key=lambda p: p.area / p.perimeter,
                                 reverse=True)
        return sorted_polygons[0]
