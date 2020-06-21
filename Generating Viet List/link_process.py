import sys

#outFile = open('urlFiles.txt', 'w') #saving all the URL links
for line in sys.stdin:
	temp = line.strip()
	if (temp == "" or temp == "<p>" or temp == "</p>" or temp == "</doc>"): #ignore cases where there is not going to be an URL
		continue
	else:
		loc = temp.find("url=")
		if (loc != -1): #if the line contains an URL
			#print out the URL
			print(temp[loc+5: temp.find("warc-file")-2] + "\n")
			#outFile.write(temp[loc+5: temp.find("warc-file")-2] + "\n")

#outFile.close()