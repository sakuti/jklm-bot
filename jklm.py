#   Pieni JKLM projekti — Saku, 12.10.2021 - 13.10.2021
#   jklm.fun on sivusto, jossa pitää arvata englanninkielisiä sanoja
#   jotka sisältävät annetun tavun. Tein skriptin joka hakee tavun kopioimalla
#   sen sivulta ja hakemalla sille vastaavia sanoja wordlist.txt:stä, joka sisältää
#   n. 60000 englanninkielen sanaa. 
# 
#   Skriptissä on viisi eri toimintoa.
#       - Realistinen nopeus virheillä [F2]
#       - Realistinen nopeus ilman virheitä [F4]
#       - Realistista nopeampi nopeus ilman virhettä [F8]
#       - Hyvin nopea nopeus ilman virheitä [F9]
#       - Realistinen nopeus pisimmällä sanalla [F10]
# 
#   Skripti toimii tällä hetkellä F2, F4, F8, F9 ja F10 painikkeilla. Kursorin on oltava 
#   jklm.fun sivustolla TAVUN päällä ja resoluutio ei saa olla liian pieni tai sivua zoomattu.
#   Skripti hakee tavun ja kirjoittaa sen automaattisesti toimintoon soveltuvalla nopeudella.


import time
import keyboard
import sys
import string
import os
import random

# Tk & PynPut
from tkinter import Tk
from pynput.mouse import Button, Controller
mouse = Controller()



os.system('cls')
position = ''
content = ''



with open("wordlist.txt", encoding="utf8") as f:
    content = f.readlines()




def click():
    mouse.click(Button.left, 1)




while True:

    # Sulje prosessi jos:
    if keyboard.is_pressed('delete'):
        sys.exit()

    # Aika realistinen, ei virheitä:
    if keyboard.is_pressed('F9'):
        click(); click();
        position = mouse.position
        keyboard.press_and_release('ctrl+c')
        x = Tk().clipboard_get().lower()
        os.system('cls')
        mouse.position = (position[0], (position[1] + 80)); click();
        mouse.position = position


        try: 
            tempArray = []

            for l in content:
                if x in l:
                    tempArray.append(l)

            for c in random.choices(tempArray, k=1):
                print(c.replace(x, f'\033[92m{x}\033[0m'))

                for kirjain in c:
                    sleep = random.randint(2, 25) / 100
                    time.sleep(sleep);

                    if random.randint(1, 10) > 1:  
                        if kirjain != "\n":
                            print(f'\033[92m{kirjain.upper()}\033[0m   {sleep}');
                        keyboard.press_and_release(kirjain)
                    else:
                        if kirjain != "\n":
                            rndlet = random.choice(string.ascii_letters).upper()
                            print(f'\033[93m{kirjain.upper()}\033[0m   {sleep}   [\033[91m{rndlet}\033[0m]');
                            keyboard.press_and_release(rndlet.lower())
                            time.sleep(0.05);
                            keyboard.press_and_release('BACKSPACE')
                            time.sleep(0.3);
                            keyboard.press_and_release(kirjain)
                        else:
                            keyboard.press_and_release(kirjain)

        except:
            continue
    




    # Nopea aika, ei virheitä:
    if keyboard.is_pressed('F8'):
        click(); click();
        position = mouse.position
        keyboard.press_and_release('ctrl+c')
        x = Tk().clipboard_get().lower()
        os.system('cls')
        mouse.position = (position[0], (position[1] + 80)); click();
        mouse.position = position


        try: 
            tempArray = []

            for l in content:
                if x in l:
                    tempArray.append(l)

            for c in random.choices(tempArray, k=1):
                print(c.replace(x, f'\033[96m{x}\033[0m'))

                for kirjain in c:
                    sleep = random.randint(1, 15) / 100
                    time.sleep(sleep);

                    if kirjain != "\n":
                        print(f'\033[96m{kirjain.upper()}\033[0m   {sleep}');

                    keyboard.press_and_release(kirjain)
        except:
            continue




    # Epärealistinen nopeus, ei virheitä
    elif keyboard.is_pressed('F2'):
        click(); click();
        position = mouse.position
        keyboard.press_and_release('ctrl+c')
        x = Tk().clipboard_get().lower(); os.system('cls')
        mouse.position = (position[0], (position[1] + 80)); click();
        mouse.position = position

        try: 
            tempArray = []

            for l in content:
                if x in l:
                    tempArray.append(l)

            for c in random.choices(tempArray, k=1):
                print(c.replace(x, f'\033[91m{x}\033[0m'))

                for kirjain in c:
                    sleep = 0.05

                    if kirjain != "\n":
                        print(f'\033[91m{kirjain.upper()}\033[0m   {sleep}');

                    time.sleep(sleep);
                    keyboard.press_and_release(kirjain)

        except:
            continue




    # Realistinen nopeus, virheitä
    elif keyboard.is_pressed('F10'):
        click(); click();
        position = mouse.position
        keyboard.press_and_release('ctrl+c')
        x = Tk().clipboard_get().lower(); os.system('cls')
        mouse.position = (position[0], (position[1] + 80)); click();
        mouse.position = position

        try: 
            tempArray = []

            for l in content:
                if x in l:
                    tempArray.append(l)

            for c in random.choices(tempArray, k=1):
                print(c.replace(x, f'\033[93m{x}\033[0m'))
                
                for kirjain in c:
                    sleep = random.randint(2, 25) / 100

                    if kirjain != "\n":
                        print(f'\033[93m{kirjain.upper()}\033[0m   {sleep}');

                    time.sleep(sleep);
                    keyboard.press_and_release(kirjain)

        except:
            continue




    # Hieman nopeampi nopeus, pisin sana
    elif keyboard.is_pressed('F4'):
        click(); click();
        position = mouse.position
        keyboard.press_and_release('ctrl+c')
        x = Tk().clipboard_get().lower(); os.system('cls')
        mouse.position = (position[0], (position[1] + 80)); click();
        mouse.position = position

        try: 
            tempArray = []

            for l in content:
                if x in l:
                    tempArray.append(l)

            c = max(tempArray, key=len)
            print(c.replace(x, f'\033[31m{x}\033[0m'))
            
            for kirjain in c:
                sleep = random.randint(2, 20) / 100

                if kirjain != "\n":
                    print(f'\033[31m{kirjain.upper()}\033[0m   {sleep}');

                time.sleep(sleep);
                keyboard.press_and_release(kirjain)

            content.remove(c)

        except:
            continue