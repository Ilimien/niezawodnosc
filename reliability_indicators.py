"""
@author: Łukasz Nizioł

"""

import matplotlib.pyplot as plt

def Dystrybuanta(n,t,m): #dystrybuanta empiryczna
    F = [m[0]/n] #pierwszy element
    num = m[0] #licznik pierwszego równania
    
    for i in range (1,len(m)):
        num = num+m[i] #licznik i-tego równania
        F.append(round(num/n,3)) #dodanie wartości dystrybuanty do tablicy
    return F

def Rt(n,t,m): # empiryczna funkcja niezawodności
    
    R= [n/n] #funkcja niezawodności dla pierwszego dt
    num = n #licznik pierwszego równania
    for i in range (1,len(m)):
        num = num-m[i]  #licznik i-tego równania
        R.append(round(num/n,3)) #dodanie wartości dystrybuanty do tablicy
    return R
    
def Gestosc_praw(n,t,m): #funkcja gęstości prawdopodobieństwa
    ft=[0] #funkcja niezawodności dla t1
    for i in range (1,len(m)-1):
        ft.append(round(m[i]/(n*(t[i]-t[i-1])),3)) #dodanie wartości gęstości prawdopodobieństwa
    return ft

def suma_m(i,m): #suma uszkodzonych elementów
    suma = 0
    for j in range (0,i):
        suma = suma+m[j]
    return suma

def intens(n,t,m): #funkcja intensywności uszkodzeń
    lamb=[0] #pierwszy element tablicy - funkcja dla t1

    for i in range (1,len(m)-1):
        den = (n-suma_m(i,m))*(t[i]-t[i-1]) #mianownik równania funkcji intensywności
        lamb.append(round(m[i]/den,3)) #dodanie wartości funkcji intensywności do tablicy
    return lamb

def rozklad(F,t): #wartosc oczekiwana trwałości elementów
    ET=0 #zadeklarowanie wartości trwałości
    for i in range(0,len(t)-1):
        ET=ET+(F[i+1]-F[i])*t[i] #obliczenie na podstawie empirycznej dystrybuanty
    return round(ET,3)

def Inicjalizacja():
    
    print("Wprowadź dane inicjalizujące program. Zostaniesz poproszony/a o decyzję czy użyć gotowych danych. Napisz tak jesli mają zostać wczytane.")
    if str(input("Czy wykorzystać dane z przykładu 5.1?: "))==("tak"):
        """Przykład 5.1, strona 209 Niezawodność urządzeń elektrycznych, M. Prażewska"""
        n = 35 #liczność
        t = [1,2,3,4,5,6,7,8,9,10] #jednostka czasu wykonywania eksperymentu
        m = [0,3,3,5,8,7,6,2,1,0] #liczba elementów uszkodoznych
    else:
        t=[] #pusty wektor - deklaracja czasu
        m=[] #pusty wektor - deklaracja elementów uszkodzonych
        print("Zostaniesz poproszony/a o podanie licznośći. Podanie liczby ujemnej jest traktowane jako błąd i zostanie automatycznie poprawione.")
        try:
            n = int(input("Wprowadź liczność: "))
        except:
            n = input("Wprowadź liczność - tylko liczby całkowite: ")
            while type(n)!=int:
                n = input("Wprowadź liczność - tylko liczby całkowite: ")
                try: 
                    n=abs(int(n)) #Zamiana na liczbę dodatnią
                except:
                    pass
        print("Zostaniesz poproszony/a o podanie czasu trwania eksperymentu. Podanie liczby ujemnej jest traktowane jako błąd i zostanie automatycznie poprawione.")
        try:
            tk = int(input("Podaj czas trwania eksperymentu: "))
        except:
            tk = input("Podaj czas trwania eksperymentu - tylko liczby całkowite: ")
            while type(tk)!=int:
                tk = input("Podaj czas trwania eksperymentu - tylko liczby całkowite: ")
                try: 
                    tk=abs(int(tk)) #Zamiana na liczbę dodatnią
                except:
                    pass
        print("Zostaniesz poproszony/a o podanie poszczególnych elementów. Podanie liczby ujemnej jest traktowane jako błąd i zostanie automatycznie poprawione.")
        for i in range (0,tk):
            t.append(i+1)
            try:
                mk = float(input("Wprowadz kolejny element m: "))
            except:
                mk = input("Wprowadz kolejny element m - tylko liczby typu float: ")
                while type(mk)!=float:
                    mk = input("Wprowadz kolejny element m - tylko liczby typu float: ")
                    try:
                        mk=float(mk)
                        if mk<0:
                            mk=-mk #Zamiana na liczbę dodatnią
                    except:
                        pass
            m.append(mk)
    return n,t,m

