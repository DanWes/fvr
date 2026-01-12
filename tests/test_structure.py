"""Test of structure module.

"""
import pytest
import fvr.structure

class TestBeam:
  @pytest.fixture(autouse=True)
  def obj(self):
    self.obj = fvr.structure.Beam(1, 2, 3, 4, 5)

  def test_beam_volume(self):
    assert self.obj.V == 12

  def test_volume_a(self):
    self.obj.A = 6
    assert self.obj.V == 24

  def test_volume_l(self):
    self.obj.L = 7
    assert self.obj.V == 21

  def test_mu(self):
    assert self.obj.mu == 15

  def test_m(self):
    assert self.obj.m == 60

  def test_eigenfrequency(self):
    assert self.obj.eigenfrequency(1) == 0.012770856732837836

class TestTubeBuckling:
  @pytest.fixture(autouse=True)
  def obj(self):
    self.obj = fvr.structure.TubeBuckling(1, 0.2, 3, h=4)

  def test_force(self):
    assert self.obj.force() == 1.8518518518518516

  def test_pressure(self):
    assert self.obj.pressure() == 0.6172839506172838

  def test_stress(self):
    assert self.obj.stress() == 0.46296296296296297
