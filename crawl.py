from HTMLParser import HTMLParser
from urllib2 import urlopen
import urlparse
class Parser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            self.handle_a(attrs)

    def error(self, message):
        print(message)

    def handle_a(self, attrs):
        for (attribute, value) in attrs:
            if attribute == 'href':
                url = urlparse.urljoin('https://thenewboston.com/', value)
                print(attribute + ': ' + url)


response = urlopen('https://thenewboston.com/')
htmlString = ''
# Only parse page if it is html
if dict(response.info())['content-type'] == 'text/html':
    htmlBytes = response.read()
    htmlString = htmlBytes.decode("utf-8")
parser = Parser()
parser.feed(htmlString)