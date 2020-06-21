import sys
import urllib.request 
from bs4 import BeautifulSoup

encodings = set()

for line in sys.stdin:
	url = line.strip() #read in each URL from the URL file

	if (url != ""): #not empty line
		try:
			source = urllib.request.urlopen(url)
		except:
			print("Link broken for " + url, file=sys.stderr)

		if (source is not None): #link is not broken
			try:
				soup = BeautifulSoup(source, 'lxml')
				encodings.add(soup.original_encoding)
			except:
				print("Can not make soup for " + url, file = sys.stderr)

print(encodings)