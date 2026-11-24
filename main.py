from engine.tile import tile_to_string, TOTAL_TILES, create_deck,shuffle_deck,deal_tiles

def main():
    print("================")
    print(" Welcome to RiichiAI!")
    print("================")
    print("Japanese Mahjong AI project")
    print("Total physical tiles:",TOTAL_TILES)

    for tile in range(34):
        print(tile,"->",tile_to_string(tile))

    deck = create_deck()

    print("Deck size:", len(deck))
    print("First 10 tiles:", deck[:10])

    print("Before shuffle: ", deck[:10])

    shuffle_deck(deck)

    print("After shuffle: ", deck[:10])

    print("Deck size:", len(deck))
    print("Unique tile types:", len(set(deck)))

    for tile in range(34):
        count = deck.count(tile)
        if count != 4:
            print("Error:", tile_to_string(tile), count)

    hands = deal_tiles(deck)

    for player in range(4):
        print(f"Player {player + 1}:{len(hands[player])} tiles")

    print("Remaining tiles:", len(deck))


if __name__ == "__main__":
    main()