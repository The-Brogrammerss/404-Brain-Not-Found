



listy1 = [1, 2, 7, 6]
listy2 = [1, 2, 4, 7]
whatever = [abs(x - y) for x in listy1 for y in listy2 if x == y]
print("whatever:", whatever)
W = sum(whatever) / len(whatever)
print(W)


num = sum([1 if x%2 == 0 else 0 for x in listy1])
print(num)
