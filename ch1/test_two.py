def test_falling():
  assert (1, 2, 3) == (3, 2, 1)

def test_passing_1():
  assert 1 in [2, 3, 4, 5]

def test_passing_2():
  assert 2 < 1

def test_passing_3():
  assert "fizz" not in "fizzbuzz"
