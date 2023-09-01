#  File: Poker.py

#  Description: We will simulate a regular Poker game otherwise known as the 5-Card Draw.
#  Regular Poker is played with a standard deck of 52 cards. 
#  Cards are ranked from high to low in the following order: Ace, King, Queen, Jack, 10, 9, 8, 7, 6, 5, 4, 3, 2.
#  The value of an Ace is higher than a King which is higher than a Queen and so on.
#  There are four suits - Spades, Hearts, Clubs, and Diamonds. The suits are of equal value.


#  Student Name: Mohamad Minoneshan

#  Partner Name: Mercedes Milke

#  Course Name: CS 313E

#  Unique Number: 52535

#  Date Created: 9/17/2022

#  Date Last Modified: 9/19/2022

from re import X
import sys, random

class Card (object):
    RANKS = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)

    SUITS = ('C', 'D', 'H', 'S')

  # constructor
    def __init__ (self, rank = 12, suit = 'S'):
        if (rank in Card.RANKS):
            self.rank = rank
        else:
            self.rank = 12

        if (suit in Card.SUITS):
            self.suit = suit
        else:
            self.suit = 'S'

  # string representation of a Card object
    def __str__ (self):
        if (self.rank == 14):
            rank = 'A'
        elif (self.rank == 13):
            rank = 'K'
        elif (self.rank == 12):
            rank = 'Q'
        elif (self.rank == 11):
            rank = 'J'
        else:
            rank = str (self.rank)
        return rank + self.suit

  # equality tests
    def __eq__ (self, other):
        return self.rank == other.rank

    def __ne__ (self, other):
        return self.rank != other.rank

    def __lt__ (self, other):
        return self.rank < other.rank

    def __le__ (self, other):
        return self.rank <= other.rank

    def __gt__ (self, other):
        return self.rank > other.rank

    def __ge__ (self, other):
        return self.rank >= other.rank

class Deck (object):
  # constructor
    def __init__ (self, num_decks = 1):
        self.deck = []
        for i in range(num_decks):
            for suit in Card.SUITS:
                for rank in Card.RANKS:
                    card = Card(rank, suit)
                    self.deck.append (card)

  # shuffle the deck
    def shuffle (self):
        random.shuffle(self.deck)

  # deal a card
    def deal (self):
        if (len(self.deck) == 0):
            return None
        else:
            return self.deck.pop(0)

