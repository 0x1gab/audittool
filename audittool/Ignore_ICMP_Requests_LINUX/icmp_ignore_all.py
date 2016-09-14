import os

os.system('sudo cat /proc/sys/net/ipv4/icmp_echo_ignore_all >> valor_icmp_echo_ignore_all.txt')

valor = open('valor_icmp_echo_ignore_all.txt','r')
lectura_valor = valor.read()

revisar_nuevo = open('valor_recomendado.txt','w')

if lectura_valor.find('0')>=0:
    valor.close()
    revisar_escritura = revisar_nuevo.write('[+]El valor actual del archivo /proc/sys/net/ipv4/icmp_echo_ignore_all es incorrecto: ' + str(lectura_valor) )
    revisar_escritura = revisar_nuevo.write('\t [-] Debe ser cambiado a 1')
else:
    valor.close()
    revisar_escritura = revisar_nuevo.write(' [+]El valor actual del archivo /proc/sys/net/ipv4/icmp_echo_ignore_all es [1], por lo que es correcto.')

os.system('rm valor_icmp_echo_ignore_all.txt')

          
