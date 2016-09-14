import os, re

os.system('cat /etc/passwd >> usuarios_uid.txt')

archivo = open('usuarios_uid.txt','r').readlines()

usuarios = []

for x in archivo:
    mod_x = x.split(':')
    if int(mod_x[2])>=500 and x.find('nobody')<=0:
        usuarios.append(x)


for i in usuarios:
    archivo_usuarios = open('usuarios_temporales.txt','a')
    archivo_usuarios.write(i)
    archivo_usuarios.close()

os.system('rm usuarios_uid.txt')

usuarios_finales = open('usuarios_temporales.txt','r').readlines()

os.system('cat usuarios_temporales.txt | cut -f1 -d: >> usuarios.txt')

os.system('rm usuarios_temporales.txt')

usuarios_home = open('usuarios.txt','r').readlines()

for w in usuarios_home:
    user = w[:-1]
    os.system('touch temp.txt')
    os.system('touch resultados_finales.txt')    
    os.system('ls /home/' + str(user) + ' > temp.txt 2>&1')
    temporal = open('temp.txt','r').read()
    #print temporal
    if temporal.find('No such file')>=0 or temporal.find('No existe el archivo')>=0 or re.match('ls*',temporal):
        no = 'El usuario ' +str(user) + ' no posee su carpeta personal en el directorio /home/.'
        os.system('echo ' + str(no) + ' >> resultados_finales_home_directories.txt')
    else:
        si = 'El usuario ' +str(user) + ' posee su carpeta personal en el directorio /home/.'
        os.system('echo ' + str(si) + ' >> resultados_finales_home_directories.txt')
    os.system('rm temp.txt')

os.system('rm usuarios.txt')
