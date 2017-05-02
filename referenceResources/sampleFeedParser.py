import feedparser

d = feedparser.parse('http://rss.cnn.com/rss/edition.rss')

print d['entries'][4]['title']
print d['entries'][4]['description']

