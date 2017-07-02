import urllib.request
import collections
import string
import itertools

# Get the input data from the problem webpage
url = 'http://www.pythonchallenge.com/pc/def/ocr.html'
with urllib.request.urlopen(url) as response:
   html = response.read().decode('utf-8')
data = html.split('<!--')[2].strip('\n-->')
print(f'Input data:\n{data[:60]}...(truncated)\n')

# Source code hint suggests looking for rare characters in the input data (less a tenth of the avg)
counts = collections.Counter(data)
avgCount = sum(counts.values()) / len(counts.values())
rareChars = [key for key, value in counts.items() if value < avgCount / 10]
print(f'Rare characters in input data:\n{rareChars}\n') 

# Inspection suggests an anagram. Check permutations against Unix dictionary for matches
try:
    with open('/usr/share/dict/words', 'r') as f:
        words = {word for word in f.read().splitlines()}
except:
    print('Unix dictionary not found - using a harcoded dictionary instead')
    words = {'a', 'cheat', 'dictionary', 'that', 'includes', 'equality'}

for perm in itertools.permutations(rareChars):
    perm = ''.join(perm)
    if perm in words:
        anagram = perm
print(f'Rare characters are an anagram of:\n{anagram}\n') 

# Build the solution url by replacing the path end with the anagram
newUrl = url.split('/')
newUrl[-1] = anagram + '.html'
newUrl = '/'.join(newUrl)

solution = newUrl
print(f'Solution url:\n{solution}\n')
