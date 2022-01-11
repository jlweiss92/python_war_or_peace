class Deck:

    def __init__(self, cards): #creating a deck of cards.
        self.cards = cards

    def rank_of_card_at(self, index): #checking the rank of a card in the deck.
        if self.cards == []:
            return 0
        else:
            return self.cards[index].rank

    def high_ranking_cards(self): # Checking for cards that rank above 10.
        high = []
        for card in self.cards: #@cards.each do |card|
            if card.rank > 10: # The if statement is the same
                high.append(card) # This is the shovel method if the condition is met
        return high # This is the return value we are looking for

    #below is how I solved this in Ruby as a reference

    #def high_ranking_cards
        #high_ranked_cards = []
        #@cards.each do |card|
            #if card.rank > 10
            #high_ranked_cards << card
            #end
        #end
        #high_ranked_cards
    #end

    def percent_high_ranking(self): # Checking in a deck the percentage of cards that are high ranking cards (above 10)
        if len(self.high_ranking_cards()) == 0:
             return 0 # edge case for if there are no cards
        else:
            return len(self.high_ranking_cards())\
            / len(self.cards)\
            * 100

    def remove_card(self): # remove card from deck
        return self.cards.pop(0)

    def add_card(self, card): # Add card to deck
        self.cards.append(card)

# import ipdb; ipdb.set_trace() <---- this is similar to Ruby's binding.pry for debugging
