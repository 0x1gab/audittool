import os

os.system('ls -la /root/ >> permisos_dir_root.txt')

archivo = open('permisos_dir_root.txt','r')

lectura_archivo = archivo.readlines()

del lectura_archivo[0]
del lectura_archivo[1:]

archivo_permiso = '\n'.join(lectura_archivo)


if archivo_permiso.find('drwx------')>=0:
    resultado = open('permisos_directorio_root.txt','w')
    esc_resultado = resultado.write('[+] Los permisos del directorio /root/ son correctos \n')
    esc_resultado = resultado.write('\t [-] Los permisos actuales de la carpeta son >> ' + str(archivo_permiso))
    resultado.close()
else:
    resultado = open('permisos_directorio_root.txt','w')
    esc_resultado = resultado.write('[+] Los permisos del directorio /root/ son incorrectos \n')
    esc_resultado = resultado.write('\t [-] Los permisos actuales de la carpeta son >> ' + str(archivo_permiso) + ' y se deben cambiar a 700 (drxw------)')
    resultado.close()

archivo.close()

os.system('sudo rm permisos_dir_root.txt')
