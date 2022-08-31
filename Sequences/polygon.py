import math

class Polygon:
    def __init__(self, edges, circum_radius):
        self._edges = edges
        self._circum_radius = circum_radius
        self._interior_angle = None
        self._edge_length = None
        self._apothem = None
        self._area = None
        self._perimeter = None


    @property
    def edges(self):
        return self._edges

    def _create_cache(self, value):
        self._interior_angle = None
        self._edge_length = None
        self._apothem = None
        self._area = None
        self._perimeter = None

    @edges.setter
    def edges(self, value):
        self._create_cache(value)
        self._edges = value

    @property
    def circum_radius(self):
        return self._circum_radius

    @circum_radius.setter
    def circum_radius(self, value):
        self._create_cache(value)
        self._circum_radius = value

    @property
    def vertices(self):
        return self._edges

    @vertices.setter
    def vertices(self, value):
        self._create_cache(value)
        self._edges = value

    @property
    def interior_angle(self):
        if self._interior_angle is None:
            self._interior_angle = (self._edges - 2) * 180 / self._edges
        return self._interior_angle

    @property
    def edge_length(self):
        if self._edge_length is None:
            self._edge_length = 2 * self._circum_radius * math.sin(math.pi / self._edges)
        return self._edge_length

    @property
    def apothem(self):
        if self._apothem is None:
            self._apothem = self._circum_radius * math.cos(math.pi / self._edges)
        return self._apothem

    @property
    def area(self):
        if self._area is None:
            self._area = 0.5 * self._edges * self.edge_length * self.apothem
        return self._area

    @property
    def perimeter(self):
        if self._perimeter is None:
            self._perimeter = self._edges * self.edge_length
        return self._perimeter

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
