global X,O,EMPTY,TIE,LICZBA_POL
X="X"
O="O"
EMPTY=" "
TIE="TIE"
LICZBA_POL=9

def instrukcja():
    """Wyswietl instrukcje"""
    print("""
    	Wprowadz numer
    	
    	0   |1   |2 
    	____|____|___
    	3   |4   |5 
    	____|____|___
    	    |    |
    	6   |7   |8 
    	
    	""")
def yes_no(question):
    """Zadaj pytanie na ktore mozna odpowiedziec rak lub nie"""
    odpowiedz=None
    while odpowiedz not in("t","n"):
        odpowiedz=input(question).lower()
    return odpowiedz
        
def zakres_liczb(question,low=1,high=1):
    """Popros o podanie liczby z pewnego zakresu"""
    odpowiedz=None
    while odpowiedz not in range(low,high):
        odpowiedz=int(input(question))
        return odpowiedz
    
def kogo_ruch():
    """Ustal do kogo nalezy pierwszy ruch"""
    go_first=yes_no("Czy chcesz byc pierwszy?(t/n)")
    if go_first=="t":
        print("Pierwszy ruch nalezy do Ciebie")
        human=X
        computer=O
    else:
        print("Komputer zaczyna")
        computer=X
        human=O
    return computer,human
    
def nowa_plansza():
    """Tworzy nowa plansze gry"""
    plansza=[]
    for square in range(LICZBA_POL):
        plansza.append(EMPTY)
    return plansza

def wyswietl_plansze(plansza):
    """Wyswietla plansze na pulpicie"""
    print("\t",plansza[0],"|",plansza[1],"|",plansza[2])
    print("\t___|___|___")
    print("\t",plansza[3],"|",plansza[4],"|",plansza[5])
    print("\t___|___|___")
    print("\t",plansza[6],"|",plansza[7],"|",plansza[8],"\n")
    	
def prawidlowe_ruchy(plansza):
    """Tworzy liste prawidlowych ruchow"""
    ruchy=[]
    for square in range(LICZBA_POL):
        if plansza[square]==EMPTY:
            ruchy.append(square)
    return ruchy
    
def winner(plansza):
    """ Ustal zwyciezce gry"""
    WIN=((0,1,2),
    	    (3,4,5),
    	    (6,7,8),
    	    (0,3,6),
    	    (1,4,7),
    	    (2,5,8),
    	    (0,4,8),
    	    (2,4,6))
    for row in WIN:
        if plansza[row[0]]==plansza[row[1]]==plansza[row[2]]!=EMPTY:
            winner=plansza[row[0]]
            return winner
        if EMPTY not in plansza:
            return TIE
    return None
    
def ruch_czlowieka(plansza,human):
    """Odczytaj tuch czlowieka"""
    legal=prawidlowe_ruchy(plansza)
    move=None
    while move not in legal:
        move=zakres_liczb("Jaki bedzie twoj ruch(0-8) ",0,LICZBA_POL)
        if move not in legal:
            print("To pole jest juz zajete, probuj ponownie\n")
    print("Dobrze")
    return move
    
def ruch_komputera(plansza,computer,human):
    """Spowoduj wykonywanie ruchu przez komputer"""
    plansza=plansza[:]#kopia bo funkcja zmienia liste
    NAJLEPSZE_RUCHY=(4,0,2,6,8,1,3,5,7)
    print("Wybieram pole numer ")
    for move in prawidlowe_ruchy(plansza):
        plansza[move]=computer
        if winner(plansza)== computer:
            print(move)
            return(move)
            #Ten ruch zostal sprawdzony, wycofaj go
        plansza[move]=EMPTY
        #Jesli czlowiek moze wygrac zablokuj ruch
        for move in prawidlowe_ruchy(plansza):
            plansza[move]=human
            if winner(plansza)==human:
                print(move)
                return move
            #Ten ruch zostal juz sprawdzony wycofaj go
            plansza[move]=EMPTY
        for move in NAJLEPSZE_RUCHY:
             if move in prawidlowe_ruchy(plansza):
                 print(move)
                 return move
                 
def nastepny_ruch(turn):
    """Zmien wykonawce ruchu"""
    if turn==X:
        return O
    else:
        return X
        
def gratulacje_zwyciezcy(the_winner,computer,human):
    if the_winner!=TIE:
        print(the_winner,"jest zwyciezca\n")
    else:
        print("Remis\n")
    if winner==computer:
        print("Wygral komputer")
    elif winner==human:
        print("Czlowiek wygral")
    elif winner==TIE:
        print("Remis")
    
def main():
    instrukcja()
    computer,human=kogo_ruch()
    turn=X
    plansza=nowa_plansza()
    wyswietl_plansze(plansza)
    while not winner(plansza):
        if turn==human:
            move=ruch_czlowieka(plansza,human)
            plansza[move]=human
        else:
            movie=ruch_komputera(plansza,computer,human)
            plansza[movie]=computer
        wyswietl_plansze(plansza)
        turn=nastepny_ruch(turn)
    the_winner=winner(plansza)
    gratulacje_zwyciezcy(the_winner,computer,human)
            
main()
input("Aby zakonczyc nacisnij ENTER")
    
    
    
    
    
