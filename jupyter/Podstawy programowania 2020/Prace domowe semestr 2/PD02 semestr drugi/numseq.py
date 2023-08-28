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
