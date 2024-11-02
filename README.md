# 🎉 Bidding System 🎉

Welcome to the Bidding System! This program allows users to place bids and determines the highest bid along with the winner. It's a simple console application that showcases how to use dictionaries to store bid data and identify the winner based on user input.

---

## Features 🌟

- **User Input**: Enter your name and bid amount.
- **Continuous Bidding**: Accepts bids until the user indicates no more bidders.
- **Winner Announcement**: Displays the highest bid and the corresponding winner.

---

## How It Works 🔍

1. **Input**: The user is prompted to enter their name and bid amount.
2. **Storage**: Bids are stored in a dictionary with names as keys and bid amounts as values.
3. **Continuation**: Users can indicate if there are more bidders.
4. **Winner Determination**: A function identifies and displays the highest bid and the winner.

---

## Code Overview 📜

The main components of the code include:

- **Input Handling**: Collects user input for names and bid amounts.
- **Dictionary Usage**: Efficiently stores bid data.
- **Finding the Highest Bid**: A dedicated function (`findHighestPrice`) that compares bids to determine the winner.

### Code Snippet 💻

```python
from art import logo
print(logo)

def findHighestPrice(biddingDict):
    winner = ""
    highestBid = 0
    for bidder in biddingDict:
        bidAmount = biddingDict[bidder]
        if bidAmount > highestBid:
            highestBid = bidAmount
            winner = bidder
    print(f"The winner is {winner}, with a bid of {highestBid}")

bids = {}
continueBidding = True
while continueBidding:
    name = input("Enter your name: ")
    price = int(input("Enter your bid: $"))
    bids[name] = price
    shouldContinue = input("Are there any other bidders? Type 'yes' or 'no':\n").lower()

    if shouldContinue == 'no':
        continueBidding = False
        findHighestPrice(bids)
    elif shouldContinue == 'yes':
        print("\n" * 20)
```

## Requirements 📋
  Python: Version 3.x

## Usage 🚀
  1. Run the program in a Python environment.
  2. Follow the prompts to enter your name and bid amount.
  3. Indicate if there are more bidders or if the bidding has ended.
  4. Receive the result: The program will announce the winner!

## Contributing 🤝
  Feel free to fork the repository and submit pull requests for any improvements or features you would like to add!

## License 📄
  This project is licensed under the MIT License - see the LICENSE file for details.

Thank you for using the Bidding System! Happy bidding! 🎉

