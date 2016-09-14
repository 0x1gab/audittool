#!/bin/bash

while read linea; do
groups $(cut -f1 -d: | sort) >> usuarios_grupos.txt;
done < /etc/passwd
