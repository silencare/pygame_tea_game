import pygame, json
from random import randint
from ustawienia import SCALE, WIDTH_HEIGHT

pygame.init()

screen = pygame.display.set_mode((WIDTH_HEIGHT))
pygame.display.set_caption(f"Flower Tea")

#import obrazków
tlo_w_sklepie_img = pygame.image.load(f'img/tlo_w sklepie.png').convert()
tlo_zbieranie_img = pygame.image.load(f'img/tlo_zbieranie.png').convert()
tlo_rozwidlenie_img = pygame.image.load(f'img/mapacz1.png').convert()
tlo_przed_domem_img = pygame.image.load(f'img/mapacz2.png').convert()
tlo_przed_sklepem_img = pygame.image.load(f'img/mapacz3.png').convert()
tlo_domek_img = pygame.image.load(f'img/dom_środek/dom_środek.png').convert()
tlo_sklep_img = pygame.image.load(f'img/tlo_sklep.png').convert()
tlo_ekwipunek_img = pygame.image.load(f'img/tlo_ekwipunek.png').convert()
tlo_maszyna1_img = pygame.image.load(f'img/maszyna1/tlo_maszyna1.png').convert() 

krzak_obraz_img1 = [pygame.image.load(f'img/krzak1.png').convert_alpha(), pygame.image.load(f'img/krzak2.png').convert_alpha()]
kwiatek_obraz_img = [pygame.image.load(f'img/kwiatek/kwiatek.png').convert_alpha(), pygame.image.load(f'img/kwiatek/kwiatek2.png').convert_alpha(), pygame.image.load(f'img/kwiatek/kwiatek3.png').convert_alpha(), pygame.image.load(f'img/kwiatek/kwiatek4.png').convert_alpha()]
strzalka_dol_img = [pygame.image.load(f'img/strzalka_dol/strzałka_dol.png').convert_alpha(), pygame.image.load(f'img/strzalka_dol/strzalka_dol2.png').convert_alpha(), pygame.image.load(f'img/strzalka_dol/strzalka_dol3.png').convert_alpha()]
strzalka_gora_img = [pygame.image.load(f'img/strzalka_gora/strzałka_gora.png').convert_alpha(), pygame.image.load(f'img/strzalka_gora/strzalka_gora2.png').convert_alpha(), pygame.image.load(f'img/strzalka_gora/strzalka_gora3.png').convert_alpha()]
strzalka_lewo_img = [pygame.image.load(f'img/strzalka_lewo/strzalka_lewo1.png').convert_alpha(), pygame.image.load(f'img/strzalka_lewo/strzalka_lewo2.png').convert_alpha(), pygame.image.load(f'img/strzalka_lewo/strzalka_lewo3.png').convert_alpha()]
strzalka_prawo_img = [pygame.image.load(f'img/strzalka_prawo/strzałka_prawo.png').convert_alpha(), pygame.image.load(f'img/strzalka_prawo/strzalka_prawo2.png').convert_alpha(), pygame.image.load(f'img/strzalka_prawo/strzalka_prawo3.png').convert_alpha()]

maszyna1_img = pygame.image.load(f'img/maszyna1.png').convert_alpha()
maszyna2_img = pygame.image.load(f'img/maszyna2.png').convert_alpha()
maszyna3_img = pygame.image.load(f'img/maszyna3.png').convert_alpha()
maszyna4_img = pygame.image.load(f'img/maszyna4.png').convert_alpha()

moneta_img = pygame.image.load(f'img/moneta.png').convert_alpha()
koszyk_img = pygame.image.load(f'img/koszyk.png').convert_alpha()
ziola_img = pygame.image.load(f'img/maszyna1/ziola.png').convert_alpha()
herbata_img= pygame.image.load(f'img/maszyna2/herbata.png').convert_alpha()
ramka_interfejs_img = pygame.image.load(f'img/ramka_interfejs.png').convert_alpha()
maszyna1_kwiatek_img = [pygame.image.load(f'img/maszyna1/1kwiatek.png').convert_alpha(), pygame.image.load(f'img/maszyna1/2kwiatek.png').convert_alpha(), pygame.image.load(f'img/maszyna1/3kwiatek.png').convert_alpha(), pygame.image.load(f'img/maszyna1/4kwiatek.png').convert_alpha()]
maszyna1_tluczek_img = pygame.image.load(f'img/maszyna1/tluczek.png').convert_alpha()
maszyna1_widelec_img = pygame.image.load(f'img/maszyna1/widelec.png').convert_alpha()
tlo_guzik_img = pygame.image.load(f'img/tlo_guzik.png').convert()

#zmienne globalne
global dane
global ilosc_kwiatkow
global ilosc_monet
global ilosc_barwnikow
global ilosc_wywarow
global ilosc_herbaty
global zebrane_kwiaty
global nazwa_sceny

dane = {
    'ilosc_kwiatkow': 0,
    'ilosc_monet': 0,
    'ilosc_barwnikow': 0,  # 4maszyna
    'ilosc_wywarow': 0,    # 3maszyna
    'ilosc_herbaty': 0,    # 2maszyna
    'ilosc_ziol': 0,       # 1maszyna
    'zebrane_kwiaty': 0,
    'nazwa_sceny': 0
}

