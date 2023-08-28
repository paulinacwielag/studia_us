#Igor Juraszek

def zamien_na_slowne(liczba_int):
    
    liczba = str(liczba_int)
    liczba_slownie = ''
    
    # 1 do 20
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
            
            # usuwanie ewentualnej spacji na końcu
            if liczba_slownie[-1] == ' ':
                liczba_slownie = liczba_slownie[:-1]
        
        return liczba_slownie

# test działania funkcji / wykonanie polecenia czy coś
    
liczby_do_zamienienia = [1, 3, 52, 1234, 742, 106, 2137, 997, 18, 93]
zamienione_liczby = []

for liczba in liczby_do_zamienienia:
    zamienione_liczby += [zamien_na_slowne(liczba)]


print(liczby_do_zamienienia)
print(zamienione_liczby)


# testy
def test_suite_zamien_na_slowne():
    dane_testowe = [
        (1, 'jeden'),
        (3, 'trzy'),
        (52, 'pięćdziesiąt dwa'),
        (1234, 'tysiąc dwieście trzydzieści cztery'),
        (742, 'siedemset czterdzieści dwa'),
        (106, 'sto sześć'),
        (2137, 'dwa tysiące sto trzydzieści siedem'),
        (997, 'dziewięćset dziewięćdziesiąt siedem'),
        (18, 'osiemnaście'),
        (93, 'dziewięćdziesiąt trzy'),  
    ]
    for wartosc, spodziewany_wynik in dane_testowe:
        test = zamien_na_slowne(wartosc)
        assert test == spodziewany_wynik, f'Błąd: zamien_na_slowne({wartosc}) != {spodziewany_wynik}'
        
        
test_suite_zamien_na_slowne()