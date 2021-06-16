from utils.card import Card


from utils.card import Card # COACHES' NOTES: Don't import stuff twice
from typing import List
import random


class Player:
    def __init__(self):
        self.cards = []
        self.turn_count = 0
        self.number_of_cards = 0
        self.history = []
        self.name = ""

    """def play():
        #randomly pick a Card in cards.

        #Add the Card to the Player's history.
        #Print: {PLAYER_NAME} {TURN_COUNT} played: {CARD_NUMBER} {CARD_SYMBOL_ICON}.
        #return the Card"""


class Deck:
    def __init__(self):
        self.cards = []

    def fill_deck(self):
        # method that will fill cards with a complete card game
        # (an instance of 'A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K' for each possible symbol [♥, ♦, ♣, ♠]).
        # Your deck should contain 52 cards at the end.
        suits = ["♥", "♦", "♣", "♠"]
        ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        colors = ["Red", "Black"]
        suit_index = 0
        rank_index = 0
        for item in suits:
            for item in ranks:
                # COACHES' NOTES: See comments in card.py
                poker_card = Card()
                poker_card.icon = suits[suit_index]
                poker_card.value = ranks[rank_index]
                self.cards.append(poker_card)
                rank_index += 1
            suit_index += 1
            rank_index = 0
        # COACHES' NOTES: Other functions have access to the self.cards variable, no need to
        # assign it to a new variable and return it.
        cards_deck = self.cards
        return cards_deck

    def shuffle(self):
        # method to shuffle all the list of cards:
        # COACHES' NOTES: Other functions have access to the self.cards variable, no need to
        # assign it to a new variable and return it.
        # return random.shuffle(self.cards)

        # COACHES' NOTES: No abbreviations -->shuffled_deck
        shuf_deck = random.shuffle(self.fill_deck())
        return shuf_deck

    def distribute(self, players: List[Player]):
        # that will take a list of Player as parameter and will distribute the cards evenly between all the players
        # COACHES' NOTES:  No need to use player_index.
        # for player in players:
        #   player.cards....

        player_index = 0
        card_index = 0
        for item in players:
            players[player_index].cards.append(self.cards[card_index])
            card_index += 1

            # COACHES' NOTES: Difficult to understand what's going gon here at first glance
            # A variable called cards_per_player = self.cards / (len(players)) would have been perfect.
            # You are looping through the players using a for loop but using player_index
            # to get the players. Use the for loop to your advantage ;)
            if len(players[player_index].cards) == self.cards / (len(players)):
                player_index += 1
        return players
