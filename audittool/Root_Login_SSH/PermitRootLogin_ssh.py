#/usr/bin/python

import os

os.system('cat /etc/ssh/sshd_config |grep PermitRootLogin >> configuracion_rootlogin.txt')

rootlogin = open('configuracion_rootlogin.txt','r')
leer_rootlogin = rootlogin.read()

#print leer_rootlogin

if leer_rootlogin.find('#PermitRootLogin no')>=0 or leer_rootlogin.find('PermitRootLogin no')!=0:
    cerrar_rootlogin = rootlogin.close()
    final = open('configuracion_login_as_root_SSH.txt','w')
    esc_final = final.write(' [+] La configuracion no es correcta. \n')
    esc_final = final.write('\t [-] Es recomendable cambiar el parametro ' + str(leer_rootlogin) + ' a "PermitRootLogin no"')
    cerrar_final = final.close()
else:
    cerrar_rootlogin = rootlogin.close()
    final = open('configuracion_login_as_root_SSH.txt','w')
    esc_final = final.write(' [+]La configuracion es correcta. No se permite el servidor mediante el usuario ROOT. \n')
    cerrar_final = final.close()

#os.system('rm configuracion_rootlogin.txt')

