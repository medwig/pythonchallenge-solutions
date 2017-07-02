import urllib.request
import re

# Get the input data from the problem webpage
url = 'http://www.pythonchallenge.com/pc/def/equality.html'
with urllib.request.urlopen(url) as response:
   html = response.read().decode('utf-8')
data = html.split('<!--')[1].strip()
print(f'Input data:\n{data[:60]}...(truncated)\n')

# Hint suggests a lowercase letter with exactly 3 uppercase on either side
matches = re.findall(r'[^A-Z]([A-Z]{3}[a-z][A-Z]{3})[^A-Z]', data)
print(f'Target strings:\n{matches}\n') 
letters = ''.join([i[3] for i in matches])
print(f'Target letters:\n{letters}\n') 

# Build the solution url by replacing the path end with the anagram
newUrl = url.split('/')
newUrl[-1] = letters + '.html'
newUrl = '/'.join(newUrl)

print(f'Url solution page:\n{newUrl}\n')
with urllib.request.urlopen(newUrl) as response:
   html = response.read().decode('utf-8')
print(f'Content of solution page:\n{html.strip()}\n')

# Solution page content suggests replacing '.html' with '.php' in the url
solution = newUrl.replace('.html', '.php')
print(f'Solution url:\n{solution}\n')
