import os

os.system('id root > root_GID_UID_0.txt')

archivo = open('root_GID_UID_0.txt','r').read()

if archivo.find('uid=0(root) gid=0(root)')>=0: 
    os.system('echo [+] Efectivamente, el usuario root posee su UID y GID "0". >> GID_UID_root.txt ')
else:
    os.system('echo [+] Corregir el UID/GID del usuario root, ya que no se encuentra en 0 >> GID_UID_root.txt')
    os.system('echo     [-] Para mas informacion, ingrese el comando id root. >> GID_UID_root.txt ')

os.system('rm root_GID_UID_0.txt')
