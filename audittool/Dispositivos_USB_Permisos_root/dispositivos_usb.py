import os

os.system('ls -la /media/ | cut -f1 -d: > salida_permisos_media.txt')
perm = open('salida_permisos_media.txt','r')
permisos = perm.readlines()

del permisos[0]
del permisos[1:]

permiso_media = ' '.join(permisos)

permiso_media = permiso_media.split(' ')

arc = open('revisar.txt','w')
esc = arc.write(permiso_media[0])
arc.close()

archivo = open('revisar.txt','r')
lectura = archivo.read()

if lectura.find('drwx------')<=0 or lectura.find('-rwx------')<=0:
    archivo.close()
    revisar = open('revisar_permisos_usb.txt','w')
    esc_revisar = revisar.write('[+] Los permisos actuales para los dispositivos USB son: ' + str(permiso_media[0]) + ' \n' )
    esc_revisar = revisar.write(' \t [-] Se debe hacer un chmod 700 /media/. Los permisos deberian quedar de la siguiente forma: drwx------ ') 
    revisar.close()
    
else:
    archivo.close()
    revisar = open('revisar_permisos_usb.txt','w')
    esc_revisar = revisar.write('[+] Los permisos actuales para los dispositivos USB estan aplicados de forma correcta: drwx------ (700)')
    revisar.close()

perm.close()
os.system('rm revisar.txt')
os.system('rm salida_permisos_media.txt')
