import sys
import requests
import re
from bs4 import BeautifulSoup

def get_encoding(soup):
    if soup and soup.meta:
        encod = soup.meta.get('charset')
        if encod == None:
            encod = soup.meta.get('content-type')
            if encod == None:
                content = soup.meta.get('content')
                match = re.search('charset=(.*)', content)
                if match:
                    encod = match.group(1)
                else:
                    return "N/A"
    else:
        return "N/A"
    return encodings

encodings = set()

for line in sys.stdin:
	if (line != "" and line != "\n"): #not empty line
		url = line.strip() #read in each URL from the URL file
		try:
			source = requests.get(url)
		except:
			print("Link broken for " + url, file=sys.stderr)
			continue


		try:
			soup = BeautifulSoup(source.content, 'lxml')

			encoding = get_encoding(soup)

		    #fails to retrieve encoding using tag, try Unicode Dammit
			if (encoding == "N/A"): 
				encoding = soup.original_encoding

			encodings.add(encoding)
		except:
			print("Can not make soup for " + url, file = sys.stderr)

print(encodings)