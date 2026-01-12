"""Test of geom2d module.

"""
import numpy as np
import fvr.geom2d

def test_vertex_obj():
  np.testing.assert_equal(
    fvr.geom2d.Vertex(1, 2), np.array([1, 2, 1]),
    'incorrect object after creation')

def test_vertex_x():
  np.testing.assert_equal(
    fvr.geom2d.Vertex(1, 2).x, 1, 'incorrect x after creation')

def test_vertex_y():
  np.testing.assert_equal(
    fvr.geom2d.Vertex(1, 2).y, 2, 'incorrect y after creation')

def test_vertex_w():
  np.testing.assert_equal(
    fvr.geom2d.Vertex(1, 2).w, 1, 'incorrect w after creation')
