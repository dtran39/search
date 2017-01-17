from HTMLParser import HTMLParser
import urlparse


class LinkFinder(HTMLParser):

    def __init__(self, base_url, page_url):
        # https://www.peterbe.com/plog/python-new-style-classes-and-super   
        HTMLParser.__init__(self)
        self.base_url = base_url
        self.page_url = page_url
        self.links = set()

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for (attribute, value) in attrs:
                if attribute == 'href':
                    url = urlparse.urljoin(self.base_url, value)
                    self.links.add(url)

    def get_page_links(self):
        return self.links

    def error(self, message):
        pass
