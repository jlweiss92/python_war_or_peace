class Deck:

    def __init__(self, cards):
        self.cards = cards

    def rank_of_card_at(self, index):
        if self.cards == []:
            return 0
        else:
            return self.cards[index].rank
