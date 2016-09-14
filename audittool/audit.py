#!/usr/bin/python

# Audit Module Root Secure - v1.4.0

# Gabriel Franco Root Secure Security Consultant

# gfranco@root-secure.com

import os
import time
import sys

global os, sys, time, re

def Cuentas_Sistema_Deshabilitadas():
    print '[+] Deteccion de cuentas del sistema deshabilitadas.'
    time.sleep(1)
    print ' \t [-] Se estan listando los usuarios actuales'
    time.sleep(1)
    print ' \t [-] Revisando usuarios y cuentas del sistema'
    time.sleep(1)
    print ' \t [-] Revisando usuarios locales'
    time.sleep(1)
    print ' \t [-] Generando reporte'
    time.sleep(1)
    print ' \t [-] Los resultados seran almacenados en /tmp/audittool/Cuentas_Sistema_Deshabilitadas/'
    os.system('sudo python Cuentas_Sistema_Deshabilitadas/Cuentas_Sistema.py')
    os.system('sudo mkdir /tmp/audittool/Cuentas_Sistema_Deshabilitadas/')
    os.system('sudo mv revisar_usuarios.txt /tmp/audittool/Cuentas_Sistema_Deshabilitadas/ ')
    os.system('sudo rm Cuentas_del_Sistema.txt')
    print

def Directorio_userROOT_es_root():
    print '[+] Deteccion de existencia de directorio /root/ para el usuario root.'
    time.sleep(2)
    print ' \t [-] Se esta corroborando la existencia del directorio /root/'
    os.system('sudo chmod 755 Directorio_de_ROOT_root/./directorio_usuario_root.sh')
    os.system('sudo Directorio_de_ROOT_root/./directorio_usuario_root.sh')
    time.sleep(1)
    print ' \t [-] Generando reporte'
    time.sleep(1)
    print ' \t [-] Los resultados seran almacenados en /tmp/audittool/Directorio_de_ROOT_root/'
    os.system('sudo mkdir /tmp/audittool/Directorio_de_ROOT_root/')
    os.system('sudo mv revision_directorio_root.txt /tmp/audittool/Directorio_de_ROOT_root/')
    print

def Dispositivos_USB_Permisos_Solo_root():
    print '[+] Detectando si los dispositivos USB en /media/ poseen permisos solo del usuario root.'
    time.sleep(1)
    print '\t [-] Corroborando permisos en /media/'
    print '\t [-] Generando reporte'
    time.sleep(1)
    os.system('sudo python Dispositivos_USB_Permisos_root/dispositivos_usb.py')
    print '\t [-] Los resultados seran almacenados en /tmp/audittool/Permisos_USB'    
    os.system('sudo mkdir /tmp/audittool/Permisos_USB/')
    os.system('sudo mv revisar_permisos_usb.txt /tmp/audittool/Permisos_USB/')   
    print

def Permisos_SGID_SUID_en_archivos_globales():
    print '[+] Detectando la configuracion de los archivos con atributos SGID / SUID.'
    os.system('sudo chmod 755 Files_Globales_Permisos_SUID-SGID/./listado_archivos_SUID_SGID.sh')
    os.system('sudo Files_Globales_Permisos_SUID-SGID/./listado_archivos_SUID_SGID.sh 2> temp.txt')
    time.sleep(1)
    print '\t [-] Recopilando informacion de archivos con estos atributos.'
    time.sleep(1)
    print '\t [-] Cargando permisos de los archivos.'
    time.sleep(1)
    os.system('sudo python Files_Globales_Permisos_SUID-SGID/suid_sgid_permisos.py')
    print '\t [-] Los resultados seran almacenados en /tmp/audittool/Archivos_Permisos_SUID-SGID'
    os.system('mkdir /tmp/audittool/Archivos_Permisos_SUID-SGID')
    os.system('mv permisos_suid_sgid.txt /tmp/audittool/Archivos_Permisos_SUID-SGID/')
    os.system('rm archivos_con_suid_sgid.txt')
    os.system('rm temp.txt')
    print

