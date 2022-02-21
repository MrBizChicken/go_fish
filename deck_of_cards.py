import random
class Card:
    def __init__(self, suite, vaule):
        self.suite = suite
        self.vaule = vaule



    def get_card_value(self):
        return (self.suite, self.vaule)



class DeckOfCards:
    def __init__(self):
        self.suite = ["Heart", "Diamond", "Club", "Spade"]
        self.vaule = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
        self.deck = []
        self.discard_pile = []




    def make_deck(self):
        self.deck = []

        for s in range(len(self.suite)):
            for v in range(len(self.vaule)):
                self.deck.append(Card(self.vaule[v], self.suite[s]))


    def shuffle_deck(self):
        return random.shuffle(self.deck)




    def deal(self, players, num_to_deal):
        hands = []

        for i in range(players):
            hands.append([])

        for ntd in range(num_to_deal):
            for player in range(players):
                hands[player].append(self.draw(1))

        return hands



    def draw(self, ammount):
        hand = []

        for i in range(ammount):
            hand.append(self.deck.pop())

        return hand



    def discard(self, cards):
        for card in cards:
            self.discard_pile.append(card)



    def mix_discard(self):
        self.deck = self.deck + self.discard_pile
        self.discard_pile = []
