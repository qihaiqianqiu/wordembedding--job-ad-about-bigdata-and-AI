filename = "vec.txt"
output = "goodvec.txt"
f1 = open(filename,"r")
f2 = open(output,"aw")

line = f1.readline()
content = []
temp = []
i = 0
while line:
	for char in line:
		if char == ']':
			i += 1
	if i == 0:
		temp.append(line)
		line = f1.readline()
	if i == 1:
		temp.append(line)
		content.append(temp)
		temp = []
		i = 0
		line = f1.readline()

for i in range(0,6201):
	f2.write(str(content[i]))
	f2.write("\n")
	