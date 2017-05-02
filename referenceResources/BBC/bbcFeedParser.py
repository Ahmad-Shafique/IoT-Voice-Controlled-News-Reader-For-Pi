#!/usr/bin/python

import urllib2
import re
import numpy


def removeDtdChars(var):
	var2 = var
	l1 = len(var2[0])
	var2 = var2[0][2:l1-2]
	return var2


# URL
#World
#url_str = 'http://feeds.bbci.co.uk/news/world/rss.xml?edition=uk'
#UK
#url_str = 'http://feeds.bbci.co.uk/news/uk/rss.xml?edition=uk'
#England
#url_str = 'http://feeds.bbci.co.uk/news/england/rss.xml?edition=uk'
#North Ireland
#url_str = 'http://feeds.bbci.co.uk/news/northern_ireland/rss.xml?edition=uk'
#Scotland
#url_str = 'http://feeds.bbci.co.uk/news/scotland/rss.xml?edition=uk'
#Wales
#url_str = 'http://feeds.bbci.co.uk/news/wales/rss.xml?edition=uk'
#Business
#url_str = 'http://feeds.bbci.co.uk/news/business/rss.xml?edition=uk'
#Politics
#url_str = 'http://feeds.bbci.co.uk/news/politics/rss.xml?edition=uk'
#Health
#url_str = 'http://feeds.bbci.co.uk/news/health/rss.xml?edition=uk'
#Education
#url_str = 'http://feeds.bbci.co.uk/news/education/rss.xml?edition=uk'
#Science and Environment
#url_str = 'http://feeds.bbci.co.uk/news/science_and_environment/rss.xml?edition=uk'
#Technology
#url_str = 'http://feeds.bbci.co.uk/news/technology/rss.xml?edition=uk'
#Arts and entertainment
#url_str = 'http://feeds.bbci.co.uk/news/entertainment_and_arts/rss.xml?edition=uk'
#Magazines
url_str = 'http://feeds.bbci.co.uk/news/magazine/rss.xml'


xml_str = urllib2.urlopen(url_str).read()



titles =re.findall(r"<title>.*(A\[.*]]).*<\/title>",xml_str)

var = []

l = len(titles)
for i in range(0,l):
	var1 = numpy.array(re.findall(r"A\[.*]]",titles[i]))
	titles[i] = removeDtdChars(var1)
	
for i in range(0,l):
	print titles[i] 

	


