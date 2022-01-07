import pytest
from lib.card import *

def test_it_exists():
    card = Card("heart", "King", 13)
    assert card.suit == "heart"
    assert card.value == "King"
    assert card.rank == 13
