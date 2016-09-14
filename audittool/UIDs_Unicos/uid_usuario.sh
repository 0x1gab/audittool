#!/bin/bash

while read linea; do
echo $(cut -f1 -d: | sort) >> resultado.txt;
done < /etc/passwd

 
