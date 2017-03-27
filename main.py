#!/usr/bin/python2.7
# coding: utf-8

from config import *
from DownloadCurr import DownloadCurr
from DateConvertible import DateConvertible
import fileManager as fm
import fileReader as fr

def convertDataMinToDay(dic, ref_tz='utc'):
	if dic is not dict:
		raise("L'arg 1 doit être un dictionnaire...")

	#highV = 0, lowV = 100000, openV = 0, closeV = 0
	lastDay = DateConvertible("1970.01.01 00:00")

	for dat in dic:
		dateC = DateConvertible(dat[date] +' '+ dat[min], "America/New_York")
		dateC.changeTimeZone("Europe/Paris")

		if dateC.date


if __name__ == "__main__":

	DateConvertible.printing()
	# download the data on histdata
	# dl = DownloadCurr()
	# dl.dl(dl.start_date, dl.end_date, dl.devises)
	
	# dezippage + concatenation de fichier
	# fm.listAllFromRootFolder(REP_OUTPUT, fm.unzipData)
	# fm.listAllFromRootFolder(REP_OUTPUT, fm.deleteNonCsvFile)
	# fm.concatMultipleFolders("data", REP_PTF)

	# lire et transformer les data
	#fr.readFileIntoDict(REP_PTF+'AUDUSDcat.csv', ['date', 'min', 'open', 'high', 'low', 'close'])
	
	# ajout d'un timezone a la date
	dateC = DateConvertible("2016.12.03 08:34")
	dateD = DateConvertible("2016.12.03 11:27")

	
	# dateC.setTimeZone("America/New_York")
	# dateC.changeTimeZone("Europe/Paris")




	