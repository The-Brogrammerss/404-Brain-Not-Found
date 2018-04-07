



listy1 = [1, 2, 7, 6]
listy2 = [1, 2, 4, 7]
whatever = [abs(x - y) for x in listy1 for y in listy2 if x == y]
print("whatever:", whatever)
W = sum(whatever) / len(whatever)
print(W)

