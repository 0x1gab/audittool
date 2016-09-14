import os

os.system('cat /etc/passwd |cut -f1 -d: >> usuarios.txt')

usuarios = open('usuarios.txt', 'r').readlines()

for x in usuarios:
    user = x[:-1]
    os.system("su -c 'umask' -l " + str(user) + ' > temp.txt 2>&1')
    temp = open('temp.txt','r')
    temp_leer = temp.read()
    
    if temp_leer.find('0027')>=0:
        revision = open('revisar_permisos_umask.txt','a')
        revision_escribir = revision.write('[+] La umask del usuario ' + str(user) + ' se encuentra configurada de forma correcta' + ' \n')
        revision_escribir = revision.write('\t [-] El valor umask del usuario, actualmente es: ' + str(temp_leer) + ' \n' + ' \n')
        revision.close()
    else:
        revision = open('revisar_permisos_umask.txt','a')
        revision_escribir = revision.write('[+] La umask del usuario ' + str(user) + ' se encuentra configurada de forma incorrecta, ya que debe ser 0027. ' + ' \n')
        revision_escribir = revision.write('\t [-] El valor umask del usuario, actualmente es: ' + str(temp_leer) + ' \n' + ' \n')
        revision.close()
                                           
    os.system('rm temp.txt')

os.system('rm usuarios.txt')
