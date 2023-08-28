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


def podziel_na_podciagi(L, m=2):
    """
    Funkcja zwraca listę wszystkich podciągów ciągu L o dlugosci m=2 lub większej
    """
    podciagi = []
    for dlugosc in range(m, len(L) + 1):  # 2, 3, 4, ..., n
        podciagi.extend(podziel_na_n_elementowe_podciagi(L, dlugosc))
    return podciagi


def podciagi(L):
    """
    Funkcja zwraca słownik rosnących, malejących i stałych 
    podciągów ciągu L o dlugosci 2 lub wiekszej.
    """
    ret = {}
    podciagi = podziel_na_podciagi(L, 2)
    
    rosnace = []
    malejace = []
    stale = []
    for ciag in podciagi:
        if czy_rosnacy(ciag):
            rosnace.append(ciag)
        if czy_malejacy(ciag):
            malejace.append(ciag)
        if czy_staly(ciag):
            stale.append(ciag)
            
    ret['rosnace'] = rosnace
    ret['malejace'] = malejace
    ret['stale'] = stale
    return ret


for L in ([1, 2, 3, 4], [1, 3, 4, 2, 2]):
    print(L, podciagi(L), sep=' -> ')
    
def odwroc(L):
    'Funkcja odwraca liste wspak'
    
    odwrocona = L[::-1]
    return odwrocona

def najmniejszy(L):
    'Zwraca najmniejszy element ciągu'
    
    ret = 0
    for el in L:
        if L[0] == el:
            ret = el
        else:
            if el < ret:
                ret = el
    
    return ret

def suma(lista):
    output = 0
    for i in lista:
         output =+ i
    return output

def wieksze(n,L):
    """funkcja zwraca elementy ciągu L większe od n"""
    lista_wieksze=[]
    for el in L:
        if el>n:
            lista_wieksze.append(el)
    return lista_wieksze

def sumaa(lista):
    'Funkcja zwraca sume wyrazów listy L'
    output = 0
    for i in lista:
         output =+ i
    return output

def calkowita(L):
    lista=[]
    for el in L:
        if type(el)==int:
            lista.append(el)
    return lista

def odwrooc(L):
    'Funkcja zwraca listę odwróconą wspak.'
    
    odwrocona_lista = L[::-1]
    return odwrocona_lista

def dlugosc(L): 
    i = 0    
    for a in L: 
        i += 1
    return i 

def najwiekszy(L):
    """Funkcja zwraca największy element listy"""
    najwieksza_liczba = L[0]
    for element in L:
        if element > najwieksza_liczba:
            najwieksza_liczba = element
    return najwieksza_liczba

def najwieksza(L):
    """Funkcja zwraca największy element listy"""
    x=0
    for element in L:
        if L[0]==element:
            x=element
        else: 
            if element>x:
                x=element
    return x

def mniejsze(n,L):
    'funkcja zwraca elementy ciągu L mniejsze niż n'
    elementy_mniejsze = []
    for el in L:
        if el < n:
            elementy_mniejsze.append(el)
    return elementy_mniejsze

def calkowita(L):
    """funkcja zwraca elementy ciągu L typu int"""
    lista = []
    for el in L:
        if type(el) == int:
            lista.append(el)
    return lista

def tylko_liczby(L):
    '''zwraca kopię ciągu L filtrując elementy nieliczbowe (int float)'''
    lista=[]
    for i in L:
        if type(i)==int or type(i)==float :
            lista.append(i)
    return lista

def tylko_liczby_2(L):
    lis=[]
    for i in L:
        if type(i)==int or type(i)==float :
            lis.append(i)
    return lis