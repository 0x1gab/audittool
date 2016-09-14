import os

os.system('ls -la /etc/passwd >> permisos_temp.txt')

permisos_temp = open('permisos_temp.txt','r')
lectura_permisos = permisos_temp.read()

permiso = lectura_permisos.split()

if permiso[0]=='-rw-r--r--':
    permisos_temp.close()
    resultado = open('resultado_permisos_etc-passwd.txt','w')
    esc_resultado = resultado.write('[+] Los permisos actuales del directorio /etc/passwd son correctos. \n')
    esc_resultado = resultado.write('\t [-] Estos son: ' + str(permiso[0]) + ' \n')
else:
    permisos_temp.close()
    resultado = open('resultado_permisos_etc-passwd.txt','w')
    esc_resultado = resultado.write('[+] Los permisos actuales del directorio /etc/passwd son incorrectos. \n')
    esc_resultado = resultado.write('\t [-] Estos son: ' + str(permiso[0]) + ' y deben cambiarse a 644 para que resulten: -rw-r--r-- ' + ' \n ')
    esc_resultado = resultado.write('\t [-] La remediacion seria el siguiente comando: chmod 644 /etc/passwd' + '\n')
    esc_resultado = resultado.write('\t [-] Si es necesario, cambiar el owner al usuario root, con el siguiente comando: chown root:root /etc/passwd \n')

os.system('rm permisos_temp.txt')
