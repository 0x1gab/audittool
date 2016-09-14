if [ -d /root/ ];
then
echo El directorio /root/, del usuario root existe > revision_directorio_root.txt;
else
echo El usuario root no posee su directorio /root/ > directorio_root.txt;
fi