def Ignore_All_ICMP_Requests():
    print '[+] Se verificara la posibilidad de que este equipo reciba conexiones ICMP. '
    time.sleep(1)
    print '\t [-] Intentando enviar un paquete ICMP para determinar estado de configuracion'
    time.sleep(2)
    os.system('python Ignore_ICMP_Requests_LINUX/icmp_ignore_all.py')
    print '\t [-] Generando reporte'
    time.sleep(1)
    print '\t [-] Los resultados seran almacenados en /tmp/audittool/ICMP_Status_Requests'
    os.system('sudo mkdir /tmp/audittool/ICMP_Status_Requests/')
    os.system('sudo mv valor_recomendado.txt /tmp/audittool/ICMP_Status_Requests/')
    print

def IP_Forwarding():
    print '[+] Se verificara el estado de configuracion de IP Forwarding. '
    time.sleep(1)
    print '\t [-] Intentando reconocer parametros de configuracion. '
    os.system('sudo python IP_Forwarding/ip_forward.py')
    time.sleep(1)
    print '\t [-] Generando reporte'
    time.sleep(1)
    os.system('sudo mkdir /tmp/audittool/IP_Forward_Status/')
    print '\t [-] Los resultados seran almacenados en /tmp/audittool/IP_Forward_Status'
    os.system('sudo mv valor_recomendado_ip_forward.txt /tmp/audittool/IP_Forward_Status/')
    print

def Permisos_umask_Usuarios():
    print '[+] Se verificara la configuracion umask de todos los usuarios del sistema.'
    print '\t [!] Aclaracion: Si en la salida se encuentran valores nulos o que a la cuenta no es posible accederla, hacer el favor de omitirlos.'
    time.sleep(1)
    os.system('sudo python Linux_Permisos_umask/python_umask.py')
    print '\t [-] Se estan listando los usuarios con su correspondiente umask.'
    time.sleep(1)
    print '\t [-] Generando reporte'
    os.system('sudo mkdir /tmp/audittool/Permisos_umask_Usuarios/')
    print '\t [-] Los resultados se encuentran disponibles en la siguiente ruta /tmp/auditool/Permisos_umask_Usuarios/'
    os.system('sudo mv revisar_permisos_umask.txt /tmp/audittool/Permisos_umask_Usuarios/')
    print
    
def NTP_BroadcastClient_Disabled():
    print '[+] Se procedera a verificar si el demonio NTP este configurado para trabajar de forma UNICAST'
    time.sleep(1)
    print '\t [-] Analizando configuracion NTP'
    time.sleep(1)
    os.system('sudo python NTP_Broadcast_Disabled/broadcast_disabled.py')
    print '\t [-] Generando reporte'
    time.sleep(1)
    print '\t [-] Los resultados seran almacenados en /tmp/auditool/NTP_Configuration_Status/'
    os.system('sudo mkdir /tmp/audittool/NTP_Configuration_Status/')
    os.system('mv salida_configuracion_ntp.txt /tmp/audittool/NTP_Configuration_Status/')
    print

def Permisos_Directorio_root():
    print '[+] Se procedera a verificar los permisos del directorio /root/.'
    time.sleep(1)
    print '\t [-] Listando permisos de directorio /root/'
    os.system('sudo python Permisos_Directorio_root/Permisos_Directorio_root.py')
    time.sleep(1)
    print '\t [-] Generando reporte'
    print '\t [-] Los resultados seran almacenados en /tmp/audittool/Permisos_Directorio_root/'
    time.sleep(1)
    os.system('sudo mkdir /tmp/audittool/Permisos_Directorio_root/')
    os.system('sudo mv permisos_directorio_root.txt /tmp/audittool/Permisos_Directorio_root/')
    print

def Permisos_LOGS():
    print '[+] Se procedera a verificar los permisos de los archivos y directorios de LOGS'
    time.sleep(1)
    print '\t [-] Verificando los permisos de los archivos de logs.'
    print '\t [-] Verificando los permisos de los directorios que contengan logs.'
    os.system('sudo python Permisos_LOGS/Permisos_logs.py')
    print '\t [-] Generando reporte'
    print '\t [-] Los resultados seran almacenados en /tmp/audittool/Permisos_LOGS'
    time.sleep(1)
    os.system('sudo mkdir /tmp/audittool/Permisos_LOGS')
    os.system('sudo mv permisos_logs.txt /tmp/audittool/Permisos_LOGS/')
    time.sleep(1)
    print

