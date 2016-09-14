import os

os.system('cat /etc/ntp.conf |grep -w broadcastclient > ntp.txt')

ntp = open('ntp.txt','r')
lectura_ntp = ntp.read()

if lectura_ntp.find('#broadcastclient')>=0:
    ntp.close()
    revisar_ntp = open('salida_configuracion_ntp.txt','w')
    esc_ntp = revisar_ntp.write('[+] La configuracion del archivo /etc/ntp.conf se encuentra de forma correcta.')
    revisar_ntp.close()
    

elif lectura_ntp.find('broadcastclient')>=0:
    ntp.close()
    revisar_ntp = open('salida_configuracion_ntp.txt','w')
    esc_ntp = revisar_ntp.write('[+] La configuracion actual del demonio NTP, es incorrecta. \n \t [-] Verificar que la linea broadcastclient, este comentada en el archivo /etc/ntp.conf.')
    revisar_ntp.close()

else:
    ntp.close()
    revisar_ntp = open('salida_configuracion_ntp.txt','w')
    esc_ntp = revisar_ntp.write('[+] No se ha encontrado el parametro #broadcastclient, por lo que es posible que la informacion este configurada de forma correcta. \n \t [-] Si es necesario, revisar el archivo /etc/ntp.conf para saber a que servidor de date&time apunta.')
    revisar_ntp.close()

os.system('rm ntp.txt')

