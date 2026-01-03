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

class tube:
  r"""\
  Long thin circular tube uniformly loaded with external pressure.

  Elemental ring of unit width (h)

  IMPORTANT: Can be used as long as the corresponding compressive stress does
  not exeed the proportional limit of the material.

  :math:`I = \frac{h^3}{12}`

  References:
    - Timoshenko, Stephen P., and James M. Gere. 1961. Theory of Elastic
      Stability. 2nd ed. New York: McGraw-Hill Book. ch. 7.

  """

  def __init__(self, r, h, E, nu):
    """\
    Args:
      r: mean radius (r_a + r_i)/2
      h: thickness
      E: Young's modulus
      nu: Poisson's ratio
    """
    self.r = r
    self.h = h
    self.E = E
    self.nu = nu

  def critical_buckling_force(self):
    r"""Critical buckling value of the compressive force.

    A long circular tube uniformly compressed by external pressure.

    .. math::

      f_{cr} = \frac{E h^3}{4 \, (1 - \nu^2) \, r^2}

    References:
      - Timoshenko, Stephen P., and James M. Gere. 1961. Theory of Elastic
        Stability. 2nd ed. New York: McGraw-Hill Book. p. 289.

    """
    return (self.E * self.h**3) / (4 * (1 - self.nu**2) * self.r**2)

  def critical_buckling_pressure(self):
    r"""Critical buckling value of the compressive pressure.

    A long circular tube uniformly compressed by external pressure.

    .. math::

      q_{cr} = f_{cr}/r

    .. math::

      q_{cr} = \frac{E}{4 \, (1 - \nu^2)} \left(\frac{h}{r}\right)^3

    References:
      - Timoshenko, Stephen P., and James M. Gere. 1961. Theory of Elastic
        Stability. 2nd ed. New York: McGraw-Hill Book. p. 289.

    """
    return self.E / (4 * (1 - self.nu**2)) * (self.h / self.r)**3

  def critical_buckling_stress(self):
    r"""Critical buckling stress of a long thin circular tube uniformly
    compressed by pressure.

    .. math::

      \sigma_{cr} = f_{cr}/h

    .. math::

      \sigma_{cr} = \frac{E}{1 - \nu^2} \left(\frac{h}{2r}\right)^2

    References:
      - Timoshenko, Stephen P., and James M. Gere. 1961. Theory of Elastic
        Stability. 2nd ed. New York: McGraw-Hill Book. p. 293.

    """
    return self.E / (1 - self.nu**2) * (self.h / (2 * self.r))**2
