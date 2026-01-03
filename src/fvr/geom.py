import re
from fvr.typing import FloatArray

class polygon:
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
      >>> fvr.geom.polygon([[0, 0], [0, 1], [1, 1], [1, 0]]).area
      >>> fvr.geom.polygon('[[0, 0], [0, 1], [1, 1], [1, 0]]').area

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
