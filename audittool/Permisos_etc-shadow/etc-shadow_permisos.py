import os

os.system('ls -la /etc/shadow >> permisos_temp.txt')

permisos_temp = open('permisos_temp.txt','r')
lectura_permisos = permisos_temp.read()

permiso = lectura_permisos.split()

if permiso[0]=='-rw-r-----':
    permisos_temp.close()
    resultado = open('resultado_permisos_etc-shadow.txt','w')
    esc_resultado = resultado.write('[+] Los permisos actuales del directorio /etc/shadow son correctos. \n')
    esc_resultado = resultado.write('\t [-] Estos son: ' + str(permiso[0]))
else:
    permisos_temp.close()
    resultado = open('resultado_permisos_etc-shadow.txt','w')
    esc_resultado = resultado.write('[+] Los permisos actuales del directorio /etc/shadow son incorrectos. \n')
    esc_resultado = resultado.write('\t [-] Son los siguientes: ' + str(permiso[0]) + ' y deben cambiarse a 640 para que resulten: -rw-r--r-- ' + ' \n ')
    esc_resultado = resultado.write('\t [-] La remediacion seria el siguiente comando: chmod 640 /etc/shadow' + '\n')
    #esc_resultado = resultado.write('\t [-] Si es necesario, cambiar el owner al usuario root, con el siguiente comando: chown root:root /etc/shadow')

os.system('rm permisos_temp.txt')
