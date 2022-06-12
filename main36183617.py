import classes

# ###main###
# create greek7.txt
with open("greek.txt", "r", encoding="utf-8") as f:
    with open("greek7.txt", "w") as f7:
        for line in f:
            if len(line) <= 8:
                f7.write(line)

# list with the words so we can check
# i. if the word the player wrote is correct
# ii. computer's word
wordsl = []
with open("greek7.txt","r") as f7:
     #print(f7.read())
     for line in f7:
         wordsl.append(line.strip("\n"))


#  dict with the words
#  key = η λέξη
#  value = 0 ή 1 ανάλογα με το αν έχει χρησιμοποιηθει η λέξη. Αρχικά είναι όλες 0.
wordsd= {}
with open("greek7.txt","r") as f7:
    for line in f7:
        wordsd[line.strip('\n')]= 0
#print(wordsd.keys())
game = classes.Game(wordsd)
game.setup()
game.run()

