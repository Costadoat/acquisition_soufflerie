import serial
from datetime import datetime
import matplotlib.pyplot as plt
file=open('data.txt','w')
s = serial.Serial(
    port="COM5", baudrate=115400)
s.flushInput()

input('Appuyer sur Entrée pour démarrer')
temps=[]
liste_vitesse_vent=[]
liste_force_portance=[]
while True:
    try:
        ser_bytes = s.readline()
        dt = datetime.now()
        decoded_bytes = float(ser_bytes[0:len(ser_bytes)].decode("utf-8"))
        vitesse_vent,force_portance=decoded_bytes.split(';')
        vitesse_vent=vitesse_vent*0.1
        force_portance=force_portance*0.1
        file.write(str(dt)+';'+vitesse_vent+';'+force_portance+'\n')
        temps.append(dt)
        liste_vitesse_vent.append(vitesse_vent)
        liste_force_portance.append(force_portance)
        print(dt,vitesse_vent,force_portance)
    except:
        print("Keyboard Interrupt")
        break

file.close()
plt.plot(temps,liste_vitesse_vent,label='Vitesse du vent')
plt.plot(temps,liste_force_portance,label='Force de portance')
plt.legend()
plt.show()
