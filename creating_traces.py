import os

def steep_decrease_content():
	content = ""
	for i in range(1 , 16000 + 1):
			for j in range(4): 
				content += "{}\n".format(i)

	for i in range(16000 + 1, 32000 + 1):
		content += "{}\n".format(i)
	return content

def steep_increase_content():
	content = ""
	for i in range(1, 16000 + 1):
		for j in range(12):
			content += "{}\n".format(i)
	for i in range(16000 + 1, 32000 + 1):
		for j in range(4):
			content += "{}\n".format(i)

	return content

def variable_bandwidths_content(): 
	content = ""
	for i in range(1, 8000 + 1): 
		for j in range(4): 
			content += "{}\n".format(i)

	for i in range(8000 + 1, 16000 + 1):
		content += "{}\n".format(i)

	for i in range(16000 + 1, 24000 + 1):
		for j in range(4):
			content += "{}\n".format(i)

	for i in range(24000 + 1, 32000 + 1): 
		content += "{}\n".format(i)
	return content



working_dir = "traces"

filepath = working_dir + "/variable_cycle"

# Check if working directory exists
if not os.path.isdir(working_dir):
	os.mkdir(working_dir)

with open(filepath, "w") as file:
	# file.write(steep_decrease_content())
	# file.write(steep_increase_content())
	file.write(variable_bandwidths_content())


