#!/usr/bin/python2.7
# coding: utf-8

import os
import re
import urllib
import urllib2
from bs4 import BeautifulSoup
from config import *
from datetime import datetime
from dateutil.relativedelta import relativedelta

def init():
	if not os.path.exists(REP_OUTPUT):
		os.makedirs(REP_OUTPUT)

def setCurrencies():
	liste = ["audusd", "eurusd", "eurgbp", "eurchf", "eurjpy", "usdcad", "nzdusd"]

	print"\n---------------"
	print "Liste des devises possible de traiter" 
	
	print "1: audusd, eurusd, eurgbp, eurchf, eurjpy, usdcad, nzdusd"
	print "2: audusd"
	print "3: eurusd"
	print "4: eurgbp"
	print "5: eurchf"
	print "6: eurjpy"
	print "7: usdcad"
	print "8: nzdusd"
	print"---------------\n"

	choice = int(raw_input("Entrez le nombre correspondant à votre choix:\n"))

	while choice <= 0 or choice > 8:
		print choice
		print "Votre choix n'est pas dans la liste"
		choice = raw_input("Entrez à nouveau le nombre correspondant à votre choix:\n")

	if(choice is 1 ):
		l = liste
	else:
		l = [liste[choice-2]]
				
	return l

def collectInfos():
	l_devises = setCurrencies()
	print "devises traitées:", l_devises

	start_d = getDate("Entrez la date de départ (mm/yyyy):")
	end_d = getDate("Entrez la date de fin (mm/yyyy):")

	print "début: %s, fin %s" % (start_d,end_d,) 
	
	return (start_d, end_d, l_devises)

def getDate(mess):
	d = raw_input(mess +"\n")
	while not re.match("^[0-9]{2}/[0-9]{4}$", d):
		print "Veuillez entrer une date de la forme 'mm/yyyy'"
		d = raw_input(mess +"\n")
	return d

def getParams(addr):
	p = {};
	html = urllib.urlopen(addr).read()
	soup = BeautifulSoup(html, "html.parser")

	# get all the inputs in the form
	form = soup.find("form",id="file_down")

	for child in form.children:
		try:
			attr = child['name']
			p[attr] = child['value']
		except:
			pass

	return p;

def setHeader(p):
	month = int(p["datemonth"][-2:])
	return {
		"Host": "www.histdata.com",
		"Connection": "keep-alive",
		"Content-Length": "101",
		"Cache-Control": "max-age=0",
		"Origin": "http://www.histdata.com",
		"Upgrade-Insecure-Requests": "1",
		"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
		"Content-Type": "application/x-www-form-urlencoded",
		"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
		"Referer": "http://www.histdata.com/download-free-forex-historical-data/?/"+ DATA_SOURCE +"/"+ DATA_FREQUENCY +"/"+ p["fxpair"] +"/"+ p["date"] +"/"+ str(month),
		"Accept-Language": "en-US,en;q=0.8,fr;q=0.6",
		"Cookie": "__cfduid=dc63bc2074225879801413509210cdecf1479486569; complianceCookie=on"
	}

def dlDataMonth(addr):
	ret = True
	values = getParams(addr)
	headers = setHeader(values)

	data = urllib.urlencode(values)
	req = urllib2.Request(POST_URL, data, headers)
	try:
		devise = values["fxpair"]
		response = urllib2.urlopen(req)
		result = response.read()

		if not os.path.exists(REP_OUTPUT + devise):
			os.makedirs(REP_OUTPUT + devise)

		path = REP_OUTPUT + devise +'/'+ devise +'_'+ values["datemonth"] +'_MT_M1.zip'


		with open(path, 'wb') as file:
			file.write(result)

	except :
		ret = False; 
		print "l'addresse url %s n'existe pas" % (addr,)

	return ret

def buildUrl(date, dev):
	if not isinstance(date, datetime):
		raise TypeError("Veuillez entrer un type date")
	return 'http://www.histdata.com/download-free-forex-historical-data/?/'+ DATA_SOURCE +'/'+ DATA_FREQUENCY +'/'+ dev +'/'+ str(date.year) +'/'+ str(date.month)

# attend un string de type mm/yyyy 
def dlDevise(start_d, end_d, dev):
	curr_d = datetime.strptime("01/"+ start_d, "%d/%m/%Y")
	end_d = datetime.strptime("01/"+ end_d, "%d/%m/%Y")
	keepAlive = True

	while(curr_d < end_d and keepAlive):
		print curr_d
		print type(curr_d)
		url = buildUrl(curr_d, dev)
		keepAlive = dlDataMonth(url)
		curr_d += relativedelta(months=1)


def dl(start_d, end_d, l_devises):
	for devise in l_devises:
		dlDevise(start_d, end_d, devise)


if __name__ == "__main__":
	init()
	start_date, end_date, devises = collectInfos()
	dl(start_date, end_date, devises)













	





