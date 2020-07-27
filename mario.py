for i in range(4):
    print("?", end="") #so it won't go the a new line every time.
print()
print("--------------------------")
#we can also print the same like this:
print("?" * 4)

#print column of #
for i in range(3):
    print("#")
print("--------------------------")
#same with diferent sintax
print("#\n" * 3, end="")

for i in range(3):
    for j in range(3):
        print("#", end="")
    print()