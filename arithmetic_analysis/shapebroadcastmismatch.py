from __future__ import annotations
from numpy import array, cos, cross, float64, radians, sin
from numpy.typing import NDArray
def polar_force(magnitude: float, angle: float, radian_mode: bool = False) -> list[float]:
    if radian_mode:
        return [magnitude * cos(angle), magnitude * sin(angle)]
    return [magnitude * cos(radians(angle)), magnitude * sin(radians(angle))]


def in_static_equilibrium(forces: NDArray[float64], location: NDArray[float64], eps: float = 10**-1) -> bool:
    moments: NDArray[float64] = cross(location, forces)
    sum_moments: float = sum(moments)
    return abs(sum_moments) < eps

if __name__ == "__main__":
    forces = array([polar_force(718.4, 180 - 30), polar_force(879.54, 45), polar_force(100, -90),])
    location: NDArray[float64] = array([[0, 0], [0, 0], [0, 0]])
    assert in_static_equilibrium(forces, location)
    forces = array([polar_force(30 * 9.81, 15), polar_force(215, 180 - 45), polar_force(264, 90 - 30),])
    location = array([[0, 0], [0, 0], [0, 0]])
    assert in_static_equilibrium(forces, location)
    forces = array([[0, -2000], [0, -1200], [0, 15600], [0, -12400]])
    location = array([[0, 0], [6, 0], [10, 0], [12, 0]])
    assert in_static_equilibrium(forces, location)
    import doctest
    doctest.testmod()
"""
<stdin>:2: DeprecationWarning: Arrays of 2-dimensional vectors are deprecated. Use arrays of 3-dimensional vectors instead. (deprecated in NumPy 2.0)
Traceback (most recent call last):
  File "<stdin>", line 9, in <module>
  File "<stdin>", line 2, in in_static_equilibrium
  File "/usr/local/lib/python3.12/dist-packages/numpy/_core/numeric.py", line 1662, in cross
    shape = broadcast(a[..., 0], b[..., 0]).shape
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ValueError: shape mismatch: objects cannot be broadcast to a single shape.  Mismatch is between arg 0 with shape (3,) and arg 1 with shape (4,).
"""
