import pytest
from lib.card import *
from lib.deck import *


def test_it_exists():
    card1 = Card("heart", "King", 13)
    card2 = Card("spade", "King", 13)
    card3 = Card("club", "King", 13)
    card4 = Card("diamond", "King", 13)
    cards = [card1, card2, card3]
    deck = Deck(cards)
    assert len(deck.cards) == 3
