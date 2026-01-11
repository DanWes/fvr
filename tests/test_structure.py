"""Test of structure module.

"""
import unittest
import fvr.structure

class TestStructureBeam(unittest.TestCase):
  def setUp(self):
    self.obj = fvr.structure.Beam(1, 2, 3, 4, 5)

  def test_volume(self):
    self.assertEqual(self.obj.V, 12, 'incorrect volume after creation')

  def test_volume_a(self):
    self.obj.A = 6
    self.assertEqual(self.obj.V, 24, 'incorrect volume after changing A')

  def test_volume_l(self):
    self.obj.L = 7
    self.assertEqual(self.obj.V, 21, 'incorrect volume after changing L')

  def test_mu(self):
    self.assertEqual(self.obj.mu, 15, 'incorrect specific mass after creation')

  def test_m(self):
    self.assertEqual(self.obj.m, 60, 'incorrect mass after creation')

  def test_eigenfrequency(self):
    self.assertEqual(
      self.obj.eigenfrequency(1), 0.012770856732837836,
      'incorrect eigen-frequency after creation')

class TestStructureTubeBuckling(unittest.TestCase):
  def setUp(self):
    self.obj = fvr.structure.TubeBuckling(1, 0.2, 3, h=4)

  def test_force(self):
    self.assertEqual(
      self.obj.force(), 1.8518518518518516,
      'incorrect buckling force after creation')

  def test_pressure(self):
    self.assertEqual(
      self.obj.pressure(), 0.6172839506172838,
      'incorrect buckling force after creation')

  def test_stress(self):
    self.assertEqual(
      self.obj.stress(), 0.46296296296296297,
      'incorrect buckling force after creation')

if __name__ == '__main__':
  unittest.main()
