#!/usr/bin/python

import feedparser

#Top stories
url = 'http://feeds.bbci.co.uk/news/world/rss.xml?edition=uk'



d = feedparser.parse(url)

length = len(d['entries'])

for i in range(0,length):
	print d['entries'][i]['title']
	if d['entries'][i]['description'] is None:
		continue
	else:
		print 'Description:'
		print d['entries'][i]['description']
	


