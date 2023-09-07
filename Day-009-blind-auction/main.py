from replit import clear
import art
#HINT: You can call clear() to clear the output in the console.

print(art.logo)

auctioneers = {}
is_bidding = True
while is_bidding:
    name = input("What is your name?: ")
    bid = input("What\'s your bid?: $")
    auctioneers[name] = bid
    should_continue = input(
        "Are there any other bidders? Type 'yes' or 'no'\n").lower()
    if should_continue == "no":
        is_bidding = False
    clear()

name = ""
bid = 0
for auctioneer in auctioneers:
    if int(auctioneers[auctioneer]) > bid:
        bid = int(auctioneers[auctioneer])
        name = auctioneer
print(f"The winner is {name} with a bid of ${bid}")
