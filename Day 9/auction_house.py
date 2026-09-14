from art import logo

# prints the logo
print(logo)

# create dictionaries for the auction users and bid amounts
current_bids = {}

current_name = {}

highest_bid = 0

# starts the auction loop
while True: 

    # asks for the users and bids
    name = str(input("Enter your name: "))
    if name == "":
        print("You must enter a name to continue!")
        continue

    # use try with except to avoid value error crashes and validate inputs
    try:
        bid = float(input("Enter your bid: "))
    except ValueError:
        print("Only numbers are allowed!")
        continue

    # takes the current bid from the dictionary and hands it back to bidder
    current_bids[name] = (bid)
    current_name = name
    print(f"Hello, {name}, your bid is: \n ${bid:.2f}")

    # truth gate for yes/no option to continue or complete auction
    while True:

        # asks for another bidder, yes/no option
        continue_auction = input("Does someone else need to bid?\n" \
                                    "Enter 'yes' to continue 'no' to run auction:\n")
        if continue_auction in ['yes', 'no']:
            break
        print("Invalid, try again!")

    # continues the bidding process
    if continue_auction == "yes":
        print("\n" * 100)
        continue

    # starts the auction and displays the winning amount
    elif continue_auction == "no":
        for bidder_name, bidder_amount in current_bids.items():
            print(f"{bidder_name} bids: ${bidder_amount:.2f}")
            highest_bid = max(current_bids.values())
        break
    else:
        print("Type 'yes' for more bidders or 'no' to complete the auction.")
        break 

# checks the dictionary for the highest bid and declares a winner
for name, current_bid in current_bids.items():
    if current_bid >= highest_bid:
        print(f"Highest bid is: ${highest_bid:.2f}\n{name}... you win!")
        break
 