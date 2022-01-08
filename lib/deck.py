class Deck:

    def __init__(self, cards): #creating a deck of cards
        self.cards = cards

    def rank_of_card_at(self, index): #checking the rank of a card in the deck
        if self.cards == []:
            return 0
        else:
            return self.cards[index].rank








# import ipdb; ipdb.set_trace() <---- this is similar to Ruby's binding.pry for debugging
