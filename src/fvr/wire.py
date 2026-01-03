import math

class awg:
  """Parameters of an AWG wire.
  """
  def __init__(self, number: int|str):
    """
    Args:
      number: AWG wire size, also '00', '000', '0000'
    """
    self.number = number
    self._number = self.num2int(number)

  @staticmethod
  def num2int(number: int|str):
    if isinstance(number, int):
      res = number
    elif number.isdigit():
      if number in ['00', '000', '0000']:
        res = 1 - len(number)
      else:
        res = int(number)
    else:
      raise ValueError(f"{number} is not a number.")
    return res

  @property
  def diameter(self):
    """The diameter of the AWG wire, mm"""
    return 0.127 * 92**((36-self._number)/39)

  @property
  def area(self):
    """The area of the AWG wire, mm²"""
    return math.pi/4*self.diameter**2

  def __str__(self):
    res = (
      '%s' % self.number + ' AWG\n'
      'A = %.4g' % self.area + ' mm²\n' +
      'd = %.4g' % self.diameter + ' mm\n')
    return res
