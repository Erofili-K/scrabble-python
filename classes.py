import random as ran
import itertools as it


def guidline():
    """
    ---------ΣΚΡΑΜΠΛ---------
    Ερωφίλη Κώνστα 3618
    Γεωργία Ειρήνη Κοσμίδου 3617
    --------------------------
    Πώς παίζεται το παιχνίδι:
    Μόλις ο χρήστης αποφασίσει να τρέξει το πρόγραμμα, του ζητείται να δώσει ένα όνομα. Στην συνέχεια εμφανίζεται το μενού επιλογών
    με εξής κατηγορίες:
            1. Σκορ -> Εδώ αποθηκεύονται τα σκορ των χρηστών κάθε φορά που τελειώνει ένα παιχνίδι.
            2. Πληροφορίες -> καλείται η συνάρτηση guidline που εξηγεί τον κώδικα , και πως παίζεται το παιχνίδι
            3. Παιχνίδι -> Από εδώ αρχίζει το παιχνίδι , αποτελεί την επιλογή για να αρχίσει ο παικτης να παίζει
            4. Εξοδος -> Από εδώ είναι ένας τρόπος να τερματιστεί το πρόγραμμα
    **ΠΑΙΧΝΙΔΙ**
    Για να δεις αναλυτικά τα σενάρια παιχνιδιου και τι ειναι το καθένα πήγαινε στο 6.
    Μόλις ο χρήστης επιλέξει Α ή Β που αντιστοιχει στο κάθε σενάριο, τοτε αρχίζει το παιχνίδι. Πρώτος πάιζει ο χρήστης.
    Εμφανίζονται στην οθόνη τα διαθέσιμα γράμματα που έχει και η επιλογή Π/π για πάσο αν δεν μπορει να σκεφτεί κάποια λέξη
    Μόλις δεχθεί την λέξη που έβαλε ο χρήστης, εμφανίζονται κατάλληλα μηνύματα και οι πόντοι που πήρε από αυτην , καθώς και οι
    συνολικοί ποντοι απο την αρχή του παιχνιδιού.
    Μετά είναι η σειρα του Υπολογιστη να παιξει.
    Τα σενάρια που επιλέγει ο χρήστης (Α/Β) αφορούν τον τρόπο παιχνιδιού απο την πλευρά του υπολογιστή.
    Ανάλογα με τον αλγόριθμο που εκτελείται κάθε φορά (περισσοτερα στο 6.) ο τρόπος που ελέγχεται η λέξη είναι ως εξης:
    Μολις επιλεχθεί μια συμβολοσειρά , ελέγχεται αν βρίσκεται μέσα στο λεξικό που περιέχει όλες τις επιτρεπτές λέξεις (περισσοτερα στο 5.)
    και άν υπάρχει εκεί , τότε η λέξη είναι επιτρεπτή και μπορεί να την χρησιμοποιήσει ο υπολογιστής. Τέλος εμφανίζεται η λέξη και
    προσμετρούνται οι πόντοι.
    Μόλις τελειώσει και η σειρά του υπολογιστή, έχει ουσιαστικά τελειώσει ο γύρος.
    Έχει την δυνατοτητα ο χρήστης να σταματήσει το παιχνίδι κάθε φορά που τελειώνει ο γύρο αν στην ερωτηση "Συνεχίζεις? Ν(αι)/Ο(χι)"
    απαντήσει Ο (οχι) . Γενικά ο γύρος τελειωνει μόνο οταν δεν υπάρχουν αρκετά γράμματα στο σακουλάκι.
    (αν δεν σε ενδιαφέρει η εξηγηση του κώδικα, μπορείς να σταματήσεις εδω , και να επιστρέψεις στο παιχνίδι)

    Τα αρχεια που χρησιμοποιουνται ειναι :
    - classes.py : περιλαμβανει όλςε τις κλασεις που αναλυονται πιο κατω
    - main36183617.py : Η main του προγραμματος στην οποια δημιουργειται το λεξικο με τις λεξεις απο τα αρχεια greek.txt & greek7.txt
    - greek.txt : οπως δινεται απο την σελιδα του μαθηματος , απο το οποιο δημιουργειται το greek7.txt
    - score.txt : Εδω γραφονται τα σκορ των χρηστων

    Αναλυτικότερα:
    1. Ποιές κλάσεις έχετε υλοποιήσει στον κώδικά σας;
        Στο πρόγραμμά μας - για την υλοποίηση του παιχνιδιού scrabble -
        υλοποιήσαμε πέντε (5) κλάσεις , οι οποίες είναι οι εξης:
         SakClass: κλάση που καθορίζει πώς λειτουργεί το αντικείμενο
        «σακουλάκι» με τα γράμματα του παιχνιδιού. Η κλάση SakClass έχει 5 μεθόδους:
                    __init__ : που γίνονται οι αρχικοποιήσεις,
                    getvalueofletter :  επιστρέφει την αξία ενός συγκεκριμένου γράμματος
                    randomizesack : ετοιμάζει το σακουλάκι . Δηλαδή , γνωρίζουμε ότι όλα ταγράμματα είναι 102 και πρέπει να
                        τοποθετηθούν όλα μέσα στο σακουλάκι όσες φορές αναδεικνυται. Αυτό που επιστρέφει είναι μια λιστα( self.alist)
                        που περιέχει όλα τα 102 γράμματα που μπορουν να χρησιμοποιηθουν
                        Η εντολή ran.randint(913, 937) παιρνει τυχαία αριθμους απο το 913-937 (στον πινακα ascii τσ ελληνικά γραμματα ειναι απο το 913=Α εως το 937=Ω εκτος απο την θεση 930)
                        ώστε η λίστα να έχει τυχαια κατανεμημένα τα 102 γραμματα
                    getletters : "Βγαζει" απο το σακουλάκι(δηλαδή την alist) 7 τυχαία γράμματα τα οποία αποτελούν το χέρι του παικτη
                        και το χέρι του υπολογιστή.Αυτά τα γράμματα αφαιρούνται απο την alist. Η τυχαία επιλογη των 7 γραμμάτων
                        γινεται με την ran.sample(self.alist, 7) που ουσιαστικά επιστρέφει ένα τυχαίο δειγμα Ν=7.
                    putbackletters : επιστρέφει στο σακουλακι(alist) τα γραμματα που δεν χρησιμοποιήθηκαν.
         Player: βασική κλάση από την οποία παράγονται οι Human και
        Computer
         Human: κλάση παράγωγος της Player που καθορίζει λειτουργίες του
        παιχνιδιού για τον άνθρωπο-παίκτη
         Computer: κλάση παράγωγος της Player που καθορίζει λειτουργίες του
        παιχνιδιού για τον υπολογιστή-παίκτη
         Game: κλάση που περιγράφει το πώς εξελίσσεται μια παρτίδα (game). Οι μέθοδοι που περιλαμβάνει αυτη
        η κλάση είναι :
                    __init__: εδω γίνονται οι αρχικοποιήσεις, και επίσης σαν ορισμα περνιέται και το λεξικό που έχει δημιουργηθεί
                        απο την main με όλες τις λέξεις.
                    setup: δημιουργία του αρχικού μενου και η επιλογή του χρήστη
                    run: Εδω γίνεται όλη η διαδικασία του παιχνιδιου. Αρχικά αναλογα με την επιλογη του χρήστη, εμφανίζονται εξτρα μηνυματα και
                        καλείται κάθε φορά η μεθοδος play του χρηστη και του υπολογιστη.
                    end: Η μέθοδς αυτη καλειται μόλις ο χρήστης έχει τελειωσει το παιχνίδι ή εχει αποφασισει να σταματησει.
                        Σε αυτην, αν το σκορ του χρηστη είναι πάνω απο 0 τοτε μέσα στο αρχειο score καταγράφεται το συνολικο σκορ του
                        χρηστη.

    2. Ποιά κληρονομικότητα έχετε υλοποιήσει (Π.χ. Ποιά η βασική κλάση και
       ποιές οι παράγωγες που έχετε υλοποιήσει);
        Στο πρόγραμμά μας παρατηρείται κληρονομικότητα στις κλάσεις Player ,
        Human και Computer. Συγκεκριμένα , οι κλάσεις Human και Computer
        κληρονομούν την Player με μεθόδους : init, repr και play στην οποία
        υλοποιείται ο αλγόριθμος σύμφωνα με τον οποίο θα παίζει ο H/Y (παρακάτω
        αναφέρονται αναλυτικά ποιοι αλγόριθμοι χρησιμοποιήθηκαν )

    3. Ποιά επέκταση μεθόδων έχετε υλοποιήσει (π.χ. Ποιές μέθοδοι
       επεκτείνουν την ανώτερη στις κλάσεις που δημιουργήσατε)
       Η κλαση Human κληρονομει απο την Player , και η μεθοδος play του Human επεκτείνει την play του Player.
       Αναλυτικότερα , η play (Human) αναπαριστά το πως παιζει ο χρήστης: Δεχεται ως παραμετρους την λιστα με τα 7 τυχαια γραμματα
       και το λεξικο με τις λεξεις στην συνεχεια ζητα απο τον χρηστη να γραψει την λεξη που σκεφτηκε. Υπαρχουν 2 επιλογες:
            α. να πατησει πασο αν δεν μπορει να σκεφτει καποια λεξη
            β. να γραψει την λεξη που νομιζει οτι ειναι σωστη
            Αν πληκρολογησει μια λεξη, τοτε:
                i. ελεγχει αν εχει χρησιμοποιησει καποιο γραμμα που δεν υπηρχε στην λιστα (που δεν επιτρεπεται)
                ii. αν η λεξη ειναι επιτρεπτή, τοτε ελεγχει 2 πραγματα:
                    1. αν υπαρχει η λεξη μεσα στο λεξικό
                    2. αν εχει ξανα χρησιμοποιηθει.
            Αν ολα τα κριτηρια πληρουνται ( δηλαδη η λεξη περιεχει γραμματα μονο απο τα 7 που δοθηκαν , υπαρχει στο λεξικο και δεν εχει
            ξανα χρησιμοποιηθει) , τοτε ειναι αποδεκτη και γυρναει στην run και υπολογιζονται οι ποντου
            Εμφανοζονται σε καθε περιπτωση καταλληλα μηνυματα.
        Επειδη η Computer κληρονομει και αυτη απο την Player επεκτεινει την μεθοδο play ως εξης:
        Αρχικα, επειδη ειμαστε 2 άτομα επρεπε να υλοποιησουμε 2 σεναρια για τον τροπο που παιζει ο υπολογιστης( αναφερονται στο 6.)
        τα ορισματα ειναι τα ιδια με αυτα π εχε η play του Human + ε΄να ορισμα που αφορα το πιο σεναριο εχει επιλεξει ο χρηστης.
        Σε κάθε σεναριο , επιστρεφεται η αποδεκτη λεξη που παιζει ο υπολογιστης.
        Τα σεναρια πιο αναλυτικα στο 6.

    4. Αν έχετε εφαρμόσει υπερφόρτωση τελεστών ή χρησιμοποιήσατε decorators
       και σε ποιό σημείο του κώδικα
        Δεν έχουμε εφαρμόσει κανένα από τα παραπάνω

    5. Σε ποιά δομή (λίστα ή λεξικό-dictionary) οργανώνει η εφαρμογή σας τις
       λέξεις της γλώσσας στη διάρκεια του παιχνιδιού
        Αρχικά, το πρόγραμμά μας φορτώνει τις λέξεις της γλώσσας από το αρχείο
        greek7.txt και τις μεταφέρει σε λεξικό στον κώδικα ώστε να μπορούν να
        γίνουν οι απαραίτητοι έλεγχοι στο παιχνίδι. Το λεξικό που χρησιμοποιούμε
        είναι το wordsd στο οποίο σαν κλειδί (key) χρησιμοποιείται η λέξη και σαν
        τιμή (value) εκχωρείται η ακέραια τιμή 0 (αν δεν χρησιμοποιείται η λέξη) ή 1
        (αν χρησιμοποιείται). Στην αρχή , όπως είναι λογικό, είναι εκχωρημένη παντού
        η ακέραια τιμή 0 . Καθε φορα που μια λεξη χρησιμοπιειται ο αριθμος της γινεται 1

    6. Ποιόν αλγόριθμο (ή αλγόριθμους) υλοποιήσατε για να παίξει ο Η/Υ
        Η ομάδα απαρτίζεται από δύο άτομα για αυτό και υλοποιήθηκαν δύο
        αλγόριθμοι σύμφωνα με τον οποίο θα παίζει ο Η/Υ. Συγκεκριμένα,
        ο MIN-MAX-SMART και ο SMART-FAIL (η υλοποίησή τους
        είναι πλήρως αναλυμένη στις διαφάνειες του οδηγού εργασίας για αυτό και
        δεν υπάρχει επιπλέον πληροφορία πέρα από το γεγονός ότι στην μέθοδο FAIL
        επιλέγεται η δεύτερη καλύτερη επιλογή λέξης).
        Επίσης, αξίζει να σημειωθεί,
        ότι στην μέθοδο run αν ο χρήστης έχει επιλέξει το πρωτο σσσεναριο παιχνιδιου (min-max-smart)
        ερωτάται σε κάθε παρτίδα με ποιον αλγόριθμο από τους δύο παραπάνω θα παίξει ο αντίπαλος του, δηλαδή ο H/Y.
    Τελος, μέσα στον κωδικα υπαρχουν πολλα σχολια που εξηγουν τι ειναι η καθε μεταβλητη και την πορεια της σκεψης μας για την
    υλοποιήση του προγραμματος. Για να ελεγχουμε την σωστη πορεια του κωδικα, υπάρχουν σε σχολια πολλα print που εμφανιζουν
    διαφορα σταδια και λιστες που χρησιμοποιουνται κατα την διαρκεια, οποτε αν θελησετε να εμφανισετε κατι παραπάνω μπορειτε να τα δειτε.

    """
    pass


