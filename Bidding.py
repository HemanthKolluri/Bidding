def Highest_Bidder(bids):
  highest_bid = 0
  winner=""
  for i in bids:
    A = bids[i]
    if A > highest_bid:
      highest_bid = A
      winner = i
  print(f"The winner is {winner} with Highest bid of {highest_bid}")


biding_finished = False
bids = {}
while not biding_finished:
    name = input("Your name:")
    amount = int(input("amount :$ "))
    bids[name] = amount
    X = input("are ther any other bidders: 'Yes'or 'No':").lower()
    if X == "no":
      biding_finished = True
      Highest_Bidder(bids)