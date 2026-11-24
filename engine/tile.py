# 34 types of tile in Japanese Riichi Mahjong

# Manzu: 0 - 8
# Pinzu: 9 - 17
# Souzu: 18 - 26
# Honors: 27 - 33

import random

TILE_TYPES = 34
COPIES_PER_TILE = 4
TOTAL_TILES = TILE_TYPES * COPIES_PER_TILE

def tile_to_string(tile:int) -> str:
    """Convert an integer tile into a readable string."""

    if 0 <= tile <= 8:
        return f"{tile + 1 }m"

    elif 9 <= tile <= 17:
        return f"{tile - 8}p"

    elif 18 <= tile <= 26:
        return f"{tile - 17}s"

    elif 27 <= tile <= 33:
        honors = ["East","South","West","North","White","Green","Red"]

        return honors[tile - 27]

    else:
        raise ValueError("Invalid tile number")

def create_deck() -> list[int]:
    """Create a complete 136-tile Mahjong deck."""


    deck = []

    for tile in range(TILE_TYPES):
        for _ in range(COPIES_PER_TILE):
            deck.append(tile)

    return deck

def shuffle_deck(deck: list[int]) -> None:
    """Shuffle the Mahjong deck in place"""

    random.shuffle(deck)

def deal_tiles(deck:list[int]) -> list[list[int]]:
    """Deal 13 tiles to reach to each of four players"""

    hands = []

    for player in range(4):
        hand = deck[:13]
        hands.append(hand)
        del deck[:13]

    return hands
