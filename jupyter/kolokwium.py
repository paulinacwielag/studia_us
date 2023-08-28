class Tekst:
    '''Klasa Tekst'''
    
    def __init__(self, tekst):
        self.set_tekst(tekst)
        
    def get_tekst(self):
        return self.tekst
    
    def set_tekst(self, var):
        if Tekst.sprawdz_czy_tekst(var) == True:
            self.tekst = var
        else:    
            return 'tekst musi być STR'
        
    def sprawdz_czy_tekst(tekst):
        '''Funkcja sprawdza, czy argument jest tekstem.
        
        >>> Tekst.sprawdz_czy_tekst('paulina aniluap 123')
        True
        >>> Tekst.sprawdz_czy_tekst(75862)
        False
        '''
        if isinstance(tekst, str):
            return True
        else:
            return False
        
    def suma(self):
        '''Funkcja sumuje cyfry zawarte w tekście.
        
        >>> t3 = Tekst("Jola 8 Krysia 7 Antek 5")
        >>> t3.suma()
        20
        >>> t4 = Tekst('7777')
        >>> t4.suma()
        28
        '''
        lista_liczb = []
        cyfry = '1234567890'
        tekst = self.tekst
        for znak in tekst:
            if znak in cyfry:
                lista_liczb += [int(znak)]
        return sum(lista_liczb)
    
    def zapisz(self, nazwa_pliku):
        '''Funkcja zapisuje teskt do pliku.
        
        >>> t = Tekst("Ala ma kota")
        >>> t.zapisz('ala.txt')
        >>> plik = open('ala.txt')
        >>> plik.read() == 'Ala ma kota'
        True
          
        '''
        tekst = self.get_tekst()
        with open(nazwa_pliku, mode='w') as plik:
            plik.write(tekst)
    
    def __repr__(self):
        return f'tekst: {self.get_tekst()}'
    
    def __str__(self):
        return self.__repr__()
    
def rozdziel(lista):
    '''Funkcja dodaje do list poszczególne liczby w zależności, czy są dodatnie, ujemne czy są zerami. W przypadku zer poakzuje, ile zer znajdowało się w liście.
    
    >>> rozdziel([1, 2, 3, -1, -2, -3, 0,  0, 0])
    {'+': [1, 2, 3], '-': [-1, -2, -3], '0': 3}
    >>> rozdziel([])
    
    >>> rozdziel([0.0, 4.0, -10.0])
    {'+': [4.0], '-': [-10.0], '0': 1}
    >>> rozdziel([4, 5, 6])
    {'+': [4, 5, 6], '-': [], '0': 0}
    >>> rozdziel([0.0, 0, 0.0, 0])
    {'+': [], '-': [], '0': 4}
    >>> rozdziel([-8, -9, -1000])
    {'+': [], '-': [-8, -8, -1000], '0': 0}
    '''
    el_liczbowe = 0
    dodatnie = []
    ujemne = []
    zera = []
    if len(lista) == 0:
        return None
    for el in lista:
        if isinstance(el, (int, float)):
            el_liczbowe += 1
            if el > 0:
                dodatnie += [el]
            elif el == 0 or el == 0.0:
                zera += [el]
            else:
                ujemne += [el]
    if el_liczbowe == 0:
        return None
    slownik = {'+': dodatnie,
               '-': ujemne,
               '0': len(zera)
              }
    return slownik