class Poker (object):
  # constructor
    def __init__ (self, num_players = 2, num_cards = 5):
        self.deck = Deck()
        self.deck.shuffle()
        self.players_hands = []
        self.numCards_in_Hand = num_cards

    # deal the cards to the players
        for i in range(num_players):
            hand = []
            for j in range(self.numCards_in_Hand):
                hand.append(self.deck.deal())
            self.players_hands.append(hand)

  # simulate the play of poker
    def play (self):
    # sort the hands of each player and print
        for i in range (len(self.players_hands)):
            sorted_hand = sorted (self.players_hands[i], reverse = True)
            self.players_hands[i] = sorted_hand
            hand_str = ''
            for card in sorted_hand:
                hand_str = hand_str + str (card) + ' '
            print ('Player ' + str(i + 1) + ' : ' + hand_str)

    # determine the type of each hand and print
        hand_type = []	# create a list to store type of hand
        hand_points = []	# create a list to store points for hand

        '''for i in range (len(self.players_hands)):
            hand_type.append(self.is_royal(self.players_hands[i])[0])
            hand_points.append(self.is_royal(self.players_hands[i])[1])'''

    # determine winner and print

  # Royal Flush: A Royal Flush is made of 10, Jack, Queen, King, and Ace all of the same of suit.
  # determine if a hand is a royal flush
  # takes as argument a list of 5 Card objects
  # returns a number (points) for that hand
    def is_royal (self, hand):
        same_suit = True
        for i in range (len(hand) - 1):
            same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

        if (not same_suit):
            return 0, ''

        rank_order = True
        for i in range (len(hand)):
            rank_order = rank_order and (hand[i].rank == 14 - i)

        if (not rank_order):
            return 0, ''

        points = 10 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
        points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
        points = points + (hand[4].rank)

        return points, 'Royal Flush'
        
  # Straight Flush: A straight flush is made of 5 cards in numerical sequence but of the same suit.
  # determine if a hand is a straight flush
  # takes as argument a list of 5 Card objects
  # returns a number (points) for that hand
    def is_straight_flush (self, hand):
        same_suit = True
        for i in range (len(hand) - 1):
            same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

        if (not same_suit):
            return 0, ''

        rank_order = True
        for i in range (len(hand) - 1):
            rank_order = rank_order and (hand[i].rank == hand[i+1].rank + 1)
        

        if (not rank_order):
            return 0, ''

        points = 9 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
        points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
        points = points + (hand[4].rank)

        return points, 'Straight Flush'

  # Four of a Kind: In four of a kind, the hand must have four cards
  # of the same numerical rank, e.g. four aces or four queens.
  # determine if a hand is a four of a Kind
  # takes as argument a list of 5 Card objects
  # returns a number (points) for that hand
    def is_four_kind (self, hand):

        ranks = {}
        for i in range (len(hand)):
            if hand[i].rank not in ranks.keys():
                ranks[hand[i].rank] = 1
            else:
                ranks[hand[i].rank] += 1

        rank =  0
        four_kind = False    
        for key, value in ranks.items():
            if value == 4:
                four_kind = True
                rank = key
        
        if (not four_kind):
            return 0, ''

        four = []
        one = []
        for i in range(len(hand)):
            if hand[i].rank == rank:
                four.append(hand[i])
            else:
                one.append(hand[i])

        # c1, c2, c3, and c4 are the ranks of
        # the four of a kind cards and c5 is the side card.
        points = 8 * 15 ** 5 + (four[0].rank) * 15 ** 4 + (four[1].rank) * 15 ** 3
        points = points + (four[2].rank) * 15 ** 2 + (four[3].rank) * 15 ** 1
        points = points + (one[0].rank)

        return points, 'Four of a Kind'

  # Full House: For a full house, three of the cards must have the same numerical rank 
  # and the the two remaining cards must also have the same numerical rank
  # but obviously different rank than the other three.
  # determine if a hand is a full house
  # takes as argument a list of 5 Card objects
  # returns a number (points) for that hand
    def is_full_house (self, hand):
        ranks = {}
        for i in range (len(hand)):
            if hand[i].rank not in ranks.keys():
                ranks[hand[i].rank] = 1
            else:
                ranks[hand[i].rank] += 1
        three = 0
        two = 0
        if len(ranks) == 2:
            for key, value in ranks.items():
                if value == 3:
                    three = key
                elif value == 2:
                    two = key 
        
        if (three == 0 or two == 0):
            return 0, ''
        
        threes = []
        twos = []
        for i in range(len(hand)):
            if hand[i].rank == three:
                threes.append(hand[i])
            else:
                twos.append(hand[i])
        
        # c1, c2, and c3 are the ranks of the three cards having the same rank
        # and c4 and c5 are the ranks of the two remaining cards having the same rank.
        points = 7 * 15 ** 5 + (threes[0].rank) * 15 ** 4 + (threes[1].rank) * 15 ** 3
        points = points + (threes[2].rank) * 15 ** 2 + (twos[0].rank) * 15 ** 1
        points = points + (twos[1].rank)        
        
        return points, 'Full House'

  # Flush: In a flush there are 5 cards all of the same suit.
  # The numerical order does not matter.
  # determine if a hand is a flush
  # takes as argument a list of 5 Card objects
  # returns a number (points) for that hand
    def is_flush (self, hand):
        same_suit = True
        for i in range (len(hand) - 1):
            same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

        if (not same_suit):
            return 0, ''

        points = 6 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
        points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
        points = points + (hand[4].rank)       
        
        return points, 'Flush'        

  # Straight: In a straight hand, the 5 cards are in 
  # numerical order but are not all of the same suit.
  # determine if a hand is a straight
  # takes as argument a list of 5 Card objects
  # returns a number (points) for that hand
    def is_straight (self, hand):
        rank_order = True
        for i in range (len(hand) - 1):
            rank_order = rank_order and (hand[i].rank == hand[i+1].rank + 1)
        

        if (not rank_order):
            return 0, ''

        points = 5 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
        points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
        points = points + (hand[4].rank)       
        
        return points, 'Straight'  

  # Three of a Kind: In three of a kind hand,
  # there are 3 cards of the same rank and the other two are unrelated.
  # determine if a hand is a three of a kind
  # takes as argument a list of 5 Card objects
  # returns a number (points) for that hand
    def is_three_kind (self, hand):
        ranks = {}
        for i in range (len(hand)):
            if hand[i].rank not in ranks:
                ranks[hand[i].rank] = 1
            else:
                ranks[hand[i].rank] += 1
        three = ''

        for key, value in ranks.items():
            if value == 3:
                three = key

        if (three == ''):
            return 0, ''
        
        threes = []
        others = []
        for i in range(len(hand)):
            if hand[i].rank == three:
                threes.append(hand[i])
            else:
                others.append(hand[i])

        # c1, c2, and c3 are the ranks of the three cards of the same rank
        # and c4 and c5 are the ranks of the remaining cards where c4 has higher rank than c5.
        points = 4 * 15 ** 5 + (threes[0].rank) * 15 ** 4 + (threes[1].rank) * 15 ** 3
        points = points + (threes[2].rank) * 15 ** 2 + (others[0].rank) * 15 ** 1
        points = points + (others[1].rank)   
        
        return points, 'Three of a Kind'  

  # Two Pair: In a two pair hand there are two cards of a matching rank, 
  # another two cards of a different matching rank, and a fifth random card.
  # determine if a hand is a two pair
  # takes as argument a list of 5 Card objects
  # returns a number (points) for that hand
    def is_two_pair (self, hand):
        ranks = {}
        for i in range (len(hand)):
            if hand[i].rank not in ranks:
                ranks[hand[i].rank] = 1
            else:
                ranks[hand[i].rank] += 1
        two1 = 0
        two2 = 0

        for key, value in ranks.items():
            if value == 2 and two1 == 0:
                two1 = key
            elif two1 != 0 and value == 2:
                two2 = key
        if (two1 == 0 or two2 == 0):
            return 0, ''
        
        twos1 = []
        twos2 = []
        other = []
        for i in range(len(hand)):
            if hand[i].rank == two1:
                twos1.append(hand[i])
            elif hand[i].rank == two2:
                twos2.append(hand[i])
            else:
                other.append(hand[i])

        # c1 and c2 are the ranks of the first and higher ranking pair.
        # c3 and c4 are the ranks of the second and lower ranking pair.
        # c5 is the rank of the remaining side card.      
        points = 3 * 15 ** 5 + (twos1[0].rank) * 15 ** 4 + (twos1[1].rank) * 15 ** 3
        points = points + (twos2[0].rank) * 15 ** 2 + (twos2[1].rank) * 15 ** 1
        points = points + (other[0].rank)   
        
        return points, 'Two Pair'  

  # One Pair: In a one pair hand there are two cards of the
  # same rank and the other three cards are unrelated.
  # determine if a hand is one pair
  # takes as argument a list of 5 Card objects
  # returns the number of points for that hand
    def is_one_pair (self, hand):
        one_pair = False
        for i in range (len(hand) - 1):
            if (hand[i].rank == hand[i + 1].rank):
                one_pair = True
                break
        if (not one_pair):
            return 0, ''
        
        ranks = {}
        for i in range (len(hand)):
            if hand[i].rank not in ranks:
                ranks[hand[i].rank] = 1
            else:
                ranks[hand[i].rank] += 1
        two = 0
        for key, value in ranks.items():
            if value == 2 :
                two = key
        twos = []
        other = []
        for i in range(len(hand)):
            if hand[i].rank == two:
                twos.append(hand[i])
            else:
                other.append(hand[i])  

        # c1 and c2 are the ranks of the pair of cards having the same rank.
        # c3, c4, and c5 are the ranks of the side cards from highest to lowest rank.
        points = 2 * 15 ** 5 + (twos[0].rank) * 15 ** 4 + (twos[1].rank) * 15 ** 3
        points = points + (other[0].rank) * 15 ** 2 + (other[1].rank) * 15 ** 1
        points = points + (other[2].rank)

        return points, 'One Pair'

  # High Card: If none of the hands in a game qualified under the categories listed above then 
  # the hand having the highest ranking card wins.
  # determine if a hand is a high card
  # takes as argument a list of 5 Card objects
  # returns a number (points) for that hand
    def is_high_card (self,hand):

        points = 1 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
        points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
        points = points + (hand[4].rank)

        return points, 'High Card'

def main():
    # read number of players from stdin
    line = sys.stdin.readline()
    line = line.strip()
    num_players = int (line)
    if (num_players < 2) or (num_players > 6):
        return 0

    # create the Poker object
    game = Poker (num_players)

    # play the game
    game.play()

if __name__ == "__main__":
    main()
