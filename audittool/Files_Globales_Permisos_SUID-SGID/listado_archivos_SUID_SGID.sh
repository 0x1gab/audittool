#!/bin/sh

# busca todos los archivos en '/' con permiso 4000 SUID o 2000 SGID y los lleva al txt en formato ls

find /bin/ \( -perm -4000 -o -perm 2000 \) -ls >> archivos_con_suid_sgid.txt 

find /home/ \( -perm -4000 -o -perm 2000 \) -ls >> archivos_con_suid_sgid.txt

find /etc/ \( -perm -4000 -o -perm 2000 \) -ls >> archivos_con_suid_sgid.txt 

find /usr/ \( -perm -4000 -o -perm 2000 \) -ls >> archivos_con_suid_sgid.txt 

find /opt/ \( -perm -4000 -o -perm 2000 \) -ls >> archivos_con_suid_sgid.txt 

find /var/ \( -perm -4000 -o -perm 2000 \) -ls >> archivos_con_suid_sgid.txt 

find /boot/ \( -perm -4000 -o -perm 2000 \) -ls >> archivos_con_suid_sgid.txt 

find /root/ \( -perm -4000 -o -perm 2000 \) -ls >> archivos_con_suid_sgid.txt 

find /sys/ \( -perm -4000 -o -perm 2000 \) -ls >> archivos_con_suid_sgid.txt 

find /srv/ \( -perm -4000 -o -perm 2000 \) -ls >> archivos_con_suid_sgid.txt 
