"""
 Challenge: Scrape Wikipedia h2 Headers

Use the `requests` and `BeautifulSoup` libraries to fetch the Wikipedia page on Python (programming language).

Your task is to:
1. Download the HTML of the page.
2. Parse all `<h2>` section headers.
3. Store the clean header titles in a list.
4. Print the total count and display the first 10 section titles.

Bonus:
- Remove any trailing "[edit]" from the headers.
- Handle network errors gracefully.
"""


import requests
from bs4 import BeautifulSoup


# URL= "https://pelupa.in"
URL= "https://en.wikipedia.org/wiki/Python_(programming_language)"


def get_h2_header(url):
    try:
        response=requests.get(url,headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'} ,timeout=10)
        response.raise_for_status()

    except requests.RequestException as e:
        print(f"Failed to fetch page: \n {e} ")
        return []
    
    soup=BeautifulSoup(response.text, "html.parser")
    h2_tags=soup.find_all("h2")
    # print(h2_tags)
    headers= []
    for tag in h2_tags:
        header_text=tag.get_text(strip=True)
        if header_text and header_text.lower() != "headline":
            headers.append(header_text)
    return headers

def main():

    list = get_h2_header(URL)
    print(f"Total header {len(list)}")
    count =0
    for header in list[0:10]:
        count+=1
        print(f"{count}. {header} \n")

if __name__ == "__main__":
    main()