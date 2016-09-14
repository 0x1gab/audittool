import os

os.system('sudo cat /proc/sys/net/ipv4/ip_forward >> valor_ip_forward.txt')

valor = open('valor_ip_forward.txt','r')
lectura_valor = valor.read()

revisar_nuevo = open('valor_recomendado_ip_forward.txt','w')

if lectura_valor.find('0')>=0:
    valor.close()
    revisar_escritura = revisar_nuevo.write(' [+]El valor actual del archivo /proc/sys/net/ipv4/ip_forward es [0], por lo que es correcto.')

else:
    valor.close()
    revisar_escritura = revisar_nuevo.write('[+]El valor actual del archivo /proc/sys/net/ipv4/ip_forward es incorrecto: ' + str(lectura_valor) )
    revisar_escritura = revisar_nuevo.write('\t [-] Debe ser cambiado a 0')    

os.system('rm valor_ip_forward.txt')
