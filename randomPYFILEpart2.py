#BETTER RANDOM PY FILE
import time
#VARIABLES
homeScreen = True   

while homeScreen == True:
    print("RANDOM PYFILE 2")
    print("RANDOM PYFILE 2")
    print("RANDOM PYFILE 2")
    print("")
    cmd = input("/PASSWORD/:")
    if cmd == "contrasena":
        homeScreen = False
        global prompt
        prompt = True
    else:
        print("This Password is incorrect: " + cmd + ", please try again")
        
print("")
print("Welcome to RandomPyfile2 for when your bored.")
print("When you see this 'cmd> ' type the command there")
print("Everything in this program is triggered by a command")
print("Commands will be in all CAPS and under 5 letters")
print("")
print("")
time.sleep(4)
while prompt == True:
    print("")
    print("INFO - Lists all available commands")
    cmd = input("cmd>")

    if cmd == "INFO":
        print("")
        print("")
        time.sleep(1)
        print("AVAILABLE COMMANDS")
        time.sleep(0.5)
        print("")
        print("")
        print("COM - Display the latest information and news on the slug and this program.")
        print("FIGHTG - Play a text game developed my Julian.")
        #print("LANG - Cambiar tu lenguaje a espanol")
        print("JUEGO - Envia este comando a jugar un partido en espanol")
        print("")

        leave = input("Press enter to continue...")
    elif cmd == "FIGHTG":
        prompt = False
    elif cmd == "JUEGO":
        print("")
        print("Hola jugador. Bienvenido a un partido de espanol.")
        nombre = input("Que es tu nombre?: ")
        print("")
        print("hola " + nombre)
        time.sleep(1)
        print("Una Vez...")
        print("Esta fue un chico. Su nombre es " + nombre + ". El fue caminando en el calle cuando un hombre miran su. Su dice 'Hola chico!'. Llegas dentro en mi carro porque yo tengo dulces!")
        time.sleep(1)
        print("Tu llegas dentro su carro y sentarse en la silla. El hombre despues caminan hacia tu y disparan un arma hacia a tu. Tu es muerto jaja.")
    elif cmd == "COM":
        print("")
        print("(VERSION 1.0.0) Created RANDOMPYFILE2")
        print("")
        jucudu = input("Press enter to continue...")
    else:
        print("")
        print("THIS COMMAND DOES NOT EXIST")

print("")
print("")
print("Welcome to FightG! by Julian...")
time.sleep(1)
print("")
name = input("What is your name: ")
if name == "Julian":
    print("JODER TU RETARD! NO ESTAS JULIAN MUTHERFUCK! LLEGAS FUERA DE AQUI!")
else:
    print("Hello " + name)
print("")
time.sleep(1)
print("GAME STILL IN DEVELOPMENT (VERSION 0.0.0)")
mari = input("Press enter to end randompyfile2...")
