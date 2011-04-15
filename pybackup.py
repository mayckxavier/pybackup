# -*- coding: latin1 -*-
import os
import time

ano = time.localtime()[0]
mes = time.localtime()[1]
dia = time.localtime()[2]
hora = time.localtime()[3]
minuto = time.localtime()[4]
segundo = time.localtime()[5]
hoje = str(ano) + str(mes) + str(dia) + str(hora) + str(minuto) + str(segundo)

# - localbackup - Backup location
# - Eg. - localhost = '/home/myuser/backup/'
localbackup = ''

# - Fill the list with the directories you need backup
# - Eg. diretorios = ['/var/www/','/home/']
diretorios = []

# - Fill the name list like the following model 
# - Eg. arquivos = ['backupfile' + str(hoje) + '.tar.gz', 'backupfile2' + str(hoje) + 'tar.gz']
arquivos = []

i=0
for diretorio in diretorios:
	os.system('tar zcf ' + localbackup + ' ' + arquivos[i] + ' ' + diretorios[i])
	i = i+1

print "Your backup finished =)"
