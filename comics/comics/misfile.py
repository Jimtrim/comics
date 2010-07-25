from comics.aggregator.crawler import CrawlerBase, CrawlerImage
from comics.meta.base import MetaBase

class Meta(MetaBase):
    name = 'Misfile'
    language = 'en'
    url = 'http://www.misfile.com/'
    start_date = '2004-03-01'
    rights = 'Chris Hazelton'

class Crawler(CrawlerBase):
    history_capable_days = 10
    schedule = 'Mo,Tu,We,Th,Fr'
    time_zone = -8

    def crawl(self, pub_date):

        # Use the RSS feed to look up the page by the date...
        feed = self.parse_feed('http://www.misfile.com/misfileRSS.php')
        for entry in feed.for_date(pub_date):
            url = entry.link

            # ... then, convert that into an image...
            url = url.replace('?', 'overlay.php?')
            url = url.replace('page', 'pageCalled')
            
            # ... and bail out.
            return CrawlerImage(url)
