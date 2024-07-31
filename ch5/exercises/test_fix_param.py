import pytest
from cards import Card


@pytest.fixture(params=["done", "in prog", "todo"])
def start_state(request):
  return request.param

def test_start(cards_db, start_state):
  c = Card("write a book", state=start_state)
  index = cards_db.add_card(c)
  cards_db.start(index)
  card = cards_db.get_card(index)
  assert card.state == "in prog"