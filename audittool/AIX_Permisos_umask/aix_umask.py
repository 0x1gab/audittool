import os

os.system('cat /etc/passwd |cut -f1 -d: >> usuarios.txt')

usuarios = open('usuarios.txt', 'r').readlines()

for x in usuarios:
    user = x[:-1]
    os.system("lsuser -a umask " + str(user) + ' >> temp.txt')
    temp = open('temp.txt','r')
    temp_leer = temp.read()
    
    if temp_leer.find('0027')>=0:
        revision = open('revisar.txt','a')
        revision_escribir = revision.write('[+] La umask del usuario ' + str(user) + ' se encuentra configurada de forma correcta' + ' \n')
        revision_escribir = revision.write('\t [-] El valor umask del usuario, actualmente es: ' + str(temp_leer))
        revision.close()
    else:
        revision = open('revisar.txt','a')
        revision_escribir = revision.write('\t \t[+] La umask del usuario ' + str(user) + ' se encuentra configurada de forma incorrecta, ya que debe ser 0027. ' + ' \n')
        revision_escribir = revision.write('\t \t \t [-] El valor umask del usuario, actualmente es: ' + str(temp_leer))
        revision.close()
                                           
    os.system('rm temp.txt')

os.system('rm usuarios.txt')
