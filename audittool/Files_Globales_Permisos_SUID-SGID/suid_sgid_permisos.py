import os,re 

#os.system('chmod 755 ~/listado_archivos_SUID_SGID.sh')
#os.system('~/./listado_archivos_SUID_SGID.sh')

lista = []

archivo = open('archivos_con_suid_sgid.txt','r')
lectura_archivo = archivo.readlines()

for x in lectura_archivo:
    permiso = x.split()
    #print permiso[10]
    lista.append(permiso[2]+ ' del archivo ' + permiso[10])


for i in lista:
    aux = i.split()
    if re.match("....*w",aux[0]):
        descripcion_i = ': Revisar el archivo y cambiar, si es necesario los permisos de escritura, ya que solo deben ser otorgados al usuario root o el propio owner.'
        os.system('echo [+] Los permisos actuales son ' + str(i) + str(descripcion_i) + ' >> permisos_suid_sgid.txt')
        os.system('echo >> permisos_suid_sgid.txt')
        
    else:
        descripcion_i = ': Parece que el archivo solo tiene permisos de escritura por root. Igualmente, corroborar en esta vista.'
        os.system('echo [+] Los permisos actuales son ' + str(i) + str(descripcion_i) + ' >> permisos_suid_sgid.txt')
        os.system('echo >> permisos_suid_sgid.txt')


archivo.close()
