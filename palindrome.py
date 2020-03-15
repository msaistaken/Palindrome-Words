def control(get):

	n=len(get)
	reverse=str()
	for i in range(n):

		reverse+=get[n-i-1]

	if get==reverse:
		print(get)

with open('index.verb','r') as f:
	a=f.readlines()

for i in a:
	control(str(i).split()[0])