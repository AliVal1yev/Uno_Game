from random import shuffle

from constants import COLOR, CARD
from cards import Card


__all__ = (
    "generate_deck"
)

def _generate_numeric_cards():
    numerics = [ ]

    for c in COLOR.MAIN_COLORS:
        card = Card(c, "0", CARD.NUMERIC)
        numerics.append(card)

        for t in range(1, 10): # 0-9
            card = Card(c, t, CARD.NUMERIC)
            double_cards = [card] * 2
            numerics.extend(double_cards)

    return numerics


def _generate_action_cards():
    actions = [ ]

    for c in COLOR.MAIN_COLORS:
        for tp in CARD.ACTION_CARD_TYPES:
            card = Card(c, tp, CARD.ACTION)
            double_cards = [card] * 2
            actions.extend(double_cards)

    return actions


def _generate_wild_cards():
    wilds = [ ]

    for tp in CARD.WILD_CARD_TYPES:
        card = Card("black", tp, CARD.WILD)
        double_cards = [card] * 4
        wilds.extend(double_cards)

    return wilds


def generate_deck():
    numeric_cards = _generate_numeric_cards()
    action_cards = _generate_action_cards()
    wild_cards = _generate_wild_cards()
    deck = numeric_cards + action_cards + wild_cards
    # deck = action_cards
    shuffle(deck)
    return deck