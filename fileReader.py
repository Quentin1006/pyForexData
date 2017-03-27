#!/usr/bin/python2.7
# coding: utf-8

from config import *

def readFileIntoDict(file, champs, delim=','):
	""" lit un fichier csv et met son contenu dans un tableau de dict """
	if type(champs) is not list:
		raise('Le 2eme argument doit etre une liste')

	globList = []

	with open(file, 'r') as fd:
		data = "".join(fd.readlines())
		data_cln = data.split("\r")

		for datamin in data_cln :
			tmpDict = {}
			tmpList = datamin.split(delim)
			for i, champ in enumerate(champs):
				#print "tmpList[%d] = %s" % (i, tmpList[i],)
				tmpDict[champ] = tmpList[i]

			globList.append(tmpDict)

	return globList





