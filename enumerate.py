import requests
from bs4 import BeautifulSoup
from tldextract import extract
import pandas as pd
import argparse

def get_webpage(url):
    # retrieve HTML of provided URL
    return requests.get(url).content

def extract_hyperlinks(webpage):
    # parse the HTML retrieved
    soup = BeautifulSoup(webpage, 'html.parser')
    # extract all hyperlinks (specifically denoted by <a> tags)
    links = []
    for link in soup.find_all('a'):
        links.append(link.get('href'))
    return links

def clean_hyperlinks(url, links):
    # remove telephone numbers and unnecessary javascript
    links = [link for link in links if 'tel:' not in link and 'javascript:' not in link]
    # modify links internal to the URL that lead with '#' and '/'
    links = [url + link if link[:1] == '#'
             else url[:-1] + link if link[:1] == '/'
             else link for link in links]
    # remove duplicate links
    links = list(dict.fromkeys(links))
    # return alphabetically sorted list of links
    return sorted(links)

def get_domain_info(links):
    # extract domin and subdomain from each link
    return [[extract(link).domain, extract(link).subdomain] for link in links]

def get_ssl_expiry_date():
    pass

def compile_results(links, domain_info):
    domains = [di[0] for di in domain_info]
    subdomains = [di[1] for di in domain_info]
    return pd.DataFrame({'Link': links, 'Domain': domains, 'Subdomin': subdomains})

def Main():
    parser = argparse.ArgumentParser(description = 'command-line args')
    parser.add_argument('-u', '--url', help='URL of target web application')
    parser.add_argument('-e', '--export', help='filename of target CSV to export results to')
    args = parser.parse_args()
    if args.url is not None:
        links = extract_hyperlinks(get_webpage(args.url))
        links = clean_hyperlinks(args.url, links)
        domain_info = get_domain_info(links)
        results = compile_results(links, domain_info)
        print(results)
        if args.export is not None:
            results.to_csv(args.export, index=False)
    else:
        print('usage: python enumerate.py [-u URL]')

if __name__ == '__main__':
    Main()
