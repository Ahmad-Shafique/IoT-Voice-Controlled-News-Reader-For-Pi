def selectProperUrl(channelName,category):
	if channelName == 'bbc':
		fileName = 'bbc.py'
	elif channelName == 'cnn':
		fileName = 'cnn'
	with open(fileName) as f:
		content = f.readlines()
	# you may also want to remove whitespace characters like `\n` at the end of each line
	content = [x.strip() for x in content] 

	category = category.lower()	
	
	for x in content:
		var = x.split(",")
		if category in var[0].lower() :
			return var[1]
	return ''

print selectProperUrl('bbc','world')
