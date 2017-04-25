#!/usr/bin/python

from xml.dom.minidom import parse
import xml.dom.minidom

# Open XML document using minidom parser
DOMTree = xml.dom.minidom.parse("rss.xml")
collection = DOMTree.documentElement

# Get all the movies in the collection
channel = collection.getElementsByTagName("channel")

# Print detail of each movie.
for chnl in channel:
	print "*****Channel News*****"

	items = chnl.getElementsByTagName('item')
	for item in items:
		description = item.getElementsByTagName('description')[0]
		print description.childNodes[0].data
