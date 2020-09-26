# HomepageEnumeration
* Simple enumeration tool for web application testing. Hyperlinks are extracted from a given URL and the domain as well as subdomain is determined for each. The SSL expiration date of each site is checked too, if applicable. This project was part of the application process for BreachLock.
* Example usage
  * python enumerate.py -u 'https://www.google.com/'
  * python enumerate.py -u 'https://www.google.com/' -e 'google.csv'
* Primary references
  * beautifulsoup4
    * https://pypi.org/project/beautifulsoup4/
    * https://www.crummy.com/software/BeautifulSoup/bs4/doc/
  * tldextract
    * https://pypi.org/project/tldextract/
  * SSL info
    * https://stackoverflow.com/questions/45810069/how-to-fetch-the-ssl-certificate-value-whether-its-expired-or-not/52298575
    * https://stackoverflow.com/questions/30862099/how-can-i-get-certificate-issuer-information-in-python
* Other notes
  * The current version has only been tested in Windows and works only within PowerShell
