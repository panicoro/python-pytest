import cards
import pytest
from packaging.version import parse


@pytest.mark.xfail(
  parse(cards.__version__).major < 2,
  reason="Card < comparason not supported in 1.x"
)
def test_less_than():
  c1 = cards.Card("a task")
  c2 = cards.Card("b task")
  assert c1 < c2

@pytest.mark.xfail(
  parse(cards.__version__).major < 2,
  reason="Card < comparason not supported in 1.x"
)
def test_less_than():
  c1 = cards.Card("a task")
  c2 = cards.Card("b task")
  assert c1 < c2

@pytest.mark.xfail(reason="XPASS demo")
def test_xpass():
  c1 = cards.Card("a task")
  c2 = cards.Card("a task")
  assert c1 == c2
  
@pytest.mark.xfail(reason="strict demo", strict=True)
def test_xfail_strict():
  c1 = cards.Card("a task")
  c2 = cards.Card("a task")
  assert c1 == c2
