#!/bin/bash
clear
echo "################################################################################"
echo "################################# WELCOME TO ###################################"
echo "#################################  MENS SANA ###################################"
echo "################################################################################"
echo "################################ BACKUP WZRD ###################################"
echo "################################################################################"
echo " "
echo "Digite 1 para realizar backup e 2 para restaurar backup:";
read option

if [ "$option" == "1" ];
then
  echo 'Insira a senha root do seu servidor mysql: '
  mysqldump -u root -p menssana > menssanadb1.sql
  if test 'find "menssanadb1.sql"';
  then
      rm menssanadb.sql
      mv menssanadb1.sql menssanadb.sql
      echo 'backup criado em menssanadb.sql'
  else
    echo "erro ao criar backup"
  fi
elif [ "$option" == "2" ]; then
  echo 'Insira a senha root do seu servidor mysql: '
  mysql -u root -p -h localhost menssana < menssanadb.sql
  echo "backup restaurado"
fi
