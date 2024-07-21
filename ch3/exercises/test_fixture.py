import pytest
import random
import numpy as np

@pytest.fixture()
def get_even():
  """Return an even number from 0 to 100"""
  return random.randrange(0, 101, 2)


@pytest.fixture()
def get_odd():
  """Return an odd number from 0 to 100"""
  return random.randrange(1, 100, 2)


@pytest.fixture(scope="module")
def get_matrix():
  """Create a matrix 3 * 3"""
  data = np.random.rand(3, 3)
  print("\nHI")
  yield data
  print("\nEND")

def test_is_even(get_even):
  assert get_even % 2 == 0
  
def test_is_odd(get_odd):
  assert get_odd % 2 != 0

def test_check_shape(get_matrix):
  assert get_matrix.shape == (3, 3)
  
def test_check_inverse(get_matrix):
  inverse_matrix = np.linalg.inv(get_matrix)
  inverse_matrix * get_matrix == np.eye(3, 3) 
  