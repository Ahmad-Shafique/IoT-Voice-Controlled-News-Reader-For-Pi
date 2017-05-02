#!/usr/bin/python

import feedparser

#Top stories
#url = 'http://rss.cnn.com/rss/edition.rss'
#World 		
#url ='http://rss.cnn.com/rss/edition_world.rss'


d = feedparser.parse(url)

length = len(d['entries'])

for i in range(0,length):
	print d['entries'][i]['title']
	if d['entries'][i]['description'] is None:
		continue
	else:
		print 'Description:'
		print d['entries'][i]['description']
	


