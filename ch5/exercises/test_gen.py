from cards import Card

def pytest_generate_tests(metafunc):
  if "start_state" in metafunc.fixturenames:
    metafunc.parametrize("start_state", ["done", "in prog", "todo"])

def test_start(cards_db, start_state):
  c = Card("Write a book", state=start_state)
  index = cards_db.add_card(c)
  cards_db.start(index)
  card = cards_db.get_card(index)
  assert card.state == "in prog"