def UID_GID_Usuario_root():
    print '[+] Se verificara que el usuario ROOT su UID y GID sean 0.'
    time.sleep(1)
    os.system('sudo python Root_UID_GID_0/Root_GID-UID_0.py')
    print '\t [-] Corroborando estado del usuario root'
    time.sleep(1)
    print '\t [-] Generando reporte.'
    print '\t [-] Los resultados seran almacenados en /tmp/audittool/UID_GID_Usuario_root/'
    time.sleep(1)
    os.system('sudo mkdir /tmp/audittool/UID_GID_Usuario_root/')
    os.system('sudo mv GID_UID_root.txt /tmp/audittool/UID_GID_Usuario_root/')
    print

def Timeout_Terminales_Ausencia():
    print '[+] Se verificara si el existe un tiempo de timeout por ausencia en la terminal cuando se realizan conexiones por SSH.'
    time.sleep(1)
    print '\t [-] Corroborando configuracion de SSH'
    time.sleep(1)
    os.system('sudo python Timeout_Terminales_Por_Ausencia/timeout.py')
    print '\t [-] Generando reporte.'
    print '\t [-] Los resultados seran almacenados en /tmp/audittool/Timeout_Terminales_SSH/'
    time.sleep(1)
    os.system('sudo mkdir /tmp/audittool/Timeout_Terminales_SSH/')
    os.system('sudo mv configuracion_para_aplicar.txt /tmp/audittool/Timeout_Terminales_SSH/')
    print

def UIDs_Unicos():
    print '[+] Se verificaran los UIDs de todos los usuarios.'
    time.sleep(1)
    print '\t [-] Listando usuarios y UID'
    time.sleep(1)
    os.system('chmod 755 UIDs_Unicos/./uid_usuario.sh')
    os.system('UIDs_Unicos/./uid_usuario.sh')
    os.system('python UIDs_Unicos/uid.py')
    print '\t [-] Generando reporte.'
    print '\t [-] Los resultados seran almacenados en /tmp/audittool/UIDs_Unicos_usuarios/'
    time.sleep(1)
    os.system('sudo mkdir /tmp/audittool/UIDs_Unicos_usuarios/')
    os.system('mv revisar_UIDs_unicos.txt /tmp/audittool/UIDs_Unicos_usuarios/')
    print

def Directorios_Home_usuarios():
    print '[+] Se verificaran los directorios /home/ de los usuarios del sistema.'
    time.sleep(1)
    print '\t [-] Listando usuarios y sus respectivos directorios personales.'
    time.sleep(1)
    os.system('sudo python Home_Usuario/home_usuario.py')
    time.sleep(1)
    print '\t [-] Generando reporte.'
    print '\t [-] Los resultados seran generados en /tmp/audittool/Directorios_Home_usuarios/'
    time.sleep(1)
    os.system('sudo mkdir /tmp/audittool/Directorios_Home_usuarios')
    os.system('sudo mv resultados_finales_home_directories.txt /tmp/audittool/Directorios_Home_usuarios/')
    os.system('sudo rm resultados_finales.txt')
    print

def Usuarios_Grupos():
    print '[+] Se verificaran todos los usuarios del sistema con su correspondiente grupo.'
    time.sleep(1)
    print '\t [-] Listando usuarios.'
    time.sleep(1)
    os.system('chmod 755 Usuarios_Grupos/usuarios_grupos.sh')
    print '\t [-] Listando grupos de usuarios'
    time.sleep(1)
    os.system('Usuarios_Grupos/./usuarios_grupos.sh')
    print '\t [-] Generando reporte.'
    print '\t [-] Los resultados seran generados en /tmp/audittool/Usuarios_y_Grupos/'
    time.sleep(1)
    os.system('sudo mkdir /tmp/audittool/Usuarios_y_Grupos')
    os.system('sudo mv usuarios_grupos.txt /tmp/audittool/Usuarios_y_Grupos/')
    print

