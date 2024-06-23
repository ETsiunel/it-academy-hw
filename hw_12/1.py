"""Homework_12"""
# # # Колода карт # # #
# Напишите программу, которая содержит список карт, умеет их перемешивать
# и позволяет пользователю достать карту из колоды по ее номеру.
# Всего в колоде 54 карты.
# Класс Card содержит список номеров карт и список мастей.
import random


class Card:
    """Определение класса карта"""
    number_list = ['2', '3', '4', '5', '6', '7', '8',
                   '9', '10', 'J', 'Q', 'K', 'A']
    mast_list = ['Hearts', 'Diamonds', 'Clubs', 'Spades', 'Jokers']

    def __init__(self, number, mast):
        self.number = number
        self.mast = mast

    def __repr__(self):
        return f"{self.mast} {self.number}"


class CardsDeck:
    """Определение класса колода"""
    def __init__(self):
        self.cards = self.create_deck()

    def create_deck(self):
        deck = []
        for mast in Card.mast_list[:-1]:
            for number in Card.number_list:
                deck.append(Card(number, mast))
        deck.append(Card('Joker', 'Red'))
        deck.append(Card('Joker', 'Black'))
        return deck

    def shuffle(self):
        random.shuffle(self.cards)

    def get(self, card_number):
        if 1 <= card_number <= len(self.cards):
            return self.cards[card_number - 1]
        raise ValueError("Card number must be between 1 and 54")


deck = CardsDeck()
deck.shuffle()

card_number = int(input('Выберите карту из колоды в 54 карты: '))
card = deck.get(card_number)
print(f'You card is: {card}')

card_number = int(input('Выберите карту из колоды в 54 карты: '))
card = deck.get(card_number)
print(f'You card is: {card}')
