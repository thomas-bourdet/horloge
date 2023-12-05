import time
import keyboard

alarm = None 
paused = False
format_24h = True

def set_alarm(tp):   
    return "{:02d}:{:02d}:{:02d}".format(tp[0], tp[1], tp[2])

def afficher_heure(heure, format_24h):
    if paused:
        return
    if format_24h:
        heure_format = "{:02d}:{:02d}:{:02d}   ".format(heure[3], heure[4], heure[5])
    else:
        heure_format = time.strftime("%I:%M:%S %p", heure)
    print(heure_format, end='\r')

def changer_format(format_24h):
    return not format_24h

user_input = input("Voulez-vous définir une alarme ? (oui/non) ")


if user_input.lower() == "oui":
    hour = int(input("Entrez l'heure de l'alarme (format 24 heures) : "))
    minute = int(input("Entrez les minutes de l'alarme : "))
    secondes = int(input("Entrez les secondes de l'alarme: "))
    alarm = set_alarm((hour, minute, secondes))

while True:
    heure = time.localtime()

    if alarm and "{:02d}:{:02d}:{:02d}".format(heure[3], heure[4], heure[5]) == alarm:
        print("L'alarme a sonné") 

    afficher_heure(heure, format_24h)

    if keyboard.is_pressed('Enter'):
        if not paused:
            print("Script paused. Press Enter to resume.")
            paused = True
        else:
            paused = False

    if keyboard.is_pressed('m'):
        format_24h = changer_format(format_24h)


    time.sleep(0.1)