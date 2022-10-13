# The trick to realise here is that the two groups don't have to be the same size.
# Instead let's split them into a big pile of 90 coins and a small pile of 10 coins.
# We don't know how many heads are in either pile, it couĺd be anywhere from 0 to 10.
# Let's say there are n heads in the large pile. That leaves 10-n heads in the small pile.
# If we turn over all of the coins in the small pile we get 10-(10-n) heads which simplifies to n.
# Therefore both piles will have the same number of heads as each other,
# even though we don't know how many (if any) that is.
#

# ( 0 tail) (1 head)
head = "1"*10

tail= "1"*90


coins=head+tail

print(coins)
