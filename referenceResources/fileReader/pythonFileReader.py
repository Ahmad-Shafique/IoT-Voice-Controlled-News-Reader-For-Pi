

with open('bbc') as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content] 

for x in content:
	var = x.split(",")
	for z in var:
		print z 
	break
