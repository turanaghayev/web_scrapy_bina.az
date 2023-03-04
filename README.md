#  Bina.az  Web Scrapy


## Saving CSV Files With Feeds Setting
settings.py  

FEED_FORMAT = "csv"
FEED_URI = "bina_az_scrapy.csv"

##  Set A Fake User-Agent In Scrapy and 'utf-8'
settings.py

FEED_EXPORT_ENCODING = 'utf-8'
USER_AGENT = 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'

## The limiting depth for the spider to crawl a target site
settings.py

DEPTH_LIMIT
