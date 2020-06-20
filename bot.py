import pyautogui
from PIL import ImageGrab, ImageOps
import keyboard
import time
import random
from numpy import *
import win32gui
VANGUARD=5755
BLADEMASTER=2805
SORC=4290
first_klasy=[VANGUARD,SORC]
klasy=[VANGUARD,SORC]
niepodswietlony=0
def main():
    prl=0
    prm=0
    prp=0
    imputted1=()
    imputted2=()
    while True:
        if keyboard.is_pressed('l') and prl==0:
            print(pyautogui.position())
            imputted1=imputted2
            imputted2=(pyautogui.position())
            prl=1
        elif not keyboard.is_pressed('l'):
            prl=0
        if keyboard.is_pressed('m') and prm==0:
            print(f"sum_of_rect({imputted1[0]},{imputted1[1]},{imputted2[0]},{imputted2[1]})=",sum_of_rect(imputted1[0],imputted1[1],imputted2[0],imputted2[1]))
            prm=1
        elif not keyboard.is_pressed('m'):
            prm=0
        if keyboard.is_pressed('p') and prp==0:
            print(win32gui.GetCursorInfo()[1])
            '''
            kup([0, 1, 2, 3, 4, 5, 6, 7, 8])
            for x in range(20):
                print(1285+x,1298+x,sum_of_rect(1285+x,1017,1298+x,1027))
            print('---------------')
            kliknij(490,1017)
            time.sleep(3)
            kliknij(691, 1017)
            time.sleep(3)
            kliknij(892, 1017)
            time.sleep(3)
            kliknij(1093, 1017)
            time.sleep(3)
            kliknij(1294, 1017)
            time.sleep(3)
            print(sum_of_rect(489,1017,502,1027))
            print(sum_of_rect(690,1017,703,1027))
            print(sum_of_rect(891,1017,904,1027))
            print(sum_of_rect(1093,1017,1106,1027))
            print(sum_of_rect(1294,1017,1307,1027))
            print('------------------')
            '''
            prp=1
        elif not keyboard.is_pressed('p'):
            prp=0

def p(x):
    while True:
        print(sum_of_rect(x[0],x[1],x[2],x[3]))
def wpinczol_sie():
    #time.sleep(4)
    while sum_of_rect(256,102,368,128)!=16790:
        print(sum_of_rect(256,102,368,128))
    pyautogui.click(x=301, y=127)
    #time.sleep(2)
    while sum_of_rect(258,100,380,125)!=4383:
        print(sum_of_rect(258,100,380,125))
    pyautogui.click(x=1248, y=359)
    #time.sleep(2)
    while sum_of_rect(1226,296,1293,362)!=21747:
        print(sum_of_rect(1226,296,1293,362))
    pyautogui.click(x=852, y=935)
    while sum_of_rect(230,911,440,935)!=5048:
        print(sum_of_rect(230,911,440,935))
    #time.sleep(2)

def sum_of_rect(a,b,c,d):
    img = ImageGrab.grab((a,b,c,d))
    grayImg = ImageOps.grayscale(img)
    arr = array(grayImg.getcolors())
    return arr.sum()

def szukaj_gre():
    pyautogui.click(x=840, y=930)
    time.sleep(0.5)
    #p((662,585,1030,674))
    znal=0
    while True:
        if keyboard.is_pressed('space'):
            break
        if sum_of_rect(662,585,1030,674)!=37499 and znal==0:
            print(sum_of_rect(662,585,1030,674))
            pyautogui.click(x=915, y=766)
            print("GRA ZNALEZIONA")
            znal=1
        elif sum_of_rect(662,585,1030,674)==37499:
            znal=0
        if sum_of_rect(1393,1061,1552,1069)!=1496:
            print("WSZYSCY ZAAKCEPTOWALI")
            break

def wywal_pierwszy():
    return
    pierwszy=(418, 770)
    pyautogui.moveTo(418, 770)
    time.sleep(0.2)
    pyautogui.mouseDown()
    time.sleep(0.2)
    pyautogui.moveTo(855, 1001)
    time.sleep(0.2)
    pyautogui.mouseUp()
    time.sleep(0.2)

