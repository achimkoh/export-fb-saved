# written in python3.5
from bs4 import BeautifulSoup as BS

# you need to first manually save your Facebook 'Saved' page source.
# for some reason 'view source' didn't work for me, so I grabbed the whole <body> tag in the element inspector
with open('facebook_saved.html', 'r') as f:
    source = f.read()
soup = BS(source)

saves = soup.select('div._4bl9._tev')
links = [save.select_one('div._4bl9._5yjp').select_one('a') for save in saves]
savedfrom = [save.select_one('a._24-t') for save in saves]

export = []
for i in range(len(saves)):
    l = links[i]['href']
    # add facebook url if internal link
    if l[0] == '/':
        l = 'https://www.facebook.com' + l
    try: 
        f = 'https://www.facebook.com' + savedfrom[i]['href']
    except:
        f = ''
    export.append({'link':l, 'from':f})

# not sure what format to export in yet. using a dictionary for now
export_str = [str(e) for e in export]
with open('facebook_saved.txt', 'w') as f:
    f.write(','.join(export_str))
