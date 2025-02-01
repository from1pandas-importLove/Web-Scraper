import requests
from bs4 import BeautifulSoup
import re
import os


page_n = int(input())
type_of_article = input()


for number in range(1, page_n + 1):
    os.mkdir(f'Page_{number}')
    # print('The current working directory is', str(os.getcwd()) + f'/Page_{number}/')

    # URL to scrape
    url = f'https://www.nature.com/nature/articles?sort=PubDate&year=2020&page={number}'

    # Request the page
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to fetch the page. Status code: {response.status_code}")
        exit()

    # Parse the page with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all articles
    articles = soup.find_all('article')

    # Base URL for constructing full article links
    base_url = 'https://www.nature.com'

    for article in articles:
        # Detect the article type
        span = article.find('span', {'data-test': 'article.type'})
        if span:
            nested_span = span.find('span', class_='c-meta__type')
            if nested_span and nested_span.text.strip() == type_of_article:
                # Find the link to view the article
                view_link = article.find('a', {'data-track-action': 'view article'})
                if view_link and view_link.get('href'):
                    article_url = base_url + view_link.get('href')

                    # Fetch the article content
                    article_response = requests.get(article_url)
                    if article_response.status_code == 200:
                        article_soup = BeautifulSoup(article_response.content, 'html.parser')

                        # Extract the article title
                        title_tag = article_soup.find('title')
                        if title_tag:
                            title = title_tag.text.strip()
                            # Sanitize filename
                            filename = title.replace(' ', '_')  # Replace spaces with underscores
                            filename = re.sub(r'[<>:"/\\|?*]', '', filename) + '.txt'

                            # Extract the article body
                            teaser = article_soup.find('p', {'class': 'article__teaser'})
                            if teaser:
                                article_text = teaser.text.strip()

                                # Save to file
                                path = str(os.getcwd()) + f'/Page_{number}/' + filename

                                with open(path, 'w', encoding='utf-8') as file:
                                    file.write(article_text)
                                    # print(f"Saved: {filename}")


print('Saved all articles.')
