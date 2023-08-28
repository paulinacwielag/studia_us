def podziel_na_n_elementowe_podciagi(L, n):
    ret = []
    for start in range(len(L) - n + 1):
        ret.append(L[start:start+n])
    return ret

def czy_malejacy(L):
    for idx in range(len(L) - 1):
        if L[idx] <= L[idx+1]:
            return False
    return True

def czy_staly(L):
    for idx in range(len(L) - 1):
        if L[idx] != L[idx+1]:
            return False
    return True


def czy_rosnacy(L):
    for idx in range(len(L) - 1):
        if L[idx] >= L[idx+1]:
            return False
    return True


def czy_niemalejacy(L):
    for idx in range(len(L) - 1):
        if L[idx] > L[idx+1]:
            return False
    return True

def czy_nierosnacy(L):
    for idx in range(len(L) - 1):
        if L[idx] < L[idx+1]:
            return False
    return True

def czy_naprzemienny(L):
    for idx in range(len(L) - 2):
        if (czy_nierosnacy(L[idx:idx+2]) and czy_nierosnacy(L[idx+1:idx+3])
           or
            czy_niemalejacy(L[idx:idx+2]) and czy_niemalejacy(L[idx+1:idx+3])
           ):
            return False
    return True

def dlugosc(L):
    'zwraca dlugość ciągu L'
    
    dlugosc = 0
    for element in L:
        dlugosc += 1
        
    return dlugosc


def najwiekszy(L):
    'zwraca największy element ciągu L'
    
    najwiekszy = L[0]
    for element in L:
        if element > najwiekszy:
            najwiekszy = element
            
    return najwiekszy

def najmniejszy(L):
    'zwraca największy element ciągu L'
        
    najmniejszy = L[0]
    for element in L:
        if element < najmniejszy:
            najmniejszy = element
            
    return najmniejszy

def tylko_liczby(L):
    'zwraca kopię ciągu L filtrując elementy nieliczbowe (zostawia INT i FLOAT)'
    
    kopia_L = []
    for element in L:
        if isinstance(element, (float, int)):
            kopia_L += [element]
    
    return kopia_L


def odwroc(L):
    'zwraca kopię ciągu L, ale w kolejności odwrotnej do oryginału'
    
    odwrocone_L = L[::-1]
    
    return odwrocone_L


def suma(L):
    'zwraca sumę wyrazów ciągu L'
    
    suma = 0
    for element in L:
        suma += element
        
    return suma


def zmiennoprzecinkowe(L):
    'zwraca elementy ciągu L typu FLOAT'
    
    kopia_L = []
    for element in L:
        if isinstance(element, float):
            kopia_L += [element]
    
    return kopia_L



def calkowite(L):
    'zwraca elementy ciągu L typu INT'
    
    kopia_L = []
    for element in L:
        if isinstance(element, int):
            kopia_L += [element]
    
    return kopia_L


def wieksze(n, L):
    'zwraca elementy liczbowe ciągu L większe od n'
    
    kopia_L = []
    for element in L:
        if element > n:
            kopia_L += [element]
    
    return kopia_L



def mniejsze(n, L):
    'zwraca elementy liczbowe ciągu L mniejsze od n'
    
    kopia_L = []
    for element in L:
        if element < n:
            kopia_L += [element]
    
    return kopia_L



def znajdz(n, L):
    'zwraca listę indeksów wszystkich elementów ciągu L równych n (patrz PD z podstaw programowania)'
    
    indeksy = []
    
    for indeks, element in enumerate(L):
        if element == n:
            indeksy += [indeks]
            
    return indeksy

def iloczyn(L):
    'funkcja zwraca iloczyn wszystkich liczbowych elementów listy'
    iloczyn = 1
    for element in L:
        if isinstance(element, (int, float)):
            iloczyn *= element
    return iloczyn

def iloraz(L):
    'funkcja zwraca iloraz wszystkich niezerowych liczbowych elementów listy'
    kopia_listy = []
    for element in L:
        if isinstance(element, (int, float)) and element != 0.0 and element != 0:
            kopia_listy += [element]
    if dlugosc(kopia_listy) > 0:
        iloraz = kopia_listy[0] 
        for element in kopia_listy[1:]:
            iloraz = iloraz / element
        return iloraz
    else:
        return 0.0

def wartosc_bezwzgledna(L):
    'funkcja zwraca kopię wartości bezwzględnych listy `L`'
    kopia_listy = []
    for element in L:
        if element >= 0:
            kopia_listy += [element]
        else:
            kopia_listy += [-(element)]
    return kopia_listy

def suma_par(A, B):
    'zwraca listę sum elementów o przystających indeksach list liczb A, B'
    if dlugosc(A) == dlugosc(B):
        lista = []
        for indeks in range(dlugosc(A)):
            lista += [A[indeks] + B[indeks]]
        return lista
    else:
        return 'listy nie są równej długości'
    
