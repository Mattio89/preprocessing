

with open(r"Orlando_Data_Filtered.txt",'r', encoding="utf8") as input:
	for index, line in enumerate(input):
			with open('filename{}.txt'.format(index), 'w') as output:
				output.write(line)


