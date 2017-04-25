#!/usr/bin/python





from xml.dom.minidom import parse
from bs4 import BeautifulSoup
import xml.dom.minidom
import urllib2
import re
import numpy


def removeDtdChars(var):
#	print var
	var2 = var
	l1 = len(var2[0])
#	print var2
#	print l1
	var2 = var2[0][2:l1-2]
#	print var2
	return var2


# Open XML document using minidom parser
url_str = 'http://feeds.bbci.co.uk/news/uk/rss.xml?edition=uk'

xml_str = urllib2.urlopen(url_str).read()
#soup = BeautifulSoup(xml_str)


titles =re.findall(r"<title>.*(A\[.*]]).*<\/title>",xml_str)

var = []

l = len(titles)
for i in range(0,l):
	var1 = numpy.array(re.findall(r"A\[.*]]",titles[i]))
	titles[i] = removeDtdChars(var1)
	
for i in range(0,l):
	print titles[i] 

	
#	print re.match(r"A\[.*]]",title)
	
	
#print soup.prettify()
#titles = soup.find_all('title')
#for title in titles:
#	print innerHTML(title)
	
	