def iloczyn_par(A, B):
    'funkcja zwracająca listę iloczynów elementów o przystających indeksach list liczb A, B'
    if dlugosc(A) == dlugosc(B):
        lista = []
        for indeks in range(dlugosc(A)):
            lista += [A[indeks] * B[indeks]]
        return lista
    else:
        return 'listy nie są równej długości'
    
def bezwzgledna_roznica_par(A, B):
    'funkcja zwracająca listę bezwzględnych wartości różnic elementów o przystających indeksach list liczb A, B'
    if dlugosc(A) == dlugosc(B):
        lista = []
        kopia_listy = []
        for indeks in range(dlugosc(A)):
            lista += [A[indeks] - B[indeks]]
        for element in lista:
            if element >= 0:
                kopia_listy += [element]
            else:
                kopia_listy += [-(element)]
        return kopia_listy
    else:
        return 'listy nie są równej długości'
    
def czy_palindrom(L):
    'zwracająca True gry lista L jest palindromem lub False gry nie jest'
    odwrocona = odwroc(L)
    if odwrocona == L:
        return True
    else:
        return False
    
def potegi(L, n):
    'zwracająca kopię listy L z elementami liczbowymi podniesionymi do potęgi n'
    lista_liczb = tylko_liczby(L)
    kopia_listy = []
    for element in lista_liczb:
        kopia_listy += [element ** n]
    return kopia_listy

def czy_krecony_palindrom(L):
    '''
    funkcja sprawdza
    
    >>> czy_krecony_palindrom([1, 2, 1])
    True
    >>> czy_krecony_palindrom([2, 1, 1])
    True
    >>> czy_krecony_palindrom([1, 2, 3])
    False
    '''
    
    lista = L
    powtorzenia = dlugosc(L)
    for powtorzenie in range(powtorzenia):
        ostatni_element = lista[-1]
        kopia_listy = lista[:-1]
        kopia_listy.insert(0, ostatni_element)
        lista = kopia_listy
        if czy_palindrom(lista):
            return True
    return False

def znajdz_wzorzec(L, wzorzec):
    '''
    bool, czy lista wzorzec jest podciągiem listy L
    
    >>> znajdz_wzorzec([1, 2, 3, 4, 5], [3, 4])
    True
    >>> znajdz_wzorzec([1, 2, 3, 4, 5], [4, 5, 6, 7])
    False
    >>> znajdz_wzorzec([1, 2, 3, 4, 5], [1, 3, 2])
    False
    '''
    
    lista_podciagow = podziel_na_n_elementowe_podciagi(L, dlugosc(wzorzec))
    for podciag in lista_podciagow:
        if podciag == wzorzec:
            return True
    return False

def podzial(L):
    '''
    sprawdza, czy da się podzielić listę na dwie nieprzekrywające się podlisty o równej sumie elementów; 
    gdy się da - zwraca obie podlisty, gdy się nie da, zwraca None
    
    >>> podzial([1, 2, 3, 6])
    ([1, 2, 3], [6])
    >>> podzial([-1, 2, -3, 4])
    ([-1, 2], [-3, 4])
    >>> podzial([6, 2, 1, 3])
    ([6], [2, 1, 3])
    >>> podzial([6, 2, 1])
    None
    '''
    for indeks in range(dlugosc(L) - 1):
        czesc1 = L[0:indeks + 1]
        czesc2 = L[indeks + 1:]
        if suma(czesc1) == suma(czesc2):
            return czesc1, czesc2
    return None

def rozdziel_na_podlisty(L, dlugosc_podciagu=2, rozdzielne=True):
    '''
    rozdziela listę L na nieprzekrywające się (rozdzielne=True) lub przekrywające się (rozdzielne=False) 
    podlisty o długości dlugosc (domyślnie dwuelementowe), ale tylko gdy mamy wystarczającą ilość elementów; 
    jeżeli parametr rozdzielne=True to zwracane podlisty powinny być rozdzielne, jeżeli =False to należy zwrócić 
    wszystkie podlisty, rozpoczynając od każdego możliwego indeksu listy L i elementy podlist będą na siebie nachodzić
    
    >>> rozdziel_na_podlisty([1, 2, 3, 4, 5, 6])
    [[1, 2], [3, 4], [5, 6]]
    >>> rozdziel_na_podlisty([1, 2, 3, 4, 5, 6], dlugosc_podciagu=3)
    [[1, 2, 3], [4, 5, 6]]
    >>> rozdziel_na_podlisty([1, 2, 3, 4, 5, 6], dlugosc_podciagu=4)
    [[1, 2, 3, 4]]
    >>> rozdziel_na_podlisty([1, 2, 3, 4, 5, 6], dlugosc_podciagu=7)
    []
    >>> rozdziel_na_podlisty([1, 2, 3, 4, 5, 6], rozdzielne=False)
    [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]
    >>> rozdziel_na_podlisty([1, 2, 3, 4, 5, 6], dlugosc_podciagu=3, rozdzielne=False)
    [[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6]]
    >>> rozdziel_na_podlisty([1, 2, 3, 4, 5, 6], dlugosc_podciagu=4, rozdzielne=False)
    [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]
    >>> rozdziel_na_podlisty([1, 2, 3, 4, 5, 6], dlugosc_podciagu=7, rozdzielne=False)
    []
    '''
    
    if rozdzielne == True:
        dlugoscL = dlugosc(L)
        ilesiezmiesci = dlugoscL // dlugosc_podciagu

        lista_podciagow = []
        for podciag in range(ilesiezmiesci):
            od = dlugosc_podciagu * podciag
            do = dlugosc_podciagu * podciag + dlugosc_podciagu
            lista_podciagow += [L[od:do]]

        return lista_podciagow
    else:
        lista_podciagow = podziel_na_n_elementowe_podciagi(L, dlugosc_podciagu)
        return lista_podciagow
    
