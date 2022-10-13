# The trick to realise here is that the two groups don't have to be the same size.
# Instead let's split them into a big pile of 90 coins and a small pile of 10 coins.
# We don't know how many heads are in either pile, it couĺd be anywhere from 0 to 10.
# Let's say there are n heads in the large pile. That leaves 10-n heads in the small pile.
# If we turn over all of the coins in the small pile we get 10-(10-n) heads which simplifies to n.
# Therefore both piles will have the same number of heads as each other,
# even though we don't know how many (if any) that is.
#

# ( 0 tail) (1 head)
def heads_tails(h, t):
    head = "1" * h

    tail = "0" * t

    coins = head + tail

    print(coins)

    list1 = coins[:t]
    list2 = coins[t:]
    print(list1)
    print(list2)

    ans = []
    for i in list2:
        if i == "0":
            ans.append(1)
        else:
            ans.append(0)

    print(ans)


# Num_Heads = 10
# Num_Tails = 90

Num_Heads = int(input("Enter number of heads"))
Num_Tails = int(input("Enter number of tails"))
heads_tails(Num_Heads, Num_Tails)

