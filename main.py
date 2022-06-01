import random as ran
import itertools as it


class Player:
    def __init__(self):
        self.score = 0
        self.name = ""

    def __repr__(self):
        return "Player instance , it can be human or computer"

    def increase_score(self, inc):
        self.score += inc

    def get_score(self):
        return self.score


class Human(Player):
    def __init__(self):
        self.score=0

    def __repr__(self):
        return "human player instance"

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def play(self,alist,):
        print("your turn:")
        print("Τα γραμματα που έχεις είναι αυτα: ")
        print(alist)
        print("Γραψε την λέξη σου ή πάτα Π/π για Πασο")
        self.word = input()
        if self.word == 'π' or self.word == 'Π':  # πασο
            return 'Π'
        else:
            for i in self.word:  # αν χρησιμοποιει μονο γραμματα π υπαρχουν στην λιστα τοτε η λεξη ειναι valid (v=1)
                if i in alist:
                    self.v=1
                else:  # αν καποιο γραμμα της λεξης δν ανηκει στην λιστα τοτε (v=0) και η λεξη δεν ειναι αποδεκτη
                    self.v=0
            if self.v:
                if self.word in wordsd.keys() and wordsd[self.word][1] == 0:  # Αν η λεξη υπαρχει και δεν εχει ξανα χρησιμοποιηθει
                    print("Αποδεκτη λεξη")
                    wordsd[self.w][1] += 1
                    # προσθηκη ποντων
                else:
                    print("μη αποδεκτη λεξη,χανεισ την σειρα σου")  # αν η λεξη δεν υπαρχει
                    self.word = 'lost'
            else:
                print("μη αποδεκτη λεξη,χανεισ την σειρα σου")  # αν η έξη δεν ειναι valid , περιεχει κ αλλους χαρακτηρες εκτος απο αυτους της λιστας
                self.word = 'lost'
            return self.word


class Computer(Player):
    def __init__(self):
        pass

    def __repr__(self):
        return "computer instance"

    def play(self):  # smart-fail
        pass


class SackClass:
    def __init__(self):
        self.let = []
        self.alist = []   # συνολο γραμματων 102 # έχει ολα τα γραμματα , είναι το σακουλακι
        #self.sample = []
        # 1) Πρώτη τιμή = πλήθος γραμμάτων στο παιχνίδι
        # 2) Δεύτερη τιμή = αξία γράμματος στο παιχνίδι
        self.letters ={'Α': [12, 1],
                           'Β': [1, 8],
                           'Γ': [2, 4],
                           'Δ': [2, 4],
                           'Ε': [8, 1],
                           'Ζ': [1, 10],
                           'Η': [7, 1],
                           'Θ': [1, 10],
                           'Ι': [8, 1],
                           'Κ': [4, 2],
                           'Λ': [3, 3],
                           'Μ': [3, 3],
                           'Ν': [6, 1],
                           'Ξ': [1, 10],
                           'Ο': [9, 1],
                           'Π': [4, 2],
                           'Ρ': [5, 2],
                           'Σ': [7, 1],
                           'Τ': [8, 1],
                           'Υ': [4, 2],
                           'Φ': [1, 8],
                           'Χ': [1, 8],
                           'Ψ': [1, 10],
                           'Ω': [3, 3]
                   }

    def getvalueofletter(self , l):
        return self.letters[l][1]


    def randomizesack(self): # («ετοιμάζει» το σακουλάκι με τα γράμματα)
        # print(self.letters)
        self.count = 0  # ελεγχει οτι έχουν προστεθει ολα τα γραμματα μέσα στο σακουλακι
        while self.count < 102:
            self.x = ran.randint(913, 937)  # στον πινακα ascii τσ ελληνικά γραμματα ειναι απο το 913=Α εως το 937=Ω εκτος απο την θεση 930
            self.c = chr(self.x)  # το χ έχει τον ακεραιο αριθμο  και στο c βάζουμε το αντιστοιχο γραμμα , η συν chr() επιστρεφει τον αντιστοιχο χαρ του int
            #print(self.x)
            #print(self.c)
            if self.x == 930:
                continue
            else:
                 if self.letters[self.c][0] > 0: #ελεγχει το πληθος των γρμματων που έχουν μεινει ωστε να μην πάρουμε ένα γραμμα περισσοτερες φορες
                    self.count += 1
                    self.alist.append(self.c)
                    self.letters[self.c][0] -= 1
                 else:
                    continue
        #print(self.count)
        return self.alist  # ?
       # print(self.letters[' '][1])



    def getletters(self):  # (βγάζει από το σακουλάκι για τον παίκτη Ν=7 γράμματα)
        self.sample= []
        #print(self.alist)
        self.sample = ran.sample(self.alist, 7)
        #print(self.sample)
        for i in self.sample:
            self.alist.remove(i)
            continue
        return self.sample



    def putbackletters(self, letlist): # (επιστρέφει γράμματα παίκτη στο σακουλάκι)
        for i in letlist:
            self.alist.append(i)
        #print(self.alist)

