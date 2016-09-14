import os

os.system('sudo cat /etc/shadow >> Cuentas_del_Sistema.txt')

archivo = open('Cuentas_del_Sistema.txt','r').readlines()

for x in archivo:
    aux = x.split(':')
    usr = aux[0]
    if x.find(':*:')<=0:
        linea = 'Revisar si el siguiente usuario se encuentra aprobado para estar habilitado >>>>>>>>: \t' + str(usr)
        archivo_revision = open('revisar_usuarios.txt','a')
        archivo_revision.write(linea + ' \n')
