from typing import Union, Sequence
from numpy import array, ndarray


class Point(ndarray):
    def __new__(cls, input_array: Union[Sequence[float], ndarray]):
        arr = array(input_array[:2], dtype=float)
        obj = arr.view(cls)
        return obj

    def __array_finalize__(self, obj):
        if obj is None:
            return
        if self.shape != (2,):
            self.resize((2,), refcheck=False)

    @property
    def x(self) -> float:
        return self[0]

    @x.setter
    def x(self, value: float):
        self[0] = value

    @property
    def y(self) -> float:
        return self[1]

    @y.setter
    def y(self, value: float):
        self[1] = value
