import requests
from bs4 import BeautifulSoup

print('Input the URL:')
url = input()
r = requests.get(url)

if r.status_code != 200:
    print(f'The URL returned {r.status_code}!')
else:
    file = open('source.html', 'wb')
    file.write(r.content)
    print('Content saved.')
    file.close()

# if r.status_code != 200 or 'nature.com' not in url or 'articles' not in url:
#     print('Invalid page!')
# else:
#     soup = BeautifulSoup(r.content, 'html.parser')
#     title = soup.title.string
#     meta = soup.find('meta', {'name': 'description'}).get('content')
#     result = {
#         'title' : title,
#         'description' : meta
#     }
#     print(result)

