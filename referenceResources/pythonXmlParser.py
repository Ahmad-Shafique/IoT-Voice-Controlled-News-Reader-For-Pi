#!/usr/bin/python


from xml.dom.minidom import parse
import xml.dom.minidom
import urllib2

# Open XML document using minidom parser
#url_str = 'http://feeds.bbci.co.uk/news/world/rss.xml?edition=uk'
url_str = 'http://feeds.bbci.co.uk/news/uk/rss.xml?edition=uk'
#url_str = 'http://feeds.bbci.co.uk/news/world/rss.xml?edition=uk'
#url_str = 'http://feeds.bbci.co.uk/news/world/rss.xml?edition=uk'
#url_str = 'http://feeds.bbci.co.uk/news/world/rss.xml?edition=uk'
#url_str = 'http://feeds.bbci.co.uk/news/world/rss.xml?edition=uk'
#url_str = 'http://feeds.bbci.co.uk/news/world/rss.xml?edition=uk'
#url_str = 'http://feeds.bbci.co.uk/news/world/rss.xml?edition=uk'
#url_str = 'http://feeds.bbci.co.uk/news/world/rss.xml?edition=uk'
#url_str = 'http://feeds.bbci.co.uk/news/world/rss.xml?edition=uk'
#url_str = 'http://feeds.bbci.co.uk/news/world/rss.xml?edition=uk'
#url_str = 'http://feeds.bbci.co.uk/news/world/rss.xml?edition=uk'
#url_str = 'http://feeds.bbci.co.uk/news/world/rss.xml?edition=uk'
#url_str = 'http://feeds.bbci.co.uk/news/world/rss.xml?edition=uk'
#url_str = 'http://feeds.bbci.co.uk/news/world/rss.xml?edition=uk'
#url_str = 'http://feeds.bbci.co.uk/news/world/rss.xml?edition=uk'
#url_str = 'http://feeds.bbci.co.uk/news/world/rss.xml?edition=uk'
xml_str = urllib2.urlopen(url_str).read()
DOMTree = xml.dom.minidom.parse(xml_str)
collection = DOMTree.documentElement

# Get all the movies in the collection
channel = collection.getElementsByTagName("channel")


print DOMTree


# Print detail of each movie.
for chnl in channel:
	print "*****Channel News*****"

	items = chnl.getElementsByTagName('item')
	for item in items:
		description = item.getElementsByTagName('description')[0]
		print description.childNodes[0].data