def rzymska(liczba):
    '''funkcja zamienia liczby zapisane cyframi arabskimi na liczby zapisane w systemie rzymskim'''
    
    rzymskie = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: "CD",
        100: 'C',
        90: "XC",
        50: 'L',
        40: "XL",
        10: 'X',
        9: "IX",
        5: 'V',
        4: 'IV',
        1: 'I'
    }
    
    liczba_rzymska = ''
    
    while liczba != 0:
        odejmowana = 0
        for element in rzymskie:
            if element <= liczba:
                odejmowana = element
                break
        liczba -= odejmowana
        liczba_rzymska += rzymskie[odejmowana]
    
    return liczba_rzymska
    
def system_rzymski(L):
    '''napisz funkcję zmieniającą całkowite liczby z listy L z systemu arabskiego na system rzymski (łaciński)
     w zakresie od 1 do 1000
     
     >>> system_rzymski([1, 10, 50, 51, 43, 124, 999])
     ['I', 'X', 'L', 'LI', 'XLIII', 'CXXIV', 'CMXCIX']
     '''
    
    rzymskie = []
    for element in L:
        rzymskie += [rzymska(element)]
    
    return rzymskie

def zamien_na_slowne(liczba_int):
    # współpraca z: Igor Juraszek
    
    liczba = str(liczba_int)
    liczba_slownie = ''
    
    od_1_do_20 = {
        '1': 'jeden',
        '2': 'dwa',
        '3': 'trzy',
        '4': 'cztery',
        '5': 'pięć',
        '6': 'sześć',
        '7': 'siedem',
        '8': 'osiem',
        '9': 'dziewięć',
        '10': 'dziesięć',
        '11': 'jedenaście',
        '12': 'dwanaście',
        '13': 'trzynaście',
        '14': 'czternaście',
        '15': 'piętnaście',
        '16': 'szesnaście',
        '17': 'siedemnaście',
        '18': 'osiemnaście',
        '19': 'dziewiętnaście',
        '20': 'dwadziescia',
    }
    
    jednosci = {
        '1': 'jeden',
        '2': 'dwa',
        '3': 'trzy',
        '4': 'cztery',
        '5': 'pięć',
        '6': 'sześć',
        '7': 'siedem',
        '8': 'osiem',
        '9': 'dziewięć',
    }
    
    dziesiatki = {
        '1': 'dziesięć',
        '2': 'dwadzieścia',
        '3': 'trzydzieści',
        '4': 'czterdzieści',
        '5': 'pięćdziesiąt',
        '6': 'sześćdziesiąt',
        '7': 'siedemdziesiąt',
        '8': 'osiemdziesiąt',
        '9': 'dziewięćdziesiąt',
    }
    
    setki = {
        '1': 'sto',
        '2': 'dwieście',
        '3': 'trzysta',
        '4': 'czterysta',
        '5': 'pięćset',
        '6': 'sześćset',
        '7': 'siedemset',
        '8': 'osiemset',
        '9': 'dziewięćset',
    }
    
    tysiace = {
        '1': 'tysiąc',
        '2': 'dwa tysiące',
        '3': 'trzy tysiące',
        '4': 'cztery tysiące',
        '5': 'pięć tysięcy',
        '6': 'sześć tysięcy',
        '7': 'siedem tysięcy',
        '8': 'osiem tysięcy',
        '9': 'dziewięć tysięcy',
    }
       
    
    if liczba_int <= 20:
        return od_1_do_20[liczba]
    else:
        for indeks, cyfra in enumerate(liczba[::-1]):
            if cyfra != '0':
                indeksy = {
                    '0': jednosci[cyfra],
                    '1': dziesiatki[cyfra],
                    '2': setki[cyfra],
                    '3': tysiace[cyfra],
                    }
                liczba_slownie = indeksy[str(indeks)] + " " + liczba_slownie
            

        if liczba_slownie[-1] == ' ':
             liczba_slownie = liczba_slownie[:-1]
        
        return liczba_slownie
    
def slownie(L):
    '''funkcja zmieniającą całkowite liczby z listy L na wersję słowną w zakresie od 1 do 1000'''
    
    lista_slownie = []
    for element in L:
        if element < 0 or element > 1000:
            return f'Element {element} nie mieści się w zakresie.'
        lista_slownie += [zamien_na_slowne(element)]
    return lista_slownie