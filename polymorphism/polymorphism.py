from functools import total_ordering
import operator


@total_ordering
class Mod:
    def __init__(self, value, modules):
        if not isinstance(modules, int):
            raise TypeError(f'modules must be integer number not {type(modules)}')
        elif modules < 0:
            raise ValueError('modules must be greater than 0')
        elif not isinstance(value, int):
            raise TypeError(f'values must be not {type(value)}')
        elif value < 0:
            raise ValueError('values must be greater than 0')
        self._modules = modules
        self._value = value % modules

    @property
    def modules(self):
        return self._modules

    @property
    def value(self):
        return self._value

    def _get_type(self, other):
        if isinstance(other, int):
            return other % self.modules
        elif isinstance(other, Mod) and self.modules == other.modules:
            return other.value
        raise NotImplemented

    def _operator(self, other, op, in_place=True):
        get_value = self._get_type(other)
        new_value = op(self.value, get_value)
        if in_place:
            self._value = new_value % self.modules
            return self
        else:
            return Mod(value=new_value, modules=self._modules)

    def __eq__(self, other):
        value = self._get_type(other)
        return self.value == value

    def __lt__(self, other):
        value = self._get_type(other)
        return self.value < value

    def __int__(self):
        return self.value

    def __add__(self, other):
        return self._operator(other=other, op=operator.add)

    def __iadd__(self, other):
        return self._operator(other=other, op=operator.add, in_place=True)

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        return self._operator(other=other, op=operator.sub)

    def __isub__(self, other):
        return self._operator(other=other, op=operator.sub, in_place=True)

    def __rsub__(self, other):
        return self - other

    def __mul__(self, other):
        return self._operator(other=other, op=operator.mul)

    def __imul__(self, other):
        return self._operator(other=other, op=operator.mul, in_place=True)

    def __rmul__(self, other):
        return self * other

    def __pow__(self, other):
        return self._operator(other=other, op=operator.pow)

    def __ipow__(self, other):
        return self._operator(other=other, op=operator.pow, in_place=True)

    def __rpow__(self, other):
        return self + other

    def __repr__(self):
        return f'Mod(value={self.value} modules={self.modules})'
