from wifi import Cell, Scheme
#
var = Cell.all('wlan0')
#
for c in var:
	if c.ssid == 'aaa450':
		ssid = 'aaa450'
#		scheme = Scheme.for_cell('wlan0', 'aaa', c, 'pentium4')
#		#scheme.save()
#		scheme.activate()
#		break
	print c.ssid
#	
#scheme = Scheme.find('wlan0', 'aaa450')
#scheme.activate()

pas = 'pentium4'




from wireless import Wireless
wireless = Wireless()

wireless.connect(ssid='aaa450', password='pentium4')


