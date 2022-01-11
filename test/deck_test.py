import pytest
from lib.card import *
from lib.deck import *


def test_it_exists(): #Testing that the deck of cards exist
    card1 = Card("heart", "King", 13)
    card2 = Card("spade", "King", 13)
    card3 = Card("club", "King", 13)
    card4 = Card("diamond", "King", 13)
    cards = [card1, card2, card3]
    deck = Deck(cards)
    assert len(deck.cards) == 3

def test_rank_of_card_at(): #Testing the rank of a card in the deck
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

def test_high_ranking_cards(): # Testing for cards in a deck that rank above 10
    card1 = Card("heart", "King", 13)
    card2 = Card("spade", "5", 5)
    card3 = Card("club", "8", 8)
    card4 = Card("diamond", "Queen", 12)
    cards = [card1, card2, card3, card4]
    deck = Deck(cards)

    assert deck.high_ranking_cards()[0] == card1
    assert deck.high_ranking_cards()[1] == card4
    assert len(deck.high_ranking_cards()) == 2

def test_percent_high_ranking(): # Testing to see the percentage of high ranking cards in a deck
    card1 = Card("heart", "King", 13)
    card2 = Card("spade", "5", 5)
    card3 = Card("club", "8", 8)
    card4 = Card("diamond", "Queen", 12)
    cards = [card1, card2, card3, card4]
    deck = Deck(cards)

    assert deck.percent_high_ranking() == 50.0
    empty = []
    empty_deck = Deck(empty)
    assert empty_deck.percent_high_ranking() == 0 # Tests if deck is empty that it returns a 0
    card_1 = Card("heart", "10", 10)
    card_2 = Card("spade", "5", 5)
    card_3 = Card("club", "8", 8)
    card_4 = Card("diamond", "3", 3)
    different_cards = [card_1, card_2, card_3, card_4]
    no_high_rank = Deck(different_cards)
    assert no_high_rank.percent_high_ranking() == 0 # Tests that if no cards are high ranking that it returns a 0