def kup(zajete):
    global klasy
    limit_klas=2
    do_kupna=[(599,991),(749,988),(1006,982),(1194,979),(1376,984)]
    miejsca_klas=[(489,1017,502,1027),(690,1017,703,1027),(891,1017,904,1027),(1093,1017,1106,1027),(1294,1017,1307,1027)]
    pozy=[(410, 757),(529, 769),(655, 768),(771, 762),(893, 772),(1010, 754),(1121, 761),(1245, 759),(1368, 755)]
    index=0
    nr=0
    while index<len(pozy):
        poz=pozy[index]
        pyautogui.moveTo(poz[0],poz[1])
        pyautogui.mouseDown()
        time.sleep(0.1)
        if win32gui.GetCursorInfo()[1]!=niepodswietlony and index not in zajete:
            pyautogui.moveTo(875, 1061)
            pyautogui.mouseUp()
        elif win32gui.GetCursorInfo()[1]==niepodswietlony and index in zajete and nr<=1:
            time.sleep(2)
            index=-1
            nr+=1
        else:
            pyautogui.moveTo(poz[0], poz[1])
            pyautogui.mouseUp()
        index+=1
    if len(klasy)<limit_klas:
        index=-1
        for kupowany in do_kupna:
            index+=1
            if len(klasy)>=limit_klas:
                break
            #pyautogui.moveTo(784, 323)
            #pyautogui.mouseDown(button='right')
            #pyautogui.mouseUp(button='right')
            #time.sleep(2)
            akt_klasa=miejsca_klas[index]
            rodzaj_klasy=sum_of_rect(akt_klasa[0],akt_klasa[1],akt_klasa[2],akt_klasa[3])
            kliknij(kupowany[0],kupowany[1])
            nowy_rodzaj_klasy=sum_of_rect(akt_klasa[0],akt_klasa[1],akt_klasa[2],akt_klasa[3])
            if rodzaj_klasy!=nowy_rodzaj_klasy and nowy_rodzaj_klasy==215 and rodzaj_klasy not in klasy:
                klasy.append(rodzaj_klasy)
                #print('nowy:',rodzaj_klasy)
            #else:
                #print('nie')
    if len(klasy) >= limit_klas:
        index=-1
        for kupowany in do_kupna:
            index+=1
            akt_klasa = miejsca_klas[index]
            rodzaj_klasy = sum_of_rect(akt_klasa[0], akt_klasa[1], akt_klasa[2], akt_klasa[3])
            if rodzaj_klasy in klasy:
                kliknij(kupowany[0], kupowany[1])
                #print('stary i go biore',index)
            #else:
                #print('nie biore')
            #time.sleep(1)
            #pyautogui.rightClick(784, 323)
            #time.sleep(2)
            #wywal_pierwszy()
    pyautogui.moveTo(784, 323)
    pyautogui.mouseDown(button='right')
    pyautogui.mouseUp(button='right')
    time.sleep(1)
    newzajete=[]
    pyautogui.moveTo(pozy[8][0], pozy[8][1])
    pyautogui.mouseDown()
    pyautogui.moveTo(875, 1061)
    pyautogui.mouseUp()
    index=-1
    for poz in pozy:
        index+=1
        pyautogui.moveTo(poz[0],poz[1])
        pyautogui.mouseDown()
        time.sleep(0.1)
        if win32gui.GetCursorInfo()[1]!=niepodswietlony:
            newzajete.append(index)
        pyautogui.moveTo(poz[0],poz[1])
        pyautogui.mouseUp()
    if newzajete!=[]:
        zajete=[]
        for x in newzajete:
            zajete.append(x)
    #print(zajete)
    return zajete

def ruszaj():
    lewy_gorny=(573, 202)
    prawy_dolny=(1329, 714)
    for _ in range(10):
        losx,losy=random.random()*(prawy_dolny[0]-lewy_gorny[0])+lewy_gorny[0],random.random()*(prawy_dolny[1]-lewy_gorny[1])+lewy_gorny[1]
        losx, losy=int(losx), int(losy)
        pyautogui.moveTo(losx, losy)
        pyautogui.mouseDown(button='right')
        pyautogui.mouseUp(button='right')
        time.sleep(0.2)
    for x in range(4):
        losx,losy=600,250+x*100
        pyautogui.moveTo(losx, losy)
        pyautogui.mouseDown(button='right')
        pyautogui.mouseUp(button='right')
        time.sleep(1)
        losx, losy = 1300, 250 + x * 100
        pyautogui.moveTo(losx, losy)
        pyautogui.mouseDown(button='right')
        pyautogui.mouseUp(button='right')
        time.sleep(1)

