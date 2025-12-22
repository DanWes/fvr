import sys
import pathlib
import importlib


__version__ = "2025.12.22"


def rundir():
  """
  returns the path of the script running or the current working directory.
  """
  if sys.argv[0] == '-c':
    return pathlib.Path.cwd()
  return pathlib.Path(sys.argv[0]).parent
  # return pathlib.Path(sys.argv[0]).parent.resolve()

def reload(module):
  importlib.reload(module)

def printdoc(object):
  res = object.__doc__
  print(res)