class Player:
    def __init__(self):
        self.score = 0
        self.name = ""

    def __repr__(self):
        return "Player instance , it can be human or computer"

    def set_score(self, score):
        pass

    def get_score(self):
        return self.score

    def play(self):
        pass


class Human(Player):
    def __init__(self):
        self.score = 0

    def __repr__(self):
        return "human player instance"

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def play(self, alist, wordsd):
        print("Η σειρα σου:")
        print("Τα γραμματα που έχεις είναι αυτα: ")
        print(alist)
        print("Γραψε την λέξη σου ή πάτα Π/π για Πασο")
        self.word = input()
        if self.word == 'π' or self.word == 'Π':  # πασο
            return 'Π'
        else:
            self.v = 1
            for i in self.word:  # αν καποιο γραμμα της λεξης δν ανηκει στην λιστα τοτε (v=0) και η λεξη δεν ειναι αποδεκτη
                if i not in alist:
                    self.v = 0
                    break
            if self.v == 1:
                if self.word in wordsd.keys():  # Αν η λεξη υπαρχει και δεν εχει ξανα χρησιμοποιηθει
                    if wordsd[self.word] == 0:
                        print("Αποδεκτη λεξη")
                        wordsd[self.word] = 1
                        #print(wordsd)
                    else:
                        self.word = 'lost'
                        print("Η λεξη εχει ξανα χρησιμοποιηθει.")
                else:
                    print("Η λεξη δεν υπαρχει , χανεισ την σειρα σου")  # αν η λεξη δεν υπαρχει
                    self.word = 'lost'
            else:
                print("μη αποδεκτη λεξη,χανεισ την σειρα σου")  # αν η έξη δεν ειναι valid , περιεχει κ αλλους χαρακτηρες εκτος απο αυτους της λιστας
                self.word = 'lost'
            return self.word


