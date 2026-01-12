import re
import numpy as np
from fvr.typing import FloatArray

class Vertex(np.ndarray):
  """Point in 2d space using homogeneous coordinates."""

  def __init__(cls, x=0, y=0):
    obj = np.asarray([x, y, 1]).view(cls)

  @property
  def x(self):
    return self[0]

  @property
  def y(self):
    return self[1]


class Polygon:
  r"""Properties of a simple polygon.
  """

  def __init__(self, vertices: FloatArray|str):
    r"""
    Args:
      vertices: List of points, pair of x and y: ``[[x1, y1], [x2, y2], ...]``
    """
    if isinstance(vertices, str):
      vertices = self.str2arr(vertices)
    self.vertices = vertices

  @staticmethod
  def str2arr(vertices: str) -> list:
    strm = re.match(r'\[.*\]', ''.join(vertices))
    if strm and strm.group():
      return eval(strm.group())

  @property
  def area(self) -> float:
    r"""Determine the area of a simple polygon.

    Example:
      >>> polygon([[0, 0], [0, 1], [1, 1], [1, 0]]).area
      1.0
      >>> polygon('[[0, 0], [0, 1], [1, 1], [1, 0]]').area
      1.0

    Shoelace formula, Gauss's area formula, surveyor's formula

    https://en.wikipedia.org/wiki/Shoelace_formula
    """
    count = len(self.vertices)  # of corners
    result = 0.0
    for i in range(count):
      j = (i + 1) % count
      result += self.vertices[i][0] * self.vertices[j][1] - \
        self.vertices[i][1] * self.vertices[j][0]
    result = abs(result) / 2.0
    return result
