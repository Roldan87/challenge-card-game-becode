from typing import List
from utils.card import Card
from utils.player import Player, Deck


class Board:
    def __init__(self):
        self.players = []
        self.turn_count: int = 0
        self.active_cards = ""
        self.history_cards = []

    def start_game(self):
        num_players = int(input("Enter number of players (2 or 4): "))
        for number in range(num_players):
            new_player = Player()
            new_player.name = input("Enter player name: ")
            self.players.append(new_player)
        new_deck = Deck()
        new_deck.fill_deck()
        new_deck.shuffle()
        for item in new_deck.cards:
            print(item.value + item.icon)
        #new_deck.distribute(self.players)