# Mediator -> ρυθμιστής, ενώνει όλες τις κλάσεις
class Game:
    def __init__(self,wordsd):
        self.ph = Human()
        self.pc = Computer()
        self.sack = SackClass()
        self.validW = wordsd
        self.scoreH = 0
        self.scoreC = 0

    def __repr__(self):
        return "Game instance"

    def setup(self):
        print("Welcome to Scrabble! \nPlease enter your name:")
        x = input()
        self.ph.set_name(x)
        print("Hello " + self.ph.get_name() + "!")
        print("Choose from the following menu 1 , 2 , 3 or q: ")
        side = 10
        print(14 * "* ")
        print("*          M E N U        *")  # *25*
        print("*  1: ΣΚΟΡ                *")
        print("*  2: ΠΛΗΡΟΦΟΡΙΕΣ         *")
        print("*  3: ΠΑΙΧΝΙΔΙ            *")
        print("*  q: ΕΞΟΔΟΣ              *")
        print(14 * "* ")
        self.a = input("-> ") #Επιλογη του χρηστη με β αση το μενου

    def run(self):
        while self.a != "q" or "Q":
            if self.a == "1":
                with open("score.txt", 'r') as f:
                    print(f.read())
            elif self.a == "2":
                pass
            elif self.a == "3":
                self.l = self.sack.randomizesack() #λιστα π περιεχει ολα τα γραμματα
                #print(self.l)
                print("Υπάρχουν 2 είδη παιχνιδιού, Διάλεξε ποιο προτιμάς:")
                print(10 * "-")
                print("Α. *Σεναριο α*")
                print("B. *Senafrio b*")
                print(10 * "-")
                self.b = input("-> ")
                if self.b == "A" or self.b == "a" or self.b == "Α" or self.b == "α":
                    print("Σεναριο Α : ΕΝΑΡΞΗ ΠΑΙΧΝΙΔΙΟΥ")
                    while len(self.l) != 0:
                        self.let = self.sack.getletters() #επιλεγονται 7 τυχαια γραμματα
                        self.w = self.ph.play(self.let)  # παιζει ο
                        #print("H Λεξη " +self.w)
                        if self.w == 'lost':
                            print('Μη αποδεκτη λεξη')
                        elif self.w == 'π' or self.w == 'Π':
                            print(" Πηγες πάσο , χανεις την σειρά σου")
                            self.sack.putbackletters(self.let)
                        else:
                            print("Η ΛΕΞΗ ΣΟΥ: ")
                            print(self.w)
                            print("ΟΙ ΠΟΝΤΟΙ ΣΟΥ: ")
                            self.wordlist = []
                            self.wordlist[:0] = self.w
                            for i in self.wordlist:
                                self.scoreH += self.sack.getvalueofletter(i)
                            print(self.scoreH)
                            """""
                            sum=0
                            alist= ['Σ','Κ','Ρ','Α','Μ','Π','Λ']
                            for i in alist:
                                for j in dict:
                                    if i == j:
                                        sum += dict[j][1]  # increse_score()
                            #print(sum)
                            """
                        print("Computer's turn")
                        #self.let = self.sack.getletters()
                        #self.w = self.pc.play()




                elif b == "B" or b == "b" or b == "Β" or b == "β":
                    pass
                else:
                    print("Wrong Input")
                    print("Α. *Σεναριο α*")
                    print("B. *Senafrio b*")
                    print(10 * "-")
                    b = input("-> ")
            elif self.a == "q" or self.a == "Q":
                print("Goodbye " + self.ph.get_name() + "! \n")
                break
            else:
                print("Wrong Input")
            print("do you want to continue to another category? Yes/No")
            self.c = input("-> ")
            if self.c == 'yes' or self.c == "YES":
                self.a = input(" choose 1 , 2 , 3 ,q: -> ")
            elif self.c == 'no' or self.c == "NO":
                print("Goodbye " + self.ph.get_name() + "! \n")
                break
            else:
                print("Wrong Input")
                print("do you want to continue to another category? Yes/No")
                self.c = input("-> ")

    def end(self):
        pass #το τελικο σκορ τ παικτη γραφεται στο αρχειο score και όλα τα γραμματα γυρνανε στο σακουλακι


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
# key = η λέξη
#  value = 0 ή 1 ανάλογα με το αν έχει χρησιμοποιηθει η λέξη. Αρχικά είναι όλες 0.
wordsd= {}
with open("greek7.txt","r") as f7:
    for line in f7:
        wordsd[line.strip('\n')]= 0
