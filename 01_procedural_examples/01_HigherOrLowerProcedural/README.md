# 🎮 Game Description
- The game randomly selects 8 cards from a standard deck of 52 cards.
- The first card is shown to the player.
- The player is asked: "Will the next card be higher or lower in value?"
- The next card is then revealed:
- If the guess is correct, the player earns 20 points.
- If the guess is incorrect, they lose 15 points.
- If the next card is of equal value (e.g., two 5s), it counts as incorrect.

## 🃏 How Cards Are Represented in the Code
Each card is represented as a dictionary with the following structure:

```python
{
  'rank': 'Jack',
  'suit': 'Clubs',
  'value': 11
}
```

- 'rank': Name of the card (e.g., 'Ace', '2', ..., 'King').
- 'suit': One of the four suits ('Hearts', 'Diamonds', 'Clubs', 'Spades').
- 'value': A numerical representation used for comparison (1–13 for Ace to King).
- The deck is a list of 52 such dictionaries.

## 🔄 Game Flow
- Create and shuffle the full deck of cards.
- Pick 8 cards randomly from the shuffled deck.
- Show the first card to the player.

For each of the remaining 7 cards:
- Ask the player for a prediction: "higher" or "lower".
- Reveal the next card.
- Compare its 'value' to the previous card’s 'value'.
- Adjust the score based on whether the guess was correct.