import math

class awg:
  """AWG wire.
  """
  def __init__(self, number: int|str):
    """Determine parameters for a given AWG wire size.

    Args:
      number: AWG wire size, also '00', '000', '0000'
    """
    self.number = number
    self.num2int()

  def num2int(self):
    if isinstance(self.number, int):
      self._number = self.number
    elif self.number.isdigit():
      if self.number in ['00', '000', '0000']:
        self._number = 1 - len(self.number)
      else:
        self._number = int(self.number)
    else:
      raise ValueError

  @property
  def diameter(self):
    """The diameter for a given AWG wire size in mm"""
    return 0.127 * 92**((36-self._number)/39)

  @property
  def area(self):
    """The area for a given AWG wire size in mm²"""
    return math.pi/4*self.diameter**2

  def __str__(self):
    res = (
      '%s' % self.number + ' AWG\n'
      'A = %.4g' % self.area + ' mm²\n' +
      'd = %.4g' % self.diameter + ' mm\n')
    return res
