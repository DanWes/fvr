import math

class beam:
  """Euler-Bernoulli beam.
  """
  def __init__(self, E, I, A, L, rho):
    """
    Args:
      E: Elastic modulus / Young's modulus
      I: Second moment of area of the beam's cross-section
      A: Cross-section
      L: Length
      rho: Density
    """
    self.E = E
    self.I = I
    self.A = A
    self.L = L
    self.rho = rho

  @property
  def V():
    return self.A * self.L

  @property
  def mu():
    """Mass per unit length (or the product of density and cross-section)"""
    return self.rho * self.A

  @property
  def m():
    return self.mu * self.L
    # return self.rho * self.V

  def eigenfrequency(self, n:int, support : str = 'fixed-free') -> float:
    r"""Natural frequencies of the beam.

    Args:
      n: Mode number (1 for first mode, ...)
      support: only 'fixed-free' atm.

    Returns:
      n-th natural frequencies of vibration
      !!! Currently only the first four frequencies can be calculated.

    Dynamic beam equation, the Euler-Lagrange equation, of an Euler-Bernoulli
    beam. The governing differential equation of motion, with :math:`\mu` the
    mass per unit length and :math:`\delta` the viscous damping per unit length.

    .. math::

      \frac{\partial^2}{\partial x^2} \left( EI(x)
        \frac{\partial^2 y}{\partial x^2} \right) +
        \mu(x)\frac{\partial^2 y}{\partial t^2} +
        \delta (x)\frac{\partial y}{\partial t} = f(x, t)

    Consider the undamped mode in bending vibration of the beam with uniform
    sectional property. The natural frequencies and mode shapes are obtained
    considering the homogeneous solution of the beam vibration equation. The
    Ansatz is

    .. math::

      y(x, t) = \phi(x)\sin(\omega t)

    with :math:`\phi` being mode shape functions and :math:`\omega` the angular
    natural frequency. Substituting gives

    .. math::

      \frac{\mathrm{d}^4\phi}{\mathrm{d}x^4} - a^4 \phi(x) = 0

    with :math:`a^4:=\mu\omega^2/(EI)` or

    .. math::

      a_n := \left(\frac{\mu\,\omega_n^2}{E\,I}\right)^{1/4}

    The general solution is

    .. math::

      \phi(x) = A\sin{ax} + B\cos{ax} + C\sinh{ax} + D\cosh{ax}

    with :math:`A,B,C,D` being integration constants and defined by the coundary
    conditions.

    ``fixed-free`` support (free vibration of a cantilever beam). Characteristic
    equations:

    .. math::

      \cos{aL}\,\cosh{aL}+1=0

    :math:`a_n` is a numerically solved value: :math:`a_1 L = 0.596864...\pi`,
    :math:`a_2 L = 1.49418...\pi`, :math:`a_3 L = 2.50025...\pi`, :math:`a_4 L =
    3.49999...\pi`, ...

    .. math::

      \omega_n = a_n^2\sqrt{\frac{E\,I}{\mu}} \quad,\quad
      f_n = \frac{a_n^2}{2\pi}\sqrt{\frac{E\,I}{\mu}}

    """
    a_nLopi = [0.596864, 1.49418, 2.50025, 3.49999]
    a_n = a_nLopi[n-1]*math.pi/self.L if n < len(a_nLopi) else 0
    return a_n**2*math.sqrt(self.E*self.I/self.mu)/(2*math.pi)