def Permisos_etc_passwd():
    print '[+] Se verificaran los permisos del directorio /etc/passwd. '
    time.sleep(1)
    print '\t [-] Analizando permisos del directorio. '
    time.sleep(1)
    os.system('python Permisos_etc-passwd/etc-passwd_permisos.py')
    print '\t [-] Generando reporte. '
    print '\t [-] Los resultados seran generados en /tmp/audittool/Permisos_etc-passwd/'
    time.sleep(1)
    os.system('sudo mkdir /tmp/audittool/Permisos_etc-passwd/ ')
    os.system('sudo mv resultado_permisos_etc-passwd.txt /tmp/audittool/Permisos_etc-passwd/')

def Permisos_etc_shadow():
    print '[+] Se verificaran los permisos del directorio /etc/shadow. '
    time.sleep(1)
    print '\t [-] Analizando los permisos del directorio. '
    time.sleep(1)
    os.system('python Permisos_etc-shadow/etc-shadow_permisos.py')
    print '\t [-] Generando reporte. '
    print '\t [-] Los resultados seran generados en /tmp/audittool/Permisos_etc-shadow/'
    time.sleep(1)
    os.system('sudo mkdir /tmp/audittool/Permisos_etc-shadow/')
    os.system('sudo mv resultado_permisos_etc-shadow.txt /tmp/audittool/Permisos_etc-shadow/')
    
os.system('clear')

print
print
print
print '\t \t \t \t \t \t  ** This tool was developed by Gabriel Franco and Jorge Sodanelli *'
print '\t \t \t \t \t \t                   ** Use by your own risk **                    '
print '\t \t \t \t \t \t   * This tool requires privileges, so please use with it. *     '
print
print
print

# Sacar esto para que nadie tenga que presionar nada [.]-[.]
raw_input('Press a key before you begin ...')

os.system('clear')


try:
    if sys.argv[1]=='-V':
        print
        print        
        print '\t     #####   ##   ## #######   ## ########     ##                  ##         ####          '
        print '\t    #######  ##   ## ##    ##  ##    ##      ######                ##           ##          '
        print '\t   ##     ## ##   ## ##     ## ##    ##        ##    ###### ###### ##           ##          '
        print '\t   ######### ##   ## ##     ## ##    ##        ##    #    # #    # ##    #   #  ##   ## ##  '
        print '\t   ##     ## ##   ## ##    ##  ##    ##        ##    #    # #    # ##     # #   ##     #    '
        print '\t   ##     ## ####### #######   ##    ##        ####  ###### ###### ##      #    ## # ## ##  '
        print                                                               
        print        
        os.system('sudo mkdir /tmp/audittool/')
        Cuentas_Sistema_Deshabilitadas()
        Directorio_userROOT_es_root()
        Dispositivos_USB_Permisos_Solo_root()
        Permisos_SGID_SUID_en_archivos_globales()
        Ignore_All_ICMP_Requests()
        IP_Forwarding()
        Permisos_umask_Usuarios()
        NTP_BroadcastClient_Disabled()
        Permisos_Directorio_root()
        Permisos_LOGS()
        UID_GID_Usuario_root()
        Timeout_Terminales_Ausencia()
        UIDs_Unicos()
        Directorios_Home_usuarios()
        Usuarios_Grupos()
        Permisos_etc_passwd()
        Permisos_etc_shadow()

# Donde se guardaran los archivos sera el directorio /NOMBREDESERVER/, descomentar esta linea si se requiere asi.

        #os.system('uname -n > nombre.txt')
        #nombre_archivo = open('nombre.txt','r')
        #nombre_carpeta = nombre_archivo.read()
        #os.system('mv /tmp/audittool/ /tmp/audittool_' + str(nombre_carpeta))
        #os.system('rm nombre.txt')

        print 'Thanks for using this tool.'
        print
        print
        print 'Todos los resultados se encuentran en la carpeta ' + str(nombre_carpeta) + '/tmp/audittool'
        print
        print        
except:
    print
    print
    print 'manpage for audit.py coming in the next version'
    print 'try just -V option for this demo, verbose mode'
    print
    print
