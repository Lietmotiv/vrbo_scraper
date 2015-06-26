import scraperwiki
from pyquery import PyQuery

url = 'http://www.vrbo.com/373926'

q = PyQuery(url)

print q('.ratesdetails').text()


