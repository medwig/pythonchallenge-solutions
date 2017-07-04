import urllib.request
import re
import operator

OPERATORS = {
    "divide": operator.floordiv
}
NUMBERS = {
    "one": 1,
    "two": 2
}

def replace_path_end(url, newEnd):
    newUrl = url.split('/')
    newUrl[-1] = newEnd 
    return '/'.join(newUrl)


# Get the input data from the problem webpage
URL = 'http://www.pythonchallenge.com/pc/def/linkedlist.php'
with urllib.request.urlopen(URL) as response:
   html = response.read().decode('utf-8')
data = re.findall(r'a href="(.*)">', html)[0]
print(f'Input data:\n{data}\n')

# The problem input data is a url - follow it
newUrl = replace_path_end(URL, data)
with urllib.request.urlopen(newUrl) as response:
   html = response.read().decode('utf-8')
print(f'Input data link reads:\n{html}\n')

# Hint suggests following resulting next 'nothing' numbers in the fashion of linked list with maxlength=400
print("Subbing 'nothing' into url gives next url: {}\n".format(re.sub(r'\d+', re.findall(r'next nothing is (\d+)', html)[0], newUrl)))
print("Walking through linked list subbing 'nothing' into urls as we go...")
url = newUrl
for i in range(400):
    if '.html' in html:
        target = html
        break
    try:
        nextNothing = re.findall(r'next nothing is (\d+)', html)[0]
        nextUrl = re.sub(r'\d+', nextNothing, url)
    except IndexError:  # Handle text-based math if no numbers are present
        oper, num = re.search(r'(\w+).by.(\w+)', html).groups()    
        print(f'\tNo number found, applying math: {oper} by {num}')
        nextNothing = OPERATORS[oper.lower()](int(nothing), NUMBERS[num])
        nextUrl = re.sub(r'\d+', str(nextNothing), url)
        
    with urllib.request.urlopen(nextUrl) as response:
        nextHtml = response.read().decode('utf-8')

    nothing = nextNothing
    url = nextUrl
    html = nextHtml

print(f'\nTarget found in linked list:\n{target}\n')

# Build the solution url by replacing the path end with the anagram
solution = replace_path_end(URL, target)

print(f'Url solution page:\n{solution}\n')

