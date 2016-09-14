import os

os.system('sudo ls -la /var/log/ >> permisos.txt')

permisos = open('permisos.txt','r').readlines()

del permisos[0]
del permisos[1:]

permisos = ' '.join(permisos)

permisos = permisos.split(' ')

del permisos[1:]


try:
    permisos.index('drwx------')
    salida = open('permisos_logs.txt','w')
    esc_salida = salida.write('[+] Los permisos del directorio /var/log/ se encuentran de forma correcta' + ' \n')
    esc_salida = salida.write('\t [-] Los permisos actuales son ' + str(permisos))
    salida.close()
except:
    salida = open('permisos_logs.txt','w')
    esc_salida = salida.write('[+] Los permisos del directorio /var/log/ se encuentran de forma incorrecta' + ' \n')
    esc_salida = salida.write('\t [-] Los permisos actuales son ' + str(permisos) + ' y deberian cambiarse a 700 (drwx------)')
    salida.close()    


os.system('rm permisos.txt')
    


