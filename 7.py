import random
def jeden():
    with open("78\jeden.txt") as f:
        print(f.readlines())
#jeden()
def dwa():
    with open("78\jeden.txt") as f:
        for lines in f:
            print(lines)
#dwa()
def trzy():
    print("Input the name of the file: ")
    name = input()
    temp = 0
    with open(name) as f:
        for lines in f:
            temp = temp + 1
        print(temp)
#trzy()
def cztery():
    with open("78\jeden.txt") as f:
        for x in range(5):
            print(f.readline())
            print(f.readline())
            print(f.readline())
            print(f.readline())
            print(f.readline())
            input("Press Enter to continue")
#cztery()
def piec():
    temp = "temp"
    with open("78\jeden.txt") as firstFile, open("78\dwa.txt", "x") as secondFile:
        for lines in firstFile:
            secondFile.write(lines)                 
#piec()
def szesc():
    with open("78\shoppingList.txt", "x") as ShoppingList, open("78\MeatAndFish.txt") as  MeatAndFsih, open("78\GrainsAndBread.txt") as GrainsAndBread:
        for lines in MeatAndFsih:
            ShoppingList.write(lines)
        for liness in GrainsAndBread:
            ShoppingList.write(liness)
#szesc()
def siedem():
    with open("78\dwadziescia.txt", "x") as file:
        for x in range(1, 51):
            file.write(str(x))
            file.write("\n")
#siedem()
def osiem():
    with open("78\dfandom.txt", "x") as file:
        for x in range(50):
            file.write(str(random.uniform(0, 51)))
            file.write("\n")
#osiem()