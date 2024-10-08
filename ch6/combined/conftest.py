import cards
import pytest


@pytest.fixture(scope="session")
def tmp_db_path(tmp_path_factory):
    """Path to temporary database"""
    return tmp_path_factory.mktemp("cards_db")


@pytest.fixture(scope="session")
def session_cards_db(tmp_db_path):
    """CardsDB"""
    db_ = cards.CardsDB(tmp_db_path)
    yield db_
    db_.close()


@pytest.fixture(scope="function")
def cards_db(session_cards_db, request, faker):
  """CardsDB object that's empty"""
  db = session_cards_db
  db.delete_all()
  
  # support for `@pytest.mark.num_cards(<some number>)`
  
  # random seed
  faker.seed_instance(101)
  m = request.node.get_closest_marker("num_cards")
  if m and len(m.args) > 0:
    num_cards = m.args[0]
    for _ in range(num_cards):
      db.add_card(
        cards.Card(summary=faker.sentence(), owner=faker.first_name())
      )
  return db