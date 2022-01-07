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

def test_rank_of_card_at():
    card1 = Card("heart", "King", 13)
    card2 = Card("spade", "5", 5)
    card3 = Card("club", "8", 8)
    card4 = Card("diamond", "Queen", 12)
    cards = [card1, card2, card3]
    empty = []
    deck = Deck(cards)
    empty_deck = Deck(empty)

    assert deck.rank_of_card_at(0) == 13
    assert deck.rank_of_card_at(1) == 5
    assert deck.rank_of_card_at(2) == 8
    assert empty_deck.rank_of_card_at(0) == 0