with open('dane.txt') as plik_dane:
    dane = json.load(plik_dane)

#klasy

#podstawowe tworzenie i wyświetlanie strzalek

class Element():
    def __init__(self, img, x, y):
        self.img = img
        self.rect = img.get_rect()
        self.x = x
        self.y = y

    def draw(self):
        screen.blit(self.img, (self.x, self.y))

    def touch(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.rect.width:
            if pos[1] > self.y and pos[1] < self.y + self.rect.height:
                return True
            
        return False

class Strzalka(Element):
    def __init__(self, img, x, y):
        self.num = 0
        self.img = img
        self.rect = img[self.num].get_rect()
        self.x = x
        self.y = y
        
    def draw(self):
        screen.blit(self.img[round(self.num)], (self.x, self.y))
        self.num += 0.5
        if self.num >= 3:
            self.num = 0

    def touch(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.rect.width:
            if pos[1] > self.y and pos[1] < self.y + self.rect.height:
                return True
            
        return False

class Krzak():
    def __init__(self, x, y):
        self.num = 0
        self.max_num = 1.5
        self.x = x
        self.y = y
        self.img = krzak_obraz_img1
        self.rect = self.img[self.num].get_rect()
        self.stan = 0
    
    def draw(self):
        if self.stan == 0:
            pass
        else:
            self.img = kwiatek_obraz_img
            self.max_num = 3.5

        screen.blit(self.img[round(self.num)], (self.x, self.y))
        self.num += 0.25
        if self.num >= self.max_num:
            self.num = 0

    def czary(self, ilosc):
        global dane
        if self.stan == 0:
            tak = randint(0, 2)
            if tak == 0:
                self.x = -500
                print(dane["ilosc_kwiatkow"])
            else:
                self.stan = 1
        elif self.stan == 1:
            dane["ilosc_kwiatkow"] += ilosc
            dane["zebrane_kwiaty"] += ilosc
            self.x = -500
            print(dane["ilosc_kwiatkow"])

    
    def touch(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.rect.width:
            if pos[1] > self.y and pos[1] < self.y + self.rect.height:
                return True
            
        return False




######################################################################
def menu():
    pass

#########################################################################
def ekwipunek():
    global nazwa_sceny
    fps = 8
    clock = pygame.time.Clock()
    font = pygame.font.Font(f'freesansbold.ttf', 52)

    strzalka_powrot = Strzalka(strzalka_prawo_img, 1100, 550)
    kwiatek = Element(kwiatek_obraz_img[1], 100, 100)
    ziola = pygame.transform.scale(ziola_img, (150,150))
    ziola = Element(ziola, 370, 100)
    herbata = pygame.transform.scale(herbata_img, (150,150))
    herbata = Element(herbata, 650, 100)
    moneta = Element(moneta_img, 1000, 450)

    running = True
    while running:
        clock.tick(fps)
        pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                with open('dane.txt', 'w') as plik_dane:
                    json.dump(dane, plik_dane)
                running = False
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if strzalka_powrot.touch(pos):
                    if dane["nazwa_sceny"] == 1:
                        przed_domem()
                    elif dane["nazwa_sceny"] == 2:
                        rozwidlenie()
                    elif dane["nazwa_sceny"] == 3:
                        domek()
                    elif dane["nazwa_sceny"] == 4:
                        przed_sklepem()
                    elif dane["nazwa_sceny"] == 5:
                        sklep()


        screen.blit(tlo_ekwipunek_img, (0,0))
        strzalka_powrot.draw()
        moneta.draw()
        monety = font.render(f'{dane["ilosc_monet"]}', True, (255,255,255))
        screen.blit(monety, (1070, 460))
        if dane["ilosc_kwiatkow"] > 0:
            kwiatek.draw()
            kwiatki = font.render(f'{dane["ilosc_kwiatkow"]}', True, (255,255,255))
            screen.blit(kwiatki, (230, 150))
        if dane["ilosc_ziol"] > 0:
            ziolo = font.render(f'{dane["ilosc_ziol"]}', True, (255,255,255))
            screen.blit(ziolo, (530, 150))
            ziola.draw()
        if dane["ilosc_herbaty"] > 0:
            herbaty = font.render(f'{dane["ilosc_herbaty"]}', True, (255,255,255))
            screen.blit(herbaty, (820, 150))
            herbata.draw()


        pygame.display.update()

#####################################################################
def przed_domem():
    fps = 8
    clock = pygame.time.Clock()

    strzalka_lewo = Strzalka(strzalka_lewo_img, 50, 400)
    strzalka_prawo = Strzalka(strzalka_prawo_img, 1200, 600)
    strzalka_gora = Strzalka(strzalka_gora_img, 750, 470)
    koszyk = Element(koszyk_img, 1150, 30)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                with open('dane.txt', 'w') as plik_dane:
                    json.dump(dane, plik_dane)
                running = False
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if strzalka_lewo.touch(pos):
                    rozwidlenie()
                if strzalka_prawo.touch(pos):
                    przed_sklepem()
                if strzalka_gora.touch(pos):
                    domek()
                if koszyk.touch(pos):
                    dane["nazwa_sceny"] = 1
                    ekwipunek()

        pos = pygame.mouse.get_pos()
        screen.blit(tlo_przed_domem_img, (0,0))
        strzalka_lewo.draw()
        strzalka_prawo.draw()
        strzalka_gora.draw()
        koszyk.draw()

        pygame.display.update()
        clock.tick(fps)

####################################################################
def rozwidlenie():
    fps = 8
    clock = pygame.time.Clock()

    koszyk = Element(koszyk_img, 1150, 30)

    strzalka_polana1 = Strzalka(strzalka_lewo_img, 50, 350)
    strzalka_polana2 = Strzalka(strzalka_gora_img, 150, 50)
    strzalka_polana3 = Strzalka(strzalka_dol_img, 70, 600)
    strzalka_polana4 = Strzalka(strzalka_gora_img, 500, 50)
    strzalka_polana5 = Strzalka(strzalka_dol_img, 430, 600)
    strzalka_polana6 = Strzalka(strzalka_gora_img, 850, 50)
    strzalka_polana7 = Strzalka(strzalka_dol_img, 800, 600)
    strzalka_powrot = Strzalka(strzalka_prawo_img, 1200, 350)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                with open('dane.txt', 'w') as plik_dane:
                    json.dump(dane, plik_dane)
                running = False
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if strzalka_polana1.touch(pos):
                    zbieranie_lvl1()
                if strzalka_polana2.touch(pos):
                    if dane["ilosc_monet"] < 10 or dane["zebrane_kwiaty"] < 30:
                        pass
                    else:
                        dane["ilosc_monet"] -= 10 
                        zbieranie_lvl2()
                if strzalka_polana3.touch(pos):
                    if dane["ilosc_monet"] < 10 or dane["zebrane_kwiaty"] < 100:
                        pass
                    else:
                        dane["ilosc_monet"] -= 10
                        zbieranie_lvl3()
                if strzalka_polana4.touch(pos):
                    if dane["ilosc_monet"] < 30 or dane["zebrane_kwiaty"] < 200:
                        pass
                    else:
                        dane["ilosc_monet"] -= 30
                        zbieranie_lvl4()
                if strzalka_polana5.touch(pos):
                    if dane["ilosc_monet"] < 35 or dane["zebrane_kwiaty"] < 300:
                        pass
                    else:
                        dane["ilosc_monet"] -= 35
                        zbieranie_lvl5()
                if strzalka_polana6.touch(pos):
                    if dane["ilosc_monet"] < 40 or dane["zebrane_kwiaty"] < 350:
                        pass
                    else:
                        dane["ilosc_monet"] -= 40
                        zbieranie_lvl6()
                if strzalka_polana7.touch(pos):
                    if dane["ilosc_monet"] < 50 or dane["zebrane_kwiaty"] < 450:
                        pass
                    else:
                        dane["ilosc_monet"] -= 50
                        zbieranie_lvl7()
                if strzalka_powrot.touch(pos):
                    przed_domem()
                if koszyk.touch(pos):
                    dane["nazwa_sceny"] = 2
                    ekwipunek()
                
        
        pos = pygame.mouse.get_pos()
        screen.blit(tlo_rozwidlenie_img, (0,0))
        strzalka_polana1.draw()
        strzalka_polana2.draw()
        strzalka_polana3.draw()
        strzalka_polana4.draw()
        strzalka_polana5.draw()
        strzalka_polana6.draw()
        strzalka_polana7.draw()
        strzalka_powrot.draw()
        koszyk.draw()

        pygame.display.update()
        clock.tick(fps)

#####################################################################
def domek():
    fps = 8
    clock = pygame.time.Clock()
    maszyna1 = Element(maszyna1_img, 80, 300)
    maszyna2 = Element(maszyna2_img, 330, 300)
    maszyna3 = Element(maszyna3_img, 600, 300)
    maszyna4 = Element(maszyna4_img, 900, 300)
    strzalka_powrot = Strzalka(strzalka_prawo_img, 1200, 550)
    koszyk = Element(koszyk_img, 1150, 30)

    running = True
    while running:
        clock.tick(fps)
        pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                with open('dane.txt', 'w') as plik_dane:
                    json.dump(dane, plik_dane)
                running = False
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if maszyna1.touch(pos):
                    dane["ilosc_kwiatkow"] -= 4
                    maszyna_lvl1()
                if maszyna2.touch(pos):
                    maszyna2()
                if maszyna3.touch(pos):
                    maszyna3()
                if maszyna4.touch(pos):
                    maszyna4()
                if strzalka_powrot.touch(pos):
                    przed_domem()
                if koszyk.touch(pos):
                    dane["nazwa_sceny"] = 3
                    ekwipunek()
        
        screen.blit(tlo_domek_img, (0, 0))
        maszyna1.draw()
        maszyna2.draw()
        maszyna3.draw()
        maszyna4.draw()
        strzalka_powrot.draw()
        koszyk.draw()

        pygame.display.update()

#####################################################################
def sklep():
    fps = 8
    clock = pygame.time.Clock()
    strzalka_powrot = Strzalka(strzalka_prawo_img, 1200, 600)
    koszyk = Element(koszyk_img, 1150, 30)
    font = pygame.font.Font(f'freesansbold.ttf', 48)
    font_napis = pygame.font.Font(f'freesansbold.ttf', 30)
    global ziola_img

    ziola_img = pygame.transform.scale(ziola_img, (100,100))
    tlo_ziola = Element(tlo_guzik_img, 290,200)
    ziola = Element(ziola_img, 130, 180)

    herbata = pygame.transform.scale(herbata_img, (100,100))
    tlo_herbaty = Element(tlo_guzik_img, 300,310)
    herbata = Element(herbata, 130, 220)


    running = True
    while running:
        clock.tick(fps)
        pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                with open('dane.txt', 'w') as plik_dane:
                    json.dump(dane, plik_dane)
                running = False
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if strzalka_powrot.touch(pos):
                    przed_sklepem()
                if koszyk.touch(pos):
                    dane["nazwa_sceny"] = 5
                    ekwipunek()
                if tlo_ziola.touch(pos):
                    dane["ilosc_monet"] += 20
                    dane["ilosc_ziol"] -= 1
                if tlo_herbaty.touch(pos):
                    dane["ilosc_monet"] += 20
                    dane["ilosc_herbaty"] -= 1
            
        
        screen.blit(tlo_sklep_img, (0,0))
        strzalka_powrot.draw()
        if dane["ilosc_ziol"] > 0:
                ziolo = font.render(f'{dane["ilosc_ziol"]}', True, (255,255,255))
                sprzedaj_kwiaty = font_napis.render(("sprzedaj"), True, (255,255,255))
                tlo_ziola.draw()
                screen.blit(ziolo, (250, 200))
                screen.blit(sprzedaj_kwiaty, (300, 210))
                ziola.draw()
        if dane["ilosc_herbaty"] > 0:
                herbaty = font.render(f'{dane["ilosc_herbaty"]}', True, (255,255,255))
                sprzedaj_kwiaty = font_napis.render(("sprzedaj"), True, (255,255,255))
                tlo_herbaty.draw()
                screen.blit(herbaty, (250, 300))
                screen.blit(sprzedaj_kwiaty, (300, 320))
                herbata.draw()
                
        koszyk.draw()

        pygame.display.update()

#####################################################################
def przed_sklepem():
    fps = 8
    clock = pygame.time.Clock()

    strzalka_lewo = Strzalka(strzalka_lewo_img, 50, 600)
    strzalka_gora = Strzalka(strzalka_gora_img, 950, 350)
    koszyk = Element(koszyk_img, 1150, 30)
    
    running = True
    while running:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                with open('dane.txt', 'w') as plik_dane:
                    json.dump(dane, plik_dane)
                running = False
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if strzalka_lewo.touch(pos):
                    przed_domem()
                if strzalka_gora.touch(pos):
                    sklep()
                if koszyk.touch(pos):
                    dane["nazwa_sceny"] = 4
                    ekwipunek()

        pos = pygame.mouse.get_pos()
        screen.blit(tlo_przed_sklepem_img, (0,0))
        strzalka_gora.draw()
        strzalka_lewo.draw()
        koszyk.draw()

        pygame.display.update()


#####################################################################
def maszyna_lvl1():

    w_rece1 = 0
    w_rece2 = 0
    w_rece3 = 0
    w_rece4 = 0
    w_rece5 = 0
    w_rece6 = 0

    w_misce1 = 0
    w_misce2 = 0
    w_misce3 = 0
    w_misce4 = 0
    w_misce5 = 0
    w_misce6 = 0

    global ziola_img

    pos = pygame.mouse.get_pos()
    fps = 8
    clock = pygame.time.Clock()
    kwiatek1 = Element(kwiatek_obraz_img[0], 50, 70)
    kwiatek2 = Element(kwiatek_obraz_img[0], 50, 220)
    kwiatek3 = Element(kwiatek_obraz_img[0], 50, 360)
    kwiatek4 = Element(kwiatek_obraz_img[0], 50, 510)

    strzalka_powrot = Strzalka(strzalka_prawo_img, 1100, 650)

    maszyna1_kwiatek_img[0] = pygame.transform.scale(maszyna1_kwiatek_img[0], (200,200))
    maszyna1_kwiatek_img[1] = pygame.transform.scale(maszyna1_kwiatek_img[1], (200,200))
    maszyna1_kwiatek_img[2] = pygame.transform.scale(maszyna1_kwiatek_img[2], (200,200))
    maszyna1_kwiatek_img[3] = pygame.transform.scale(maszyna1_kwiatek_img[3], (200,200))
    ziola_img = pygame.transform.scale(ziola_img, (200,200))
    kwiatek1_w = Element(maszyna1_kwiatek_img[0], 500, 250)
    kwiatek2_w = Element(maszyna1_kwiatek_img[1], 500, 250)
    kwiatek3_w = Element(maszyna1_kwiatek_img[2], 500, 250)
    kwiatek4_w = Element(maszyna1_kwiatek_img[3], 500, 250)
    ziola = Element(ziola_img, 500, 250)


    maszyna1_tluczek_img1 = pygame.transform.scale(maszyna1_tluczek_img, (200,200))
    tluczek = Element(maszyna1_tluczek_img1, 1050, 50)
    maszyna1_widelec_img1 = pygame.transform.scale(maszyna1_widelec_img, (200,200))
    widelec = Element(maszyna1_widelec_img1, 1050, 400)


    running = True
    while running:
        clock.tick(fps)
        pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                with open('dane.txt', 'w') as plik_dane:
                    json.dump(dane, plik_dane)
                running = False
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if strzalka_powrot.touch(pos):
                    domek()
                if kwiatek1.touch(pos):
                    if w_rece1 == 0:
                        w_rece1 = 1
                    if w_rece1 == 1 and kwiatek1.x >= 400 and kwiatek1.x <= 800 and kwiatek1.y >= 200 and kwiatek1.y <= 650:
                        w_rece1 = 0
                        kwiatek1 = Element(kwiatek_obraz_img[0], -500, -500)
                        w_misce1 = 1

                if kwiatek2.touch(pos):
                    if w_rece2 == 0:
                        w_rece2 = 1
                    if w_rece2 == 1 and kwiatek2.x >= 400 and kwiatek2.x <= 800 and kwiatek2.y >= 200 and kwiatek2.y <= 650:
                        w_rece2 = 0
                        kwiatek2 = Element(kwiatek_obraz_img[0], -500, -500)
                        w_misce2 = 1

                if kwiatek3.touch(pos):
                    if w_rece3 == 0:
                        w_rece3 = 1
                    if w_rece3 == 1 and kwiatek3.x >= 400 and kwiatek3.x <= 800 and kwiatek3.y >= 200 and kwiatek3.y <= 650:
                        w_rece3 = 0
                        kwiatek3 = Element(kwiatek_obraz_img[0], -500, -500)
                        w_misce3 = 1

                if kwiatek4.touch(pos):
                    if w_rece4 == 0:
                        w_rece4 = 1
                    if w_rece4 == 1 and kwiatek4.x >= 400 and kwiatek4.x <= 800 and kwiatek4.y >= 200 and kwiatek4.y <= 650:
                        w_rece4 = 0
                        kwiatek4 = Element(kwiatek_obraz_img[0], -500, -500)
                        w_misce4 = 1

                if tluczek.touch(pos):
                    if w_rece5 == 0 and w_rece4 == 0 and w_rece3 == 0 and w_rece2 == 0 and w_rece1 == 0:
                        w_rece5 = 1
                    if w_rece5 == 1 and tluczek.x >= 400 and tluczek.x <= 800 and tluczek.y >= 200 and tluczek.y <= 650:
                        w_rece5 = 0
                        tluczek = Element(kwiatek_obraz_img[0], -500, -500)
                        w_misce5 = 1

                if widelec.touch(pos):
                    if w_rece6 == 0:
                         w_rece6 = 1
                    if w_rece6 == 1 and widelec.x >= 400 and widelec.x <= 800 and widelec.y >= 200 and widelec.y <= 650:
                        w_rece6 = 0
                        widelec = Element(kwiatek_obraz_img[0], -500, -500)
                        w_misce6 = 1
                        dane["ilosc_ziol"] += 1
                    

                
                        

               

        screen.blit(tlo_maszyna1_img, (0,0))

        if w_misce1 == 1:
            kwiatek1_w.draw()
        if w_misce2 == 1: 
            w_misce1 = 0   
            kwiatek2_w.draw()
        if w_misce3 == 1:
            w_misce2 = 0
            kwiatek3_w.draw()
        if w_misce4 == 1:
            w_misce3 = 0
            kwiatek4_w.draw()
        if w_misce5 == 1:
            w_misce4 = 0
            ziola.draw()
        if w_misce6 == 1:
            w_misce5 = 0

        if w_rece1 == 0:
            kwiatek1.draw()
        elif w_rece1 == 1:
            kwiatek1 = Element(kwiatek_obraz_img[0], pos[0]-40, pos[1]-40)
            kwiatek1.draw()

        if w_rece2 == 0:
            kwiatek2.draw()
        elif w_rece2 == 1:
            kwiatek2 = Element(kwiatek_obraz_img[0], pos[0]-40, pos[1]-40)
            kwiatek2.draw()

        if w_rece3 == 0:
            kwiatek3.draw()
        elif w_rece3 == 1:
            kwiatek3 = Element(kwiatek_obraz_img[0], pos[0]-40, pos[1]-40)
            kwiatek3.draw()

        if w_rece4 == 0:
            kwiatek4.draw()
        elif w_rece4 == 1:
            kwiatek4 = Element(kwiatek_obraz_img[0], pos[0]-40, pos[1]-40)
            kwiatek4.draw()

        if w_rece5 == 0:
            tluczek.draw()
        elif w_rece5 == 1:
            tluczek = Element(maszyna1_tluczek_img, pos[0]-40, pos[1]-40)
            tluczek.draw()

        if w_rece6 == 0:
            widelec.draw()
        elif w_rece6 == 1:
            widelec = Element(maszyna1_widelec_img1, pos[0]-40, pos[1]-40)
            widelec.draw()

        strzalka_powrot.draw()

        

        pygame.display.update()

#####################################################################
def zbieranie_lvl1():
    fps = 8
    clock = pygame.time.Clock()
    krzak1 = Krzak(100, 100)
    krzak2 = Krzak(300, 200)
    krzak3 = Krzak(1000, 300)
    krzak4 = Krzak(400, 400)
    krzak5 = Krzak(700, 250)
    krzak6 = Krzak(200, 500)
    krzak7 = Krzak(800, 530)
    krzak8 = Krzak(850, 50)
    strzalka_powrot = Strzalka(strzalka_prawo_img, 1200, 650)
    font = pygame.font.Font(f'freesansbold.ttf', 32)
    running = True
    while running:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    with open('dane.txt', 'w') as plik_dane:
                        json.dump(dane, plik_dane)
                    running = False
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if strzalka_powrot.touch(pos):
                        rozwidlenie()
                    if krzak1.touch(pos):
                        krzak1.czary(1)
                    if krzak2.touch(pos):
                        krzak2.czary(1)
                    if krzak3.touch(pos):
                        krzak3.czary(1)
                    if krzak4.touch(pos):
                        krzak4.czary(1)
                    if krzak5.touch(pos):
                        krzak5.czary(1)
                    if krzak6.touch(pos):
                        krzak6.czary(1)
                    if krzak7.touch(pos):
                        krzak7.czary(1)
                    if krzak8.touch(pos):
                        krzak8.czary(1)
                    
        pos = pygame.mouse.get_pos()
        screen.blit(tlo_zbieranie_img, (0,0))
        score = font.render(f'{dane["ilosc_kwiatkow"]}', True, (255,255,255))
        screen.blit(score, (1200, 20))
        krzak1.draw()
        krzak2.draw()
        krzak3.draw()
        krzak4.draw()
        krzak5.draw()
        krzak6.draw()
        krzak7.draw()
        krzak8.draw()
        strzalka_powrot.draw()

        pygame.display.update()
        clock.tick(fps)

#####################################################################
def zbieranie_lvl2():
    fps = 8
    clock = pygame.time.Clock()
    krzak1 = Krzak(100, 30)
    krzak2 = Krzak(450, 70)
    krzak3 = Krzak(1000, 50)
    krzak4 = Krzak(400, 500)
    krzak5 = Krzak(960, 500)
    krzak6 = Krzak(840, 350)
    krzak7 = Krzak(660, 50)
    krzak8 = Krzak(50, 550)
    krzak9 = Krzak(1050, 260)
    krzak10 = Krzak(240, 340)
    krzak11 = Krzak(550, 240)
    krzak12 = Krzak(650, 600)
    strzalka_powrot = Strzalka(strzalka_prawo_img, 1200, 650)
    font = pygame.font.Font(f'freesansbold.ttf', 32)
    running = True
    while running:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    with open('dane.txt', 'w') as plik_dane:
                        json.dump(dane, plik_dane)
                    running = False
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if strzalka_powrot.touch(pos):
                        rozwidlenie()
                    if krzak1.touch(pos):
                        krzak1.czary(1)
                    if krzak2.touch(pos):
                        krzak2.czary(1)
                    if krzak3.touch(pos):
                        krzak3.czary(1)
                    if krzak4.touch(pos):
                        krzak4.czary(1)
                    if krzak5.touch(pos):
                        krzak5.czary(1)
                    if krzak6.touch(pos):
                        krzak6.czary(1)
                    if krzak7.touch(pos):
                        krzak7.czary(1)
                    if krzak8.touch(pos):
                        krzak8.czary(1)
                    if krzak9.touch(pos):
                        krzak9.czary(1)
                    if krzak10.touch(pos):
                        krzak10.czary(1)
                    if krzak11.touch(pos):
                        krzak11.czary(1)
                    if krzak12.touch(pos):
                        krzak12.czary(1)
                    
        pos = pygame.mouse.get_pos()
        screen.blit(tlo_zbieranie_img, (0,0))
        score = font.render(f'{dane["ilosc_kwiatkow"]}', True, (255,255,255))
        screen.blit(score, (1200, 20))
        krzak1.draw()
        krzak2.draw()
        krzak3.draw()
        krzak4.draw()
        krzak5.draw()
        krzak6.draw()
        krzak7.draw()
        krzak8.draw()
        krzak9.draw()
        krzak10.draw()
        krzak11.draw()
        krzak12.draw()
        strzalka_powrot.draw()

        pygame.display.update()
        clock.tick(fps)

#####################################################################
def zbieranie_lvl3():
    fps = 8
    clock = pygame.time.Clock()
    krzak1 = Krzak(100, 100)
    krzak2 = Krzak(300, 200)
    krzak3 = Krzak(1000, 300)
    krzak4 = Krzak(400, 400)
    krzak5 = Krzak(700, 250)
    krzak6 = Krzak(200, 500)
    krzak7 = Krzak(800, 530)
    krzak8 = Krzak(850, 50)
    strzalka_powrot = Strzalka(strzalka_prawo_img, 1200, 650)
    font = pygame.font.Font(f'freesansbold.ttf', 32)
    running = True
    while running:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    with open('dane.txt', 'w') as plik_dane:
                        json.dump(dane, plik_dane)
                    running = False
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if strzalka_powrot.touch(pos):
                        rozwidlenie()
                    if krzak1.touch(pos):
                        krzak1.czary(2)
                    if krzak2.touch(pos):
                        krzak2.czary(2)
                    if krzak3.touch(pos):
                        krzak3.czary(2)
                    if krzak4.touch(pos):
                        krzak4.czary(2)
                    if krzak5.touch(pos):
                        krzak5.czary(2)
                    if krzak6.touch(pos):
                        krzak6.czary(2)
                    if krzak7.touch(pos):
                        krzak7.czary(2)
                    if krzak8.touch(pos):
                        krzak8.czary(2)
                    
        pos = pygame.mouse.get_pos()
        screen.blit(tlo_zbieranie_img, (0,0))
        score = font.render(f'{dane["ilosc_kwiatkow"]}', True, (255,255,255))
        screen.blit(score, (1200, 20))
        krzak1.draw()
        krzak2.draw()
        krzak3.draw()
        krzak4.draw()
        krzak5.draw()
        krzak6.draw()
        krzak7.draw()
        krzak8.draw()
        strzalka_powrot.draw()

        pygame.display.update()
        clock.tick(fps)

#####################################################################
def zbieranie_lvl4():
    fps = 8
    clock = pygame.time.Clock()
    krzak1 = Krzak(100, 30)
    krzak2 = Krzak(450, 70)
    krzak3 = Krzak(1000, 50)
    krzak4 = Krzak(400, 500)
    krzak5 = Krzak(960, 500)
    krzak6 = Krzak(840, 350)
    krzak7 = Krzak(660, 50)
    krzak8 = Krzak(50, 550)
    krzak9 = Krzak(1050, 260)
    krzak10 = Krzak(240, 340)
    krzak11 = Krzak(550, 240)
    krzak12 = Krzak(650, 600)
    strzalka_powrot = Strzalka(strzalka_prawo_img, 1200, 650)
    font = pygame.font.Font(f'freesansbold.ttf', 32)
    running = True
    while running:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    with open('dane.txt', 'w') as plik_dane:
                        json.dump(dane, plik_dane)
                    running = False
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if strzalka_powrot.touch(pos):
                        rozwidlenie()
                    if krzak1.touch(pos):
                        krzak1.czary(2)
                    if krzak2.touch(pos):
                        krzak2.czary(2)
                    if krzak3.touch(pos):
                        krzak3.czary(2)
                    if krzak4.touch(pos):
                        krzak4.czary(2)
                    if krzak5.touch(pos):
                        krzak5.czary(2)
                    if krzak6.touch(pos):
                        krzak6.czary(2)
                    if krzak7.touch(pos):
                        krzak7.czary(2)
                    if krzak8.touch(pos):
                        krzak8.czary(2)
                    if krzak9.touch(pos):
                        krzak9.czary(2)
                    if krzak10.touch(pos):
                        krzak10.czary(2)
                    if krzak11.touch(pos):
                        krzak11.czary(2)
                    if krzak12.touch(pos):
                        krzak12.czary(2)
                    
        pos = pygame.mouse.get_pos()
        screen.blit(tlo_zbieranie_img, (0,0))
        score = font.render(f'{dane["ilosc_kwiatkow"]}', True, (255,255,255))
        screen.blit(score, (1200, 20))
        krzak1.draw()
        krzak2.draw()
        krzak3.draw()
        krzak4.draw()
        krzak5.draw()
        krzak6.draw()
        krzak7.draw()
        krzak8.draw()
        krzak9.draw()
        krzak10.draw()
        krzak11.draw()
        krzak12.draw()
        strzalka_powrot.draw()

        pygame.display.update()
        clock.tick(fps)

#####################################################################
def zbieranie_lvl5():
    fps = 8
    clock = pygame.time.Clock()
    krzak1 = Krzak(100, 100)
    krzak2 = Krzak(300, 200)
    krzak3 = Krzak(1000, 300)
    krzak4 = Krzak(400, 400)
    krzak5 = Krzak(700, 250)
    krzak6 = Krzak(200, 500)
    krzak7 = Krzak(800, 530)
    krzak8 = Krzak(850, 50)
    strzalka_powrot = Strzalka(strzalka_prawo_img, 1200, 650)
    font = pygame.font.Font(f'freesansbold.ttf', 32)
    running = True
    while running:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    with open('dane.txt', 'w') as plik_dane:
                        json.dump(dane, plik_dane)
                    running = False
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if strzalka_powrot.touch(pos):
                        rozwidlenie()
                    if krzak1.touch(pos):
                        krzak1.czary(5)
                    if krzak2.touch(pos):
                        krzak2.czary(5)
                    if krzak3.touch(pos):
                        krzak3.czary(5)
                    if krzak4.touch(pos):
                        krzak4.czary(5)
                    if krzak5.touch(pos):
                        krzak5.czary(5)
                    if krzak6.touch(pos):
                        krzak6.czary(5)
                    if krzak7.touch(pos):
                        krzak7.czary(5)
                    if krzak8.touch(pos):
                        krzak8.czary(5)
                    
        pos = pygame.mouse.get_pos()
        screen.blit(tlo_zbieranie_img, (0,0))
        score = font.render(f'{dane["ilosc_kwiatkow"]}', True, (255,255,255))
        screen.blit(score, (1200, 20))
        krzak1.draw()
        krzak2.draw()
        krzak3.draw()
        krzak4.draw()
        krzak5.draw()
        krzak6.draw()
        krzak7.draw()
        krzak8.draw()
        strzalka_powrot.draw()

        pygame.display.update()
        clock.tick(fps)

#####################################################################
def zbieranie_lvl6():
    fps = 8
    clock = pygame.time.Clock()
    krzak1 = Krzak(100, 30)
    krzak2 = Krzak(450, 70)
    krzak3 = Krzak(1000, 50)
    krzak4 = Krzak(400, 500)
    krzak5 = Krzak(960, 500)
    krzak6 = Krzak(840, 350)
    krzak7 = Krzak(660, 50)
    krzak8 = Krzak(50, 550)
    krzak9 = Krzak(1050, 260)
    krzak10 = Krzak(240, 340)
    krzak11 = Krzak(550, 240)
    krzak12 = Krzak(650, 600)
    strzalka_powrot = Strzalka(strzalka_prawo_img, 1200, 650)
    font = pygame.font.Font(f'freesansbold.ttf', 32)
    running = True
    while running:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    with open('dane.txt', 'w') as plik_dane:
                        json.dump(dane, plik_dane)
                    running = False
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if strzalka_powrot.touch(pos):
                        rozwidlenie()
                    if krzak1.touch(pos):
                        krzak1.czary(5)
                    if krzak2.touch(pos):
                        krzak2.czary(5)
                    if krzak3.touch(pos):
                        krzak3.czary(5)
                    if krzak4.touch(pos):
                        krzak4.czary(5)
                    if krzak5.touch(pos):
                        krzak5.czary(5)
                    if krzak6.touch(pos):
                        krzak6.czary(5)
                    if krzak7.touch(pos):
                        krzak7.czary(5)
                    if krzak8.touch(pos):
                        krzak8.czary(5)
                    if krzak9.touch(pos):
                        krzak9.czary(5)
                    if krzak10.touch(pos):
                        krzak10.czary(5)
                    if krzak11.touch(pos):
                        krzak11.czary(5)
                    if krzak12.touch(pos):
                        krzak12.czary(5)
                    
        pos = pygame.mouse.get_pos()
        screen.blit(tlo_zbieranie_img, (0,0))
        score = font.render(f'{dane["ilosc_kwiatkow"]}', True, (255,255,255))
        screen.blit(score, (1200, 20))
        krzak1.draw()
        krzak2.draw()
        krzak3.draw()
        krzak4.draw()
        krzak5.draw()
        krzak6.draw()
        krzak7.draw()
        krzak8.draw()
        krzak9.draw()
        krzak10.draw()
        krzak11.draw()
        krzak12.draw()
        strzalka_powrot.draw()

        pygame.display.update()
        clock.tick(fps)

#####################################################################
def zbieranie_lvl7():
    fps = 8
    clock = pygame.time.Clock()
    krzak1 = Krzak(100, 30)
    krzak2 = Krzak(450, 70)
    krzak3 = Krzak(1000, 50)
    krzak4 = Krzak(400, 500)
    krzak5 = Krzak(960, 500)
    krzak6 = Krzak(840, 350)
    krzak7 = Krzak(660, 50)
    krzak8 = Krzak(50, 550)
    krzak9 = Krzak(1050, 260)
    krzak10 = Krzak(240, 340)
    krzak11 = Krzak(550, 240)
    krzak12 = Krzak(650, 600)
    strzalka_powrot = Strzalka(strzalka_prawo_img, 1200, 650)
    font = pygame.font.Font(f'freesansbold.ttf', 32)
    running = True
    while running:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    with open('dane.txt', 'w') as plik_dane:
                        json.dump(dane, plik_dane)
                    running = False
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if strzalka_powrot.touch(pos):
                        rozwidlenie()
                    if krzak1.touch(pos):
                        krzak1.czary(10)
                    if krzak2.touch(pos):
                        krzak2.czary(10)
                    if krzak3.touch(pos):
                        krzak3.czary(10)
                    if krzak4.touch(pos):
                        krzak4.czary(10)
                    if krzak5.touch(pos):
                        krzak5.czary(10)
                    if krzak6.touch(pos):
                        krzak6.czary(10)
                    if krzak7.touch(pos):
                        krzak7.czary(10)
                    if krzak8.touch(pos):
                        krzak8.czary(10)
                    if krzak9.touch(pos):
                        krzak9.czary(10)
                    if krzak10.touch(pos):
                        krzak10.czary(10)
                    if krzak11.touch(pos):
                        krzak11.czary(10)
                    if krzak12.touch(pos):
                        krzak12.czary(10)
                    
        pos = pygame.mouse.get_pos()
        screen.blit(tlo_zbieranie_img, (0,0))
        score = font.render(f'{dane["ilosc_kwiatkow"]}', True, (255,255,255))
        screen.blit(score, (1200, 20))
        krzak1.draw()
        krzak2.draw()
        krzak3.draw()
        krzak4.draw()
        krzak5.draw()
        krzak6.draw()
        krzak7.draw()
        krzak8.draw()
        krzak9.draw()
        krzak10.draw()
        krzak11.draw()
        krzak12.draw()
        strzalka_powrot.draw()

        pygame.display.update()
        clock.tick(fps)

przed_domem()

