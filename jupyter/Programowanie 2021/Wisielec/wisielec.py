class Wisielec():

    def rysuj_wisielca(etap):
        """
        Funkcja zwraca 'rysunek' wisielca w zależności od podanego etapu.
        Etapy 0-5.
        Finlany rysunek:

        _______
        |/    |
        |     O
        |    /|\ 
        |    / \ 
        |
        =========

        """
        if etap == 0:
            return '\n\n\n\n\n\n'
        if etap == 1:
            return '\n\n\n\n\n\n========='
        if etap == 2:
            return '\n|\n|\n|\n|\n|\n========='
        if etap == 3:
            return '_______\n|\n|\n|\n|\n|\n========='
        if etap == 4:
            return '_______\n|/\n|\n|\n|\n|\n========='
        if etap == 5:
            return '_______\n|/    |\n|     O\n|    /|\ \n|    / \ \n|\n========='
        if (etap < 0) or (etap > 5):
            return False

    def filtruj_hasla(lista_hasel):
        '''
        Funkcja zwraca przefiltrowaną listę z hasłami niezawierającymi znaków specjalnych, cyfr i spacji z przodu i z tyłu hasła.

        >>> filtruj_hasla(['kot', 'pies', 'chomik', 'ju'])
        ['kot', 'pies', 'chomik']
        >>> filtruj_hasla(['kot', 'pi4s', 'chomi#', 'ju'])
        ['kot']
        >>> filtruj_hasla([13, 'kot', 'pi4s', 'chomi7', 'ju'])
        ['kot']
        >>> filtruj_hasla(['13', 'kot', 'pi4s', 'chomi7', 'ju'])
        ['kot']
        >>> filtruj_hasla(['kot'])
        ['kot']
        >>> filtruj_hasla([])
        []
        '''

        przefiltrowana_lista = []

        if len(lista_hasel) >= 1:
            for haslo in lista_hasel:
                if type(haslo) == str:
                    if haslo[0] == " " or haslo[-1] == " ":
                        haslo = haslo.replace(" ", "")
                    if len(haslo) >= 3: 
                        haslo_male = haslo.lower()
                        if haslo_male.isalpha():
                            przefiltrowana_lista.append(haslo_male)
        return przefiltrowana_lista

    def funkcja_szyfrujaca_i_deszyfrujaca(slowo):
        """
        Funkcja szyfruje i deszyfruje hasła.
        >>> funkcja_szyfrujaca_i_deszyfrujaca('/12/0/3/6/13/')
        'jacek'
        >>> funkcja_szyfrujaca_i_deszyfrujaca('mercedes')
        '/16/6/22/3/6/5/6/23/'
        """

        alfabet = 'aąbcćdeęfghijklłmnńoóprsśtuwyzźż'
        litery = {
            'a': '0',
            'ą': '1',
            'b': '2',
            'c': '3',
            'ć': '4',
            'd': '5',
            'e': '6',
            'ę': '7',
            'f': '8',
            'g': '9',
            'h': '10',
            'i': '11',
            'j': '12',
            'k': '13',
            'l': '14',
            'ł': '15',
            'm': '16',
            'n': '17',
            'ń': '18',
            'o': '19',
            'ó': '20',
            'p': '21',
            'r': '22',
            's': '23',
            'ś': '24',
            't': '25',
            'u': '26',
            'w': '27',
            'x': '28',
            'y': '29',
            'z': '30',
            'ź': '31',
            'ż': '32',
                }
        wartosci = {
            '0': 'a',
            '1': 'ą',
            '2': 'b',
            '3': 'c',
            '4': 'ć',
            '5': 'd',
            '6': 'e',
            '7': 'ę',
            '8': 'f',
            '9': 'g',
            '10': 'h',
            '11': 'i',
            '12': 'j',
            '13': 'k',
            '14': 'l',
            '15': 'ł',
            '16': 'm',
            '17': 'n',
            '18': 'ń',
            '19': 'o',
            '20': 'ó',
            '21': 'p',
            '22': 'r',
            '23': 's',
            '24': 'ś',
            '25': 't',
            '26': 'u',
            '27': 'w',
            '28': 'x',
            '29': 'y',
            '30': 'z',
            '31': 'ź',
            '32': 'ż',
        }

        if slowo[0] == "/":
            wynik = ''
            znaki = slowo.split("/")
            for znak in znaki:
                if znak != "":
                    wynik += wartosci[znak]
            return wynik

        else:
            wynik = '/'
            for znak in slowo:
                wynik += litery[znak] + "/"
            return wynik


    def odczytaj_hasla_z_pliku(nazwa_pliku):
        '''
        Funkcja zwraca przefiltrowane hasła pobrane z pliku tekstowego.
        '''

        hasla = []

        with open(nazwa_pliku, mode='r') as plik:
            for linijka in plik:
                hasla += [linijka.replace('\n', '')]

        dekodowana = []

        for haslo in hasla:
            dekodowana += [Wisielec.funkcja_szyfrujaca_i_deszyfrujaca(haslo)]

        lista_hasel = Wisielec.filtruj_hasla(dekodowana)

        return lista_hasel


    def losuj_haslo(lista_hasel):

        '''
        Funkcja zwraca losowe hasło z listy haseł

        '''
        import random

        haslo = random.choice(lista_hasel)

        return haslo 

    def szyfruj_haslo(haslo, litery):
        '''
        Funkcja wraca zaszyfrowane hasło.
        Szyfruje wszystkie znaki oprócz spacji 
        i liter z argumentu 'litery'.

        >>> szyfruj_haslo('gosia','') 
        '_____'

        >>> szyfruj_haslo('gosia','so') 
        '_os__'

        >>> szyfruj_haslo('gosia', 'iasog')
        'gosia'


        '''
        przefiltrowane = ''
        for litera in haslo:
            if (litera in litery):
                przefiltrowane += litera
            else: 
                przefiltrowane += '_'

        zaszyfrowane_haslo = przefiltrowane


        return zaszyfrowane_haslo

    def poprawnosc_hasla(haslo):
        '''
        funkcja sprawdza poprawność podanego hasła
        >>> poprawnosc_hasla('haslo')
        True
        >>> poprawnosc_hasla('hasl0')
        False
        '''
        alfabet = 'aąbcćdeęfghijklłmnńoóprsśtuwyzźż'

        if len(haslo) == 0:
            return False

        for znak in haslo:
            if znak not in alfabet:
                return False
        return True

    def wisielec():
        #gra w wisielca
        wybor = "1"
        while wybor != "0":
            print("Witaj w grze w wisielca!")
            print("Menu:")
            print("1. Nowa gra")
            print("2. Instrukcja")
            print("0. Wyjście")
            wybor = str(input("Twój wybór: "))
            if wybor == "1":
                print("Wprowadź hasło lub wciśnij enter, a hasło zostanie wylosowane automatycznie.")
                odpowiedz = str(input("Twój wybór: ")).lower()
                if odpowiedz == '':
                    pula_hasel = Wisielec.odczytaj_hasla_z_pliku("hasla.txt")
                    haslo = Wisielec.losuj_haslo(pula_hasel)
                else:
                    if Wisielec.poprawnosc_hasla(odpowiedz):
                        haslo = odpowiedz
                    else:
                        print("Zaproponowałeś niepoprawne hasło. Hasło zostanie wylosowane automatycznie!")
                        pula_hasel = Wisielec.odczytaj_hasla_z_pliku("hasla.txt")
                        haslo = Wisielec.losuj_haslo(pula_hasel)
                # jak wpiszemy jedną literę to sprawdza litere, a jak więcej niż jedną to sprawdza hasło
                podane_litery = ""
                bledy = 0
                rozgrywka = True
                while rozgrywka == True:
                    print(f'Hasło: {Wisielec.szyfruj_haslo(haslo, podane_litery)}')
                    print(f'Podane litery: {podane_litery}')
                    print(f'Popełnione błędy: {bledy}/5')
                    print(Wisielec.rysuj_wisielca(bledy))
                    if bledy >= 5:
                        print("Przegrałeś!")
                        rozgrywka = False
                        break
                    print(f'Podaj literę lub odgadnij hasło:')
                    odpowiedz = str(input())

                    # Wyjście
                    if odpowiedz == "#":
                        rozgrywka = False
                        print("Dziękujemy za udział w grze.")
                        break

                    # Rozgrywka
                    if len(odpowiedz) == 1:
                        if odpowiedz not in podane_litery:
                            if odpowiedz in haslo:
                                podane_litery += odpowiedz
                                print(f'Brawo! Litera {odpowiedz} znajduje się w haśle!')
                                if Wisielec.szyfruj_haslo(haslo, podane_litery) == haslo:
                                    print(f'Gratulacje! hasło to {haslo}!')
                                    rozgrywka = False
                            else:
                                bledy += 1
                                print(f'Niestety! Litery {odpowiedz} nie ma w haśle!')
                                podane_litery += odpowiedz
                        else:
                            print(f'już podałeś literę {odpowiedz}!')
                    if len(odpowiedz) > 1:
                        if odpowiedz == haslo:
                            print(f'Gratulacje! hasło to {odpowiedz}!')
                            rozgrywka = False
                        else:
                            bledy += 1
                            print(f'Niestety! hasło to nie {odpowiedz}!')
            if wybor == "2":
                print("Instrukcja:")
                print("Wybierz pozycje z menu.")
                print("Po rozpoczęciu nowej gry wprowadź hasło, lub pozostaw pole puste a hasło wylosuje się z pliku.")
                print("Podczas rozgrywki możemy zgadywać poszczególne litery hasła, bądź od razu jego całość.")
                print("W każdym momencie możemy zrezygnować z rozgrywki po wpisaniu znaku '#'.")
                print("Rozgrywka zakończy się automatycznie w przypadku gdy:")
                print("- przekroczymy ilość prób odgadnięcia hasła bądź litery")
                print("- odgadniemy hasło")
                print("- odgadniemy wszystkie litery")
                print("W GRZE UŻYWAMY TYLKO MAŁYCH LITER, BEZ CYFR, SYMBOLI ORAZ SPACJI!!!")
                print("\n")
            if wybor == "0":
                print("Do widzenia!")
            if wybor not in "012":
                print("Nieprawidłowy wybór! Spróbuj jeszcze raz!")


