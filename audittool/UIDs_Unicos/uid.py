import os

archivo = open('resultado.txt','r').read()

archivo = archivo.split(' ')
del archivo[-1]

for x in archivo:
    os.system('id ' + str(x) + ' >> revisar_UIDs_unicos.txt')
    

os.system('rm resultado.txt')
