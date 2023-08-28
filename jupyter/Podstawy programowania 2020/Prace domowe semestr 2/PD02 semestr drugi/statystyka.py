"""
Moduł statystyka służy do obliczania podstawowych wielkości statystycznych 
w oparciu o listy liczb (INT, FLOAT)
"""
from numseq import *
import numseq

def srednia_harmoniczna(L):
    'Funkcja oblicza srednia harmoniczna'
    
    dlugosc_listy = numseq.dlugosc(L)

    suma = 0
    for element in L:
        suma += 1/element
        
    srednia = dlugosc_listy / suma
    return srednia


def srednia_arytmetyczna(L):
    """Funkcja oblicza średnią arytmetyczną"""
    wynik=numseq.suma(L)/numseq.dlugosc(L)
    return wynik


def kwartyl(L):
    kwartyl1= dlugosc(L)/4
    return kwartyl1


def srednia_kwadratowa(lista_elementow):
    'Funkcja oblicza srednią kwadratowa elementów z listy'
    
    dlugosc_listy = numseq.dlugosc(L)

    suma = 0
    for element in lista_elementow:
        suma += element ** 2
        
    srednia = (suma / dlugosc_listy) ** (1/2)
    return srednia

def modalna(L):
    def ileWystapien(liczba):
        licznik = 0
        for i in L:
            if i == liczba:
                licznik += 1
        return licznik
   
    def najwieksza(lista):
        naj = lista[0]
        for i in lista:
            if i > naj:
                naj = i
        return naj
   
    zbior = set(L)
    output = dict()
 
    for i in zbior:
        output[i] = ileWystapien(i)
 
    print([(output[k]) for k in output])
    return najwieksza([(output[k]) for k in output])

def srednia_geometryczna(L):
    '''Srednia geometryczna liczb z listy L.'''
    srednia = 1
    n = numseq.dlugosc(L)
    for el in L:
        srednia *= el
        returtn (srednia) ** (1/n)