"""Funkcje rysujące przebiegi"""

def PlotFt(F,t): #Wizualizacja dystrybuanty
    plt.plot(t,F) #funkcja wykresu
    plt.xlabel('Czas trwania t') #podpisanie osi x
    plt.ylabel('Dystrybuanta F(t)') #podpisanie osi y
    plt.title('Dystrybuanta empiryczna') #tytuł wykresu
    plt.grid() #ustawienie siatki
    plt.show() #wywołanie wykresu

def PlotRt(R,t): #wizualizacja funkcji R(t)
    plt.plot(t,R) #funkcja wykresu
    plt.xlabel('Czas trwania t') #podpisanie osi x
    plt.ylabel('R(t)') #podpisanie osi y
    plt.title('Empiryczna funkcja niezawodności R(t)') #tytuł wykresu
    plt.grid() #ustawienie siatki
    plt.show() #wywołanie wykresu

def Plotftt(ft,t): #wizualizacja gęstości prawdopodobieństwa f(t)
    plt.plot(t[0:9],ft) #funkcja wykresu
    plt.xlabel('Czas trwania t') #podpisanie osi x
    plt.ylabel('Gęstość prawdopodobieństwa f(t)') #podpisanie osi y
    plt.title('Empiryczna gęstość prawdopodobieństwa') #tytuł wykresu
    plt.grid() #ustawienie siatki
    plt.show() #wywołanie wykresu
    
def Plotlambdat(lamb,t):
    plt.plot(t[0:9],lamb) #funkcja wykresu
    plt.xlabel('Czas trwania t') #podpisanie osi x
    plt.ylabel('Intensywnośc uszkodzeń λ(t)') #podpisanie osi y
    plt.title('Funkcja intensywności uszkodzeń') #tytuł wykresu
    plt.grid()
    plt.show() #wywołanie wykresu
    
def Porownanie(F,R,t):
    plt.subplot(2, 1, 1) #ustawienie położenia wykresu
    plt.title("F(t) oraz R(t) - porównanie") #tytuł wykresu
    plt.plot(t,F) #funkcja wykresu
    plt.xlabel('Czas trwania t') #podpisanie osi x
    plt.ylabel('Dystrybuanta F(t)') #podpisanie osi y
    plt.grid() #ustawienie siatki
    plt.legend(['Dystrybuanta']) #legenda
    plt.subplot(2, 1, 2) #ustawienie położenia wykresu
    plt.plot(t,R) #funkcja wykresu
    plt.xlabel('Czas trwania t') #podpisanie osi x
    plt.ylabel('R(t)') #podpisanie osi y
    plt.grid() #ustawienie siatki
    plt.legend(['Niezawodność']) #legenda
    plt.show() #wywołanie wykresu

def Poczatek(t,m):
    plt.stem(t,m)
    plt.grid()
    plt.xlabel('Czas trwania t')
    plt.ylabel('Ilość uszkodoznych elementów')
    plt.show()
    
"""Część główna programu"""

def main():
    print("Podstawy niezawodności. Projekt zaliczeniowy. Łukasz Nizioł, Marcin Supa \n")
    n,t,m=Inicjalizacja() #inicjalizacja wartości
    Poczatek(t,m)
    F = Dystrybuanta(n,t,m) #funkcja obliczająca dystrybuantę empiryczną
    print("Dystrybuanta F(t): \n",F) #Dystrybuanta F(t)
    PlotFt(F, t) #wizualizacja
    R=Rt(n,t,m) #wartości funkcji niezawodności
    print("\nFunkcja niezawodności R(t): \n",R)
    PlotRt(R, t) #wizualizacja
    Porownanie(F, R, t)
    ft = Gestosc_praw(n,t,m) #wartości funkcji gęstości prawdopodobieństwa
    print("\nFunkcja gęstości prawdopodobieństwa f(t): \n",ft)
    Plotftt(ft,t)
    lamb = intens(n,t,m) #wartości intensywności uszkodzeń
    print("\nFunkcja intensywności uszkodzeń: \n", lamb)
    Plotlambdat(lamb,t)
    ET = rozklad(F,t) #wartosc oczekiwana trwałości elementów
    print("\nWartosc oczekiwana trwałości elementów: \n",ET)
    
main()