print(wordsd.keys())


#  Δημιουργια SakClass instant
#  sack = SackClass()

game = Game(wordsd)
game.setup()
game.run()



"""""
alist = ["Α","Ε","Δ","Σ","Γ","Ο","Ο"]
blist = [ ]
for i in it.permutations(alist,5):
    mystring=""
    for x in i:
        mystring+= x
        if mystring not in blist:
            blist.append(mystring)
#print(blist)
#check= any(item in wordsl for item in blist)
#print(check)
#check the word
for i in blist:
    if i in wordsl:
        print(i)


# json or pickle ??
"""



"""""
print("Welcome to Scrabble! \nPlease enter your name:")
x = input()
player.set_name(x)
print("Hello " + player.get_name() + "!")
print("Choose from the following menu 1 , 2 , 3 or q: ")
side = 10
print(14 * "* ")
print("*          M E N U        *")  # *25*
print("*  1: ΣΚΟΡ                *")
print("*  2: ΡΥΘΜΙΣΕΙΣ           *")
print("*  3: ΠΑΙΧΝΙΔΙ            *")
print("*  q: ΕΞΟΔΟΣ              *")
print(14 * "* ")
a = input("-> ")
while a != "q" or "Q":
    if a == "1":
        with open("score.txt", 'r') as f:
            print(f.read())
    elif a == "2":
        pass
    elif a == "3":
        print("Υπάρχουν 2 είδη παιχνιδιού, Διάλεξε ποιο προτιμάς:")
        print(10 * "-")
        print("Α. *Σεναριο α*")
        print("B. *Senafrio b*")
        print(10 * "-")
        b = input("-> ")
        if b == "A" or b == "a" or b == "Α" or b == "α":
            pass
        elif b == "B" or b == "b" or b == "Β" or b == "β":
            pass
        else:
            print("Wrong Input")
            print("Α. *Σεναριο α*")
            print("B. *Senafrio b*")
            print(10 * "-")
            b = input("-> ")
    elif a == "q" or a == "Q":
        print("Goodbye " + player.get_name() + "! \n")
        break
    else:
        print("Wrong Input")
    print("do you want to continue to another category? Yes/No")
    c = input("-> ")
    if c == 'yes' or c == "YES":
        a = input(" choose 1 , 2 , 3 ,q: -> ")
    elif c == 'no' or c == "NO":
        print("Goodbye " + player.get_name() + "! \n")
        break
    else:
        print("Wrong Input")
        print("do you want to continue to another category? Yes/No")
        c = input("-> ")
"""""

""""
        for i in self.sample:
            if i == 0:
                self.let.append("Α")
                self.letters[0][0]-= 1
            elif i == 1:
                self.let.append("Β")
                self.letters[1][0]-= 1
            elif i == 2:
                self.let.append("Γ")
                self.letters[2][0]-= 1
            elif i == 3:
                self.let.append("Δ")
                self.letters[3][0]-= 1
            elif i == 4:
                self.let.append("Ε")
                self.letters[4][0]-= 1
            elif i == 5:
                self.let.append("Ζ")
                self.letters[5][0]-= 1
            elif i == 6:
                self.let.append("Η")
                self.letters[6][0]-= 1
            elif i == 7:
                self.let.append("Θ")
                self.letters[7][0]-= 1
            elif i == 8:
                self.let.append("Ι")
                self.letters[8][0]-= 1
            elif i == 9:
                self.let.append("Κ")
                self.letters[9][0]-= 1
            elif i == 10:
                self.let.append("Λ")
                self.letters[10][0]-= 1
            elif i == 11:
                self.let.append("Μ")
                self.letters[11][0]-= 1
            elif i == 12:
                self.let.append("Ν")
                self.letters[12][0]-= 1

"""