class Computer(Player):
    def __init__(self):
        self.sackA = SackClass()

    def __repr__(self):
        return "computer instance"

    def play(self,senario,alist,wordsd):  # smart-fail #MIN MAX SMART #ποιο σεναριο εχει επιλεξει
        print("Εχεις επιλέξει το", senario, "για να πάιξει ο υπολογιστής")
        print("Τα γραμματα που έχει ο υπολογιστης ειναι αυτά:")
        print(alist)
        if senario == "A" or senario == "a" or senario == "Α" or senario == "α":
            print("Επελεξε: ")
            print("Α: Μεθοδο για MIN LETTERS")
            print("B: Μεθδοδο για MAX LETTERS")
            print("Γ: Μεθοδο για SMART")
            self.dec = input("-> ")
            if self.dec == "Α":
                self.blist = []
                for i in it.permutations(alist, 2):
                    mystring = ""
                    for x in i:
                        mystring += x
                        if len(mystring) == 2:
                            if mystring not in self.blist:
                                self.blist.append(mystring)
                        else:
                            continue
                for i in it.permutations(alist, 3):
                    mystring = ""
                    for x in i:
                        mystring += x
                        if len(mystring) == 3:
                            if mystring not in self.blist:
                                self.blist.append(mystring)
                        else:
                            continue
                for i in it.permutations(alist, 4):
                    mystring = ""
                    for x in i:
                        mystring += x
                        if len(mystring) == 4:
                            if mystring not in self.blist:
                                self.blist.append(mystring)
                        else:
                            continue
                for i in it.permutations(alist, 5):
                    mystring = ""
                    for x in i:
                        mystring += x
                        if len(mystring) == 5:
                            if mystring not in self.blist:
                                self.blist.append(mystring)
                        else:
                            continue
                for i in it.permutations(alist, 6):
                    mystring = ""
                    for x in i:
                        mystring += x
                        if len(mystring) == 6:
                            if mystring not in self.blist:
                                self.blist.append(mystring)
                        else:
                            continue
                for i in it.permutations(alist, 7):
                    mystring = ""
                    for x in i:
                        mystring += x
                        if len(mystring) == 7:
                            if mystring not in self.blist:
                                self.blist.append(mystring)
                        else:
                            continue
                # print(blist)
                for i in self.blist:
                    if i in wordsd.keys():
                        return i  # επιστρεφει την πρωτη λεξη που δεχθηκε ως πιθανη λυση με τα λιγοτερα γραμματα
                    else:
                        self.blist.remove(i)
            elif self.dec =="Β":
                self.blist = []
                for i in it.permutations(alist, 7):
                    mystring = ""
                    for x in i:
                        mystring += x
                        if len(mystring)==7:
                            if mystring not in self.blist:
                                self.blist.append(mystring)
                        else:
                            continue
                for i in it.permutations(alist, 6):
                    mystring = ""
                    for x in i:
                        mystring += x
                        if len(mystring) == 6:
                            if mystring not in self.blist:
                                self.blist.append(mystring)
                        else:
                            continue
                for i in it.permutations(alist, 5):
                    mystring = ""
                    for x in i:
                        mystring += x
                        if len(mystring) == 5:
                            if mystring not in self.blist:
                                self.blist.append(mystring)
                        else:
                            continue
                for i in it.permutations(alist, 4):
                    mystring = ""
                    for x in i:
                        mystring += x
                        if len(mystring) == 4:
                            if mystring not in self.blist:
                                self.blist.append(mystring)
                        else:
                            continue
                for i in it.permutations(alist, 3):
                    mystring = ""
                    for x in i:
                        mystring += x
                        if len(mystring) == 3:
                            if mystring not in self.blist:
                                self.blist.append(mystring)
                        else:
                            continue
                for i in it.permutations(alist, 2):
                    mystring = ""
                    for x in i:
                        mystring += x
                        if len(mystring) == 2:
                            if mystring not in self.blist:
                                self.blist.append(mystring)
                        else:
                            continue
                #print(self.blist)
                for i in self.blist:
                    if i in wordsd.keys():
                       return i  # επιστρεφει την πρωτη λεξη που δεχθηκε ως πιθανη λυση με τα περισσοτερα γραμματα
                    else:
                        self.blist.remove(i)

            else:
                self.blist = []
                self.wordvalue=[]
                self.value = 0
                for i in it.permutations(alist, 7):
                    mystring = ""
                    for x in i:
                        mystring += x
                        if len(mystring) == 1:
                            continue
                        else:
                            if mystring not in self.blist and mystring in wordsd.keys():
                                self.blist.append(mystring)
                                #print(self.blist)
                                for i in mystring:
                                    self.value += self.sackA.getvalueofletter(i)
                                self.wordvalue.append(self.value)
                                self.value = 0
                                #print(self.wordvalue)
                #print(self.blist)
                self.m = max(self.wordvalue) #βρισκει το max απο τους ποντουσ
                self.ind = self.wordvalue.index(self.m) #βρικσει την θεση του max
                return self.blist[self.ind]
        else:
            print("ΣΕΝΑΡΙΟ Β")  # SMART FAIL
            self.blist = []
            self.wordvalue = []
            self.value = 0
            for i in it.permutations(alist, 7):
                mystring = ""
                for x in i:
                    mystring += x
                    if len(mystring) == 1:
                        continue
                    else:
                        if mystring not in self.blist and mystring in wordsd.keys():
                            self.blist.append(mystring)
                            #print(self.blist)
                            for i in mystring:
                                self.value += self.sackA.getvalueofletter(i)
                            self.wordvalue.append(self.value)
                            self.value = 0
                            #print(self.wordvalue)
            # print(self.blist)
            self.ziplist = zip(self.wordvalue,self.blist)
            self.sortedp= sorted(self.ziplist)
            self.tuples= zip(*self.sortedp)
            self.wordvalue, self.blist =[ list(tuple) for tuple in self.tuples]
            # print(self.blist)
            # print(self.wordvalue)
            self.m = max(self.wordvalue)
            self.ind = self.wordvalue.index(self.m)
            for i in range(self.ind,0,-1):
                #print("fffff")
                if self.wordvalue[i]<self.m:
                    #print("gggg")
                    return self.blist[i], self.wordvalue[i]


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
            if self.x == 930:  # δεν υπάρχει κατι σε αυτην την θέση οποτε την αγνοουμε
                continue
            else:
                 if self.letters[self.c][0] > 0: # ελεγχει το πληθος των γρμματων που έχουν μεινει ωστε να μην πάρουμε ένα γραμμα περισσοτερες φορες
                    self.count += 1
                    self.alist.append(self.c)
                    self.letters[self.c][0] -= 1
                 else:
                    continue
        # print(self.count)
        return self.alist
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

    def putbackletters(self, letlist):  # (επιστρέφει γράμματα παίκτη στο σακουλάκι)
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
        self.onewordp = 0  # οι ποντοι της συγκεκριμενης λέξης
        self.scoreH = 0
        self.scoreC = 0
        self.gyros = 0
        self.length = 0

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
        print("Για να δεις αναλυτικα τα σεναρια παιχνιδου πάτα 2 πριν ξεκινησεις το παιχνιδι!")
        self.a = input("-> ") #Επιλογη του χρηστη με β αση το μενου

    def run(self):
        while self.a != "q" or "Q":
            if self.a == "1": #σκορ
                print("ΣΚΟΡ ΧΡΗΣΤΩΝ:")
                with open("score.txt", 'r') as f:
                    print(f.read())
            elif self.a == "2":  #πληροφοριες
                help(guidline)
            elif self.a == "3":  #παιχνιδι
                self.l = self.sack.randomizesack() #λιστα π περιεχει ολα τα γραμματα
                self.length = len(self.l)
                # print(self.l)
                print("Υπάρχουν 2 είδη παιχνιδιού, Διάλεξε ποιο προτιμάς:")
                print(10 * "-")
                print("Α. *Σεναριο α : min-max-smart*")
                print("B. *Σεναριο β : smart-fail*")
                print(10 * "-")
                self.b = input("-> ")
                self.stop = 0
                if self.b == "A" or self.b == "a" or self.b == "Α" or self.b == "α" or self.b == "B" or self.b == "b" or self.b == "Β" or self.b == "β":
                    print("ΕΝΑΡΞΗ ΠΑΙΧΝΙΔΙΟΥ")
                    print("Αρχικα υπαρχουν", self.length, "γραμματα στο σακουλακι")
                    while self.length != 0 and self.stop == 0:
                        self.gyros += 1
                        print("Γυρος", self.gyros)
                        self.let = self.sack.getletters() #επιλεγονται 7 τυχαια γραμματα
                        self.length -= 7
                        self.w = self.ph.play(self.let,self.validW)  # παιζει ο παικτης
                        #print("H Λεξη " +self.w)
                        if self.w == 'lost':
                            self.onewordp = 0 # οι ποντοι της συγκεκριμενης λέξης
                            print('Μη αποδεκτη λεξη')
                            print("Οι ποντοι σου τωρα:", self.onewordp,"       ", "Οι ποντοι σου συνολικκα:", self.scoreH)
                        elif self.w == 'π' or self.w == 'Π':
                            self.onewordp = 0 # οι ποντοι της συγκεκριμενης λέξης
                            print(" Πηγες πάσο , χανεις την σειρά σου")
                            print("Οι ποντοι σου τωρα:", self.onewordp,"       ", "Οι ποντοι σου συνολικκα:", self.scoreH)
                            self.sack.putbackletters(self.let)
                            self.length +=7
                        else:
                            print("Η ΛΕΞΗ ΣΟΥ: ")
                            print(self.w)
                            self.onewordp = 0 # οι ποντοι της συγκεκριμενης λέξης
                            print("ΟΙ ΠΟΝΤΟΙ ΣΟΥ: ")
                            self.wordlist = []
                            self.wordlist[:0] = self.w
                            for i in self.wordlist:
                                self.onewordp += self.sack.getvalueofletter(i)
                            self.scoreH+=self.onewordp # οι συνολικοι ποντοι του χρηστη
                            print("Οι ποντοι σου τωρα:", self.onewordp,"       ", "Οι ποντοι σου συνολικκα:", self.scoreH)
                        print("--------------------------------------------------------------------------------")
                        print("ΣΕΙΡΑ ΤΟΥ ΥΠΟΛΟΓΙΣΤΗ")
                        if self.b == "A" or self.b == "a" or self.b == "Α" or self.b == "α":
                            self.let = self.sack.getletters() #γραμματα για τον υπολ
                            self.length -= 7
                            self.wordcomp = self.pc.play(self.b, self.let,self.validW)
                            print("Ο υπολογιστης επαιξε:")
                            print(self.wordcomp)
                            print("ΠΟΝΤΟΙ ΤΟΥ ΥΠΟΛΟΓΙΣΤΗ: ")
                            self.wordlist = []
                            self.wordlist[:0] = self.wordcomp
                            self.onewordp = 0
                            for i in self.wordlist:
                                self.onewordp += self.sack.getvalueofletter(i)
                            self.scoreC += self.onewordp
                            print("Οι ποντοι του υπολογιστη τωρα:", self.onewordp, "       ", "Οι ποντοι του υπολογιστη συνολικκα:", self.scoreC)
                        elif self.b == "Β" or self.b == "β" or self.b == "B" or self.b == "b":
                            self.let = self.sack.getletters()  # γραμματα για τον υπολ
                            self.length -= 7
                            self.wordcomp,self.pointsc = self.pc.play(self.b, self.let,self.validW)
                            self.scoreC+=self.pointsc
                            print("Ο υπολογιστης επαιξε:")
                            print(self.wordcomp)
                            print("ΠΟΝΤΟΙ ΤΟΥ ΥΠΟΛΟΓΙΣΤΗ: ")
                            print("Οι ποντοι του υπολογιστη τωρα:", self.pointsc, "       ", "Οι ποντοι του υπολογιστη συνολικκα:", self.scoreC)
                        print("--------------------------")
                        print("Ο",self.gyros,"ος", "γυρος τελειωσε!")
                        print("Εχουν μεινει",self.length,"γραμματα στο σακουλακι")
                        print("--------------------------")
                        if self.length < 14:
                            self.length = 0
                        print("Συνεχίζεις? Ν(αι)/Ο(χι)")
                        self.n_o = input("->")
                        print("--------------------------")
                        if self.n_o == "Ο":
                            self.stop = 1

                    else:
                        if self.stop ==1 :
                            print("Ευχαριστουμε που επαιξες!")
                        else:
                            print("Τελειωσαν τα γραμματα. Ευχαριστουμε που επαιξες!")
                        self.end()

                else:
                    print("Wrong Input")
                    print("Α. *Σεναριο α*")
                    print("B. *Σεναριο β*")
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
        self.ph.set_score(self.scoreH)
        print("Συγκέντρωσες", self.scoreH , "πόντους")
        self.pc.set_score(self.scoreC)
        print("Ο υπολογιστής συγκέντρωσε", self.scoreC, "ποντους")
        if self.scoreH > 0:
            with open("score.txt", 'a') as f:
                f.write(self.ph.get_name()+" " + str(self.scoreH))  # το τελικο σκορ τ παικτη γραφεται στο αρχειο score και όλα τα γραμματα γυρνανε στο σακουλακι
                f.write("\n")
                f.close()







"""""
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
#wordsl = []
#with open("greek7.txt","r") as f7:
     #print(f7.read())
     #for line in f7:
         #wordsl.append(line.strip("\n"))


#  dict with the words
# key = η λέξη
#  value = 0 ή 1 ανάλογα με το αν έχει χρησιμοποιηθει η λέξη. Αρχικά είναι όλες 0.
wordsd= {}
with open("greek7.txt","r") as f7:
    for line in f7:
        wordsd[line.strip('\n')]= 0
#print(wordsd.keys())
game = Game(wordsd)
game.setup()
game.run()
"""""
