import urllib.request
import re
import string

# Get the input data from the problem webpage
url = 'http://www.pythonchallenge.com/pc/def/map.html'
with urllib.request.urlopen(url) as response:
   html = response.read().decode('utf-8')
data = re.search('g.*spj\.', html)
data = data.group(0)
print('Input data:\n', data, '\n') 

# Image hint suggests a shift cipher with shift=2
alphabet = string.ascii_lowercase 
cipher = alphabet[2:] + alphabet[:2]
trans_table = str.maketrans(alphabet, cipher)
decoded = data.translate(trans_table)
print('Decoded input data:\n', decoded, '\n') 

# Decrypted message says to apply cipher to url. Trial and error reveals only the end of the url path is targeted
splitUrl = url.split('/')
target = splitUrl[-1].rstrip('.html')
transTarget = target.translate(trans_table)
newUrl = splitUrl[:]
newUrl[-1] = transTarget + '.html'
newUrl = '/'.join(newUrl)

solution = newUrl
print('Solution url:\n', solution, '\n')
