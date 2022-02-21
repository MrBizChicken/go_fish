from deck_of_cards import *
import random
# class Go_fish:
#     def __init__(self):
#
#         cards = DeckOfCards()
#         cards.make_deck()
#         cards.shuffle_deck()
#         hands = cards.deal(2, 26)
#         self.hand1 = hands[0]
#         self.hand2 = hands[1]
#
#
#     def compare(self):
#         hand1 = set(self.hand1)
#         hand2 = set(self.hand2)
#         if random.choice(hand1) == hand2:
#             self.hand1.append(hand2)
#         else:
#             self.hand2.append(cards.draw(1))
#
#         if random.choice(hand2) == hand1:
#             self.hand2.append(hand1)
#
#         else:
#             self.hand1.append(cards.draw(1))
#
#     def play(self):
#         while len(cards.deck) > 0:
#             self.compare()
#         if  len(cards.deck) == 0:
#             if len(self.hand1) < len(self.hand2):
#                 print("player 1 won!")
#             else:
#                 print("player 2 won!")
# g = Go_fish()
#
# g.play()
#     from deck_of_cards import *

class Go_fish:
    def __init__(self):


        deck_of_cards = DeckOfCards()
        deck_of_cards.make_deck()
        deck_of_cards.shuffle_deck()
        hands = deck_of_cards.deal(2, 6)
        self.hand1 = hands[0]
        self.hand2 = hands[1]
        self.deck = deck_of_cards.deck




    def compare(self):
        hand1 = set(self.hand1)
        hand2 = set(self.hand2)
        if random.choice(hand1) == hand2:
            self.hand1.append(hand2)
        else:
            self.hand2.append(deck_of_cards.draw(1))

        if random.choice(hand2) == hand1:
            self.hand2.append(hand1)

        else:
            self.hand1.append(deck_of_cards.draw(1))


    def play_game(self):
        while len(self.deck) > 0:
            self.compare()
        if  len(self.deck) == 0:
            if len(self.hand1) < len(self.hand2):
                print("player 1 won!")
            else:
                print("player 2 won!")
w = Go_fish()
w.play_game()
