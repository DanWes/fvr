from fvr.typing import FloatArray

def area(vertices: FloatArray) -> float:
  r"""Determine the area of a simple polygon.

  Args:
    vertices: List of points, pair of x and y: "[[x1, y1], [x2, y2], ...]"
  
  Shoelace formula, Gauss's area formula, surveyor's formula

  https://en.wikipedia.org/wiki/Shoelace_formula
  """
  count = len(vertices)  # of corners
  result = 0.0
  for i in range(count):
    j = (i + 1) % count
    result += vertices[i][0] * vertices[j][1] - vertices[i][1] * vertices[j][0]
  result = abs(result) / 2.0
  return result
