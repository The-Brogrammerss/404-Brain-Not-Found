import random
# a = [1]
#
# if a:
#     print("empty?")
#


# listy1 = [1, 2, 7, 6, 1, 2]
# listy2 = [1, 2, 3, 4, 5, 6]
# to_delete = []
# for index, num in enumerate(listy1):
#     if num == 1:
#         to_delete.append(index)
# list.reverse(to_delete)
# for index in to_delete:
#     del listy2[index]
# print(listy2)

# listy1 = [1, 2, 7, 6, 1, 2]
# listy2 = [1, 2, 3, 4, 5, 6]
# listy2[:] = [del listy2[index] for index, spec in enumerate(listy2) for listy in listy1 if listy != 0]
# print(listy2)

# num_similarities = sum([1 for x in listy1 for y in listy2 if x == y])
# print(num_similarities)
# whatever = [abs(x - y) for x in listy1 for y in listy2 if x == y]
# print("whatever:", whatever)
# W = sum(whatever) / len(whatever)
# print(W)

#
# num = sum([1 if x%2 == 0 else 0 for x in listy1])
# print(num)

#
#
# a = [11, 22, 33, 44]
# for index, genome in enumerate(a):
#     print(index, genome)
#
