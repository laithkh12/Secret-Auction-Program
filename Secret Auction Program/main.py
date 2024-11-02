from art import logo
print(logo)

# TODO 4 : Compare bids in dictionary
def findHighestPrice(biddingDict):
    winner = ""
    highestBid = 0
    for bidder in biddingDict:
        bidAmount = biddingDict[bidder]
        if bidAmount > highestBid:
            highestBid = bidAmount
            winner = bidder
    print(f"The winner is {winner}, with a bid of {highestBid}")

# TODO 1 : Ask the user for input
# TODO 2 : Save data into dictionary {name:price}
# TODO 3 : Whether if new bids need to be added
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