def moze_juz_rip():
    if sum_of_rect(730,520,928,550)==21233:
        kliknij(839,535)
        return True
    if sum_of_rect(908,634,1012,648)==25332:
        kliknij(959,642)
        return True
    if sum_of_rect(897,902,1016,923)==11762:
        return True
    if sum_of_rect(762,910,898,930)== 16548:
        return True

def kliknij(x,y):
    pyautogui.moveTo(x, y)
    time.sleep(0.2)
    pyautogui.mouseDown()
    time.sleep(0.2)
    pyautogui.mouseUp()
    time.sleep(0.2)

def lvlup():
    for _ in range(1):
        kliknij(358,949)



def szukaj_dwojek():
    lawka=[(411,781),(516,782),(659,767),(768,762),(909,775),(1004,765),(1142,772),(1254,788),(1389,780)]
    itemki=[(288,759),(334,725),(304,689),(348,664),(320,637),(339,596)]
    pyautogui.rightClick(784, 323)
    time.sleep(2)
    for item in itemki:
        pyautogui.moveTo(784,323)
        pyautogui.mouseDown(button='right')
        pyautogui.mouseUp(button='right')
        time.sleep(0.1)
        pyautogui.moveTo(item[0], item[1])
        pyautogui.mouseDown()
        pyautogui.moveTo(lawka[0][0], lawka[0][1])
        pyautogui.mouseUp()
    '''
    for zawodnik in lawka:
        print("KOLEJNY")
        tries=0
        pyautogui.moveTo(lawka[0][0],lawka[0][1])
        pyautogui.mouseDown()
        pyautogui.moveTo(zawodnik[0],zawodnik[1])
        pyautogui.mouseUp()
        pyautogui.moveTo(lawka[0][0],lawka[0][1])
        pyautogui.rightClick()
        while sum_of_rect(594,709,608,720)!=2946 and tries<5:
            tries+=1
            for item in itemki:
                pyautogui.moveTo(item[0],item[1])
                pyautogui.mouseDown()
                pyautogui.moveTo(lawka[0][0],lawka[0][1])
                pyautogui.mouseUp()
            pyautogui.mouseDown()
            lg=(570,456)
            pd=(1287,686)
            losx=random.random()*(pd[0]-lg[0])+lg[0]
            losy=random.random()*(pd[1]-lg[1])+lg[1]
            pyautogui.moveTo(losx,losy)
            pyautogui.mouseUp()
            pyautogui.moveTo(lawka[0][0],lawka[0][1])
            pyautogui.rightClick()
    '''
def umieramy():
    if moze_juz_rip():
        print('go next')
        time.sleep(10)
        if sum_of_rect(897, 902, 1016, 923) == 11762:
            kliknij(897, 902)
            time.sleep(5)
        print('go next')
        pyautogui.leftClick(x=840, y=935)
        time.sleep(1)
        return True


def graj():
    print("Jestesmy w grze")
    global klasy
    global niepodswietlony
    niepodswietlony=0
    klasy=first_klasy
    zajete=[]
    broken=0
    pyautogui.moveTo(50,50)
    time.sleep(30)
    niepodswietlony = win32gui.GetCursorInfo()[1]
    print(niepodswietlony)
    while True:
        #wywal_pierwszy()
        for _ in range(1):
            zajete=kup(zajete)
            if umieramy():
                broken=1
                break
        if broken:
            break

        ruszaj()
        if umieramy():
            break


        lvlup()
        if umieramy():
            break


        szukaj_dwojek()
        if umieramy():
            break


def ustaw_sie():
    pyautogui.leftClick(x=1690, y=94)
    time.sleep(1)
    pyautogui.leftClick(x=999, y=621)
    time.sleep(1)
    pyautogui.leftClick(x=961, y=696)
    time.sleep(1)
    pyautogui.leftClick(x=964, y=857)
    time.sleep(1)
def loop():
    #time.sleep(4)
    wpinczol_sie()
    while True:
        #ustaw_sie()
        szukaj_gre()
        graj()
#main()
loop()