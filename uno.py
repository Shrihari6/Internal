# uno 
# human vs human 
# computer vs human
# 1-9 * 4  + 2 * 4 + 4 + 4 = 52

import random

# Card class
class Card:
    def __init__(self, color, value):
        self.color = color
        self.value = value

    def __str__(self):
        return f"{self.color} {self.value}"

    def can_play_on(self, other):
        return self.color == other.color or self.value == other.value or self.color == "wild"

# Deck class
class Deck:
    colors = ["red", "yellow", "green", "blue"]
    values = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "skip", "reverse", "draw2"]
    wild_cards = ["wild", "wild_draw4"]

    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for color in self.colors:
            for value in self.values:
                self.cards.append(Card(color, value))
                if value != "0":  # Add two of each card except 0
                    self.cards.append(Card(color, value))
        for wild in self.wild_cards:
            for _ in range(4):
                self.cards.append(Card("wild", wild))
        random.shuffle(self.cards)

    def draw_card(self):
        return self.cards.pop() if self.cards else None

# Player class
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck, num=1):
        for _ in range(num):
            card = deck.draw_card()
            if card:
                self.hand.append(card)

    def play_card(self, card):
        self.hand.remove(card)

    def has_won(self):
        return len(self.hand) == 0

    def __str__(self):
        return f"{self.name}: " + ", ".join(str(card) for card in self.hand)

# UnoGame class
class UnoGame:
    def __init__(self, player_names):
        self.deck = Deck()
        self.players = [Player(name) for name in player_names]
        self.discard_pile = [self.deck.draw_card()]
        self.current_player_idx = 0
        self.direction = 1  # 1 for clockwise, -1 for counter-clockwise

    def start(self):
        for player in self.players:
            player.draw(self.deck, 7)
        self.play()

    def play(self):
        while True:
            current_player = self.players[self.current_player_idx]
            print(f"\n{current_player}'s turn. Top card: {self.discard_pile[-1]}")
            print(f"Your hand: {current_player}")

            playable_cards = [card for card in current_player.hand if card.can_play_on(self.discard_pile[-1])]
            if playable_cards:
                print("Playable cards:")
                for i, card in enumerate(playable_cards):
                    print(f"{i}: {card}")
                
                card_to_play_idx = self.get_card_choice(playable_cards)
                card_to_play = playable_cards[card_to_play_idx]
                current_player.play_card(card_to_play)
                self.discard_pile.append(card_to_play)
                print(f"{current_player.name} played {card_to_play}")
                self.handle_card_effect(card_to_play)
            else:
                print(f"{current_player.name} has no playable card and draws a card.")
                current_player.draw(self.deck)

            if current_player.has_won():
                print(f"\n{current_player.name} wins!")
                break

            self.current_player_idx = (self.current_player_idx + self.direction) % len(self.players)

    def get_card_choice(self, playable_cards):
        while True:
            try:
                choice = int(input("Choose a card to play (number): "))
                if 0 <= choice < len(playable_cards):
                    return choice
                else:
                    print("Invalid choice, try again.")
            except ValueError:
                print("Invalid input, please enter a number.")

    def handle_card_effect(self, card):
        if card.value == "skip":
            self.current_player_idx = (self.current_player_idx + self.direction) % len(self.players)
        elif card.value == "reverse":
            self.direction *= -1
        elif card.value == "draw2":
            next_player = self.players[(self.current_player_idx + self.direction) % len(self.players)]
            next_player.draw(self.deck, 2)
        elif card.value == "wild_draw4":
            next_player = self.players[(self.current_player_idx + self.direction) % len(self.players)]
            next_player.draw(self.deck, 4)
        # Implement color choice for wild cards if needed

# Example usage
if __name__ == "__main__":
    player_names = ["Alice", "Bob", "Charlie", "David"]
    game = UnoGame(player_names)
    game.start()
