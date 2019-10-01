from urllib.request import Request, urlopen
import re
req = Request('https://www.google.com', headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
match=re.findall('<title>.*</title>',str(webpage),re.IGNORECASE)
print(match)
