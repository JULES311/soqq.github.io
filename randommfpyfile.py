import time
print(" ________  ")
print("|  _____ |  ")
print("| /____/ |")
print("|  ______|")
print("| |")
print("| |")
print("| |")
print("| |")
print("|_|")
print("Press B to start")
print("")
start = True
while start:
    var = input("///: ")
    if var == "B":
        print("")
        time.sleep(1)
        print("Starting...")
        time.sleep(2)
        print("")
        time.sleep(1)
        print("Loading...")
        time.sleep(1)
        print("")
        print("Welcome to a random python file, AKA 'P.'")
        start = False
    else:
        print("")
        time.sleep(1)
        print("UNKNOWN COMMAND")
print("")
print("Enter commands when you see the //: prompt")
print("Enter 'INFO' for help")
time.sleep(1)
run = True
while run:
    cmd = input("//: ")
    print("Searching cmd: " + cmd)
    print("")
    if cmd == "INFO":
        print("HELP PAGE")
        print("")
        time.sleep(1)
        print("-available commands-")
        print(" ")
        print("INFO - Display the help page")
        print("LANG - Change the language")
        print("GAME - Play a console game")
        print("")
        time.sleep(0.5)
        print("Enter any character to leave")
        cmd = input("//: ")
        if cmd == "L":
            print("Leaving to command menu.")
            print("")
            print("")
        else:
            print("Leaving to command menu.")
            print("")
            print("")
    elif cmd == "LANG":
        print("")
        print("SELECT LANGUAGE")
        print("")
        time.sleep(0.5)
        print("1) English")
        print("2) Espanol")
        print("")
        lang = input("Choose your language: ")
        if lang == "2":
            print("")
            print("Changing language to Spanish")
            print("")
            run = False
            spanish = True
        elif lang == "1":
            print("")
            print("Your language is already in English")
            print("")
    elif cmd == "GAME":
        print("")
        print("WARNING: THIS GAME HAS NO SPANISH TRANSLATION BECAUSE I DONT KNOW ENOUGH SPANISH TO TRANSLATE THE ENTIRE THING")
        print("and im lazy")
        time.sleep(1)
        run = False
        game = True
while spanish:
    print("")
    print("Hola, bienvenido a la consola de 'P'")
    print("Envia 'INFO' para ayudar")
    print("")
    cmd = input("//: ")
    print("Searching cmd: " + cmd)
    print("")
    if cmd == "INFO":
        print("PAGINA DE AYUDA")
        print("")
        time.sleep(1)
        print("-Comandos-")
        print("Envia tu mensaje cuando '//:' es aqui")
        print(" ")
        print("INFO - Mostar la pagina de ayuda")
        print("LANG - Languaje")
        print("GAME - Jugar un partido de consola")
        print("")
        time.sleep(0.5)
        print("Envia ningun carta a para salir")
        cmd = input("//: ")
        if cmd == "L":
            print("saliendo")
            time.sleep(1)
            print("")
            print("")
        else:
            print("saliendo")
            time.sleep(1)
            print("")
            print("")
    elif cmd == "LANG":
        print("")
        print("SELECT LANGUAGE")
        print("")
        time.sleep(0.5)
        print("1) English")
        print("2) Espanol")
        print("")
        lang = input("Choose your language: ")
        if lang == "2":
            print("")
            print("Your language is already in English")
            print("")
            run = False
            spanish = True
        elif lang == "1":
            print("")
            print("Changing langauge to English")
            print("")
            spanish == False
            run =True
    elif cmd == "GAME":
        print("")
        print("EL PARTIDO ES EN LENGAUJE DE INGLES PORQUE ES DESIANDO DIFICIL A TRANSLUCANDO EL PARTIDO!")
        time.sleep(1)
        spanish = False
        game = True


print("")
time.sleep(1)
print("Welcome to the console game")
