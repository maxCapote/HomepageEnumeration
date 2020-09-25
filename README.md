# HomepageEnumeration
* Primary references
  * beautifulsoup4
    * https://pypi.org/project/beautifulsoup4/
    * https://www.crummy.com/software/BeautifulSoup/bs4/doc/
  * tldextract
    * https://pypi.org/project/tldextract/
* Simple enumeration tool for web application testing. Hyperlinks are extracted from a given URL and the domain as well as subdomain is determined for each. The SSL expiration date of each site is checked too, if applicable. This project was part of the application process for BreachLock.
* Example usage
  * python enumerate.py -u 'https://www.google.com/'
  * python enumerate.py -u 'https://www.google.com/' -e 'google.csv'
