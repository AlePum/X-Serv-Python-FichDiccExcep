#!/usr/bin/python
# -*- coding: utf-8 -*-

fd = open('/etc/passwd', 'r')

lineas = fd.readlines()
fd.close()
DiccRootShell = {}

for linea in lineas:
    elementos = linea.split(':')
    root = elementos[0] 
    shell = elementos[-1][:-1]
    DiccRootShell[str(root)] = str(shell)
    try:
        print DiccRootShell["root"]
        print DiccRootShell["imaginario"]
    except:
        print "Busqueda de root incorrecta: no se encuentra en el diccionario"
    raise SystemExit