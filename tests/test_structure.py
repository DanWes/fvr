"""Test of structure module.

"""
import unittest
import fvr.structure

class TestStructureBeam(unittest.TestCase):
  def setUp(self):
    self.obj = fvr.structure.beam(1, 2, 3, 4, 5)
  def test_volume(self):
    self.assertEqual(self.obj.V, 12, 'incorrect volume after creation')
  def test_volume_a(self):
    self.obj.A = 6
    self.assertEqual(self.obj.V, 24, 'incorrect volume after changing A')
  def test_volume_l(self):
    self.obj.L = 7
    self.assertEqual(self.obj.V, 21, 'incorrect volume after changing L')

if __name__ == '__main__':
  unittest.main()
