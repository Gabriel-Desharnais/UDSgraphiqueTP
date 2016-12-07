#! /usr/bin/python3
# coding: utf8
'''Ce fichier permet de montrer le fonctionnement du module «presentation»'''
import matplotlib.pyplot as plt
from presentation import *

x=list(range(42))
y=[(1/42)*X**2  for X in x]

plt.plot(x,y,'.',label=r'$y=a*x^{2}$')

plt.legend(loc=2)
#nommer les axes
plt.xlabel(r"Temps écoulé $t$ (s)")
plt.ylabel(r'Position $y$ (m)')
#Enregistrer une image png du graphique
plt.savefig('Exemple.png',bbox_inches='tight')
#Afficher le graphique
plt.show()
