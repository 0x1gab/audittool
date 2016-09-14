import os

os.system('cat /etc/ssh/sshd_config |grep TCPKeepAlive >> configuracion_actual.txt')
os.system('cat /etc/ssh/sshd_config |grep ClientAlive >> configuracion_actual.txt')

configuracion_actual = open('configuracion_actual.txt', 'r')
lect_conf_actual = configuracion_actual.read()

if lect_conf_actual.find('#TCPKeepAlive yes')>=0 or lect_conf_actual.find('#ClientAliveInterval')>=0 or lect_conf_actual.find('#ClientAliveCountMax')>=0:
    configuracion_actual.close()
    archivo = open('configuracion_para_aplicar.txt','w')
    esc_archivo = archivo.write('[+] Es necesario que se reemplace el archivo /etc/ssh/sshd_config con las siguientes lineas: \n \t [-] TCPKeepAlive yes \n \t [-] ClientAliveInternal 30 \n \t [-] ClientAliveCountMax 30 \n \n')
    esc_archivo = archivo.write('[-] La configuracion actual es: \n ' + str(lect_conf_actual))
    archivo.close()    
else:
    configuracion_actual.close()
    archivo = open('configuracion_para_aplicar.txt','w')
    esc_archivo = archivo.write('[+] La configuracion actual es correcta: ' + ' \n')
    esc_archivo = archivo.write(str(lect_conf_actual))
    
configuracion_actual.close()

os.system('rm configuracion_actual.txt')

#TCPKeepAlive yes         >>>>>>>>>     si se mantiene vivo el host
#ClientAliveInterval 30   >>>>>>>>>     cada 30 segundos manda una senial
#ClientAliveCountMax 30   >>>>>>>>>     cada 30 segundos manda una senial, y lo repite 